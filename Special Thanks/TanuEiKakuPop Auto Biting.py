#MenuTitle: TanuEiKakuPop Auto Biting
# -*- coding: utf-8 -*-
__doc__="""
"""



overlap = 100 # グリフの重なる量
offsetThickness = 15 # アウトラインの太さ
do_Offset = True # アウトラインのやり直し True or False
do_Components = True # コンポーネントグリフのやり直し True or False
do_features = True # クラスとフィーチャーのやり直し True or False

# かな文字ではないが噛み合って欲しいグリフ名のリスト。コンマ区切りで各グリフ名は""囲い
commonGlyphNames = ["prolonged-kana"]





import GlyphsApp
f = Glyphs.font
Glyphs.clearLog()
f.disableUpdateInterface() # suppresses UI updates in Font View

# find offset filter
for offsetFilter in Glyphs.filters:
	if offsetFilter.__class__.__name__ == 'GlyphsFilterOffsetCurve':
		break

hiraganas = []
katakanas = []
for g in f.glyphs:
	if g.unicodes != None and g.category == 'Letter':
		if g.name[-4:] == 'hira':
			hiraganas.append(g.layers[0])
		elif g.name[-4:] == 'kata':
			katakanas.append(g.layers[0])

commons = []
for c in commonGlyphNames:
	try:
		commons.append(f.glyphs[ c ].layers[0] )
	except:
		pass

additionals = [ f.glyphs['voicedcomb-kana'].layers[0], f.glyphs['semivoicedcomb-kana'].layers[0] ]

# Make mask layers first
if do_Offset is True:
	layersToMask = hiraganas + katakanas + commons + additionals
	for l in layersToMask:
		g = l.parent
		if not f.glyphs[ "_mask."+g.name ]: # glyph doesn't exist yet
			f.addGlyphCopy_(g)
			f.glyphs[g.name + ".001"].name = "_mask."+g.name
			maskLayer = f.glyphs[ "_mask."+g.name ].layers[0]
			maskLayer.parent.setColorIndex_(3)


		else: # glyph exists. re-import paths
			maskLayer = f.glyphs[ "_mask."+g.name ].layers[0]
			maskLayer.shapes = []
			for s in l.shapes:
				maskLayer.shapes.append(s.copy())

		maskGlyph = maskLayer.parent
		maskGlyph.export = False
		maskGlyph.leftMetricsKey = None
		maskGlyph.rightMetricsKey = None
		maskGlyph.widthMetricsKey = None

		maskLayer.decomposeComponents()
		for s in maskLayer.shapes:
			s.addNodesAtExtremes()
		thi = str(offsetThickness/2)
		offsetFilter.processLayer_withArguments_(maskLayer, ['GlyphsFilterOffsetCurve', thi, thi, '0', '0'])
		maskLayer.background.shapes = []
		for s in l.shapes:
			maskLayer.background.shapes.append(s.copy())

# Make all the alternate glyphs
def makeComponents(layers):
	for l0 in layers:
		g0 = l0.parent # g0 is parent
		for l1 in layers:
			toChange = False
			g1 = l1.parent # g1 is biting
			suffix = g1.name[:-5] if g1.name[-5:] in ("-hira", "-kata") else g1.name
			ngName = "%s.%s" % (g0.name, suffix) # remove -hira or -kata
			if not f.glyphs[ngName]: # glyph doesn't exist yet
				toChange = True
				f.addGlyph_(GSGlyph(ngName))
			ng = f.glyphs[ngName]
			nl = ng.layers[0]

			if toChange is False:
				try:
					toChange = True if ng.colorIndex != 8 else toChange
					toChange = True if nl.width != l0.width-overlap else toChange
					toChange = True if nl.shapes[0].x != -overlap else toChange
					toChange = True if nl.shapes[1].x != -l1.width else toChange
				except:
					toChange = True

			if toChange:
				ng.setColorIndex_(8)
				nl.shapes = []
				ng.widthMetricsKey = "=%s-%s" % (g0.name, overlap)
				ng.rightMetricsKey = g0.name
				nl.addShape_(GSComponent(g0.name))
				nl.addShape_(GSComponent("_mask."+g1.name))
				c0, c1 = nl.shapes[0], nl.shapes[1]
				c0.makeDisableAlignment()
				c1.makeDisableAlignment()
				c1.setAttribute_forKey_(1, 'mask')
				c0.x = - overlap
				c1.x = - l1.width
				nl.syncMetrics()

if do_Components is True:
	if len(hiraganas) > 0:
		makeComponents(hiraganas+commons)
	if len(katakanas) > 0:
		makeComponents(katakanas+commons)

# Rewrite features:

if do_features is True:
	classPrefixCode = ''
	caltFeatureCode = ''
	hiraganaNames = [l.parent.name for l in hiraganas]
	katakanaNames = [l.parent.name for l in katakanas]
	commonsNames = [l.parent.name for l in commons]
	if len(hiraganas) > 0:
		classPrefixCode += "@clean_hira=[$[name endswith '-hira' and countOfUnicodes > 0] %s ];\n" % " ".join(commonsNames)
		for hn in hiraganaNames:
			classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (hn, hn)
		for hn in hiraganaNames:
			classPrefixCode += "@bit_by_%s=[$[name endswith '-hira.%s'] %s ];\n" % (hn, hn[:-5], " ".join(commonsNames))
			caltFeatureCode +="lookup bt_%s {sub @biting_%s @clean_hira' by @bit_by_%s; } bt_%s;\n" % (hn, hn, hn, hn)


	if len(katakanas) > 0:
		classPrefixCode += "@clean_kata=[%s];\n" % " ".join(katakanaNames+commonsNames)
		for kn in katakanaNames:
			classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (kn, kn)
		for kn in katakanaNames:
			classPrefixCode += "@bit_by_%s=[$[name endswith '%s']];\n" % (kn, kn)
			caltFeatureCode +="lookup bt_%s {sub @biting_%s @clean_kata' by @bit_by_%s; } bt_%s;\n" % (kn, kn, kn, kn)

	commonsNames = [l.parent.name for l in commons]
	cleanH = "@clean_hira" if len(hiraganas) > 0 else ""
	cleanK = "@clean_kata" if len(katakanas) > 0 else ""
	for cn in commonsNames:
		classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (cn, cn)
		classPrefixCode += "@bit_by_%s=[$[name endswith 'a.%s']];\n" % (cn, cn)
		caltFeatureCode +="lookup bt_%s {sub @biting_%s [%s %s]' by @bit_by_%s; } bt_%s;\n" % (cn, cn, cleanH, cleanK, cn, cn)

	try:
		if f.featurePrefixes['classes'] is None:
			cla = GSFeaturePrefix()
			cla.name = 'classes'
			cla.code = ''
			cla.automatic = False
			cla.active = True
			f.addFeaturePrefix_(cla)
		cla = f.featurePrefixes['classes']
		cla.code = classPrefixCode
	except:
		print('class update failed')

	try:
		if f.features['calt'] is None:
			fea = GSFeature()
			fea.name = 'calt'
			fea.code = ''
			fea.automatic = False
			fea.active = True
			f.addFeature_(fea)
		fea = f.features['calt']
		fea.code = caltFeatureCode
	except:
		print('feature update failed')

f.enableUpdateInterface() # re-enables UI updates in Font View