#MenuTitle: TanuEiKakuPop Auto Biting
# -*- coding: utf-8 -*-
__doc__="""
"""

# Special Thanks: Toshi Omagari
# This python script is based on the script that he provided me.


overlap = 100 # グリフの重なる量
offsetThickness = 40 # アウトラインの太さ

do_Offset = True # アウトラインのやり直し True or False
do_Components = True # コンポーネントグリフのやり直し True or False
do_Features = True # クラスとフィーチャーのやり直し True or False

prev_overlaps_later = False	#前の文字が上に重なるように設定、Falseの時は後の文字が上になる

# かな文字・数字ではないが噛み合って欲しいグリフ名のリスト。コンマ区切りで各グリフ名は""囲い
# フィーチャーグループの仕様通りの順番で記述すること。（要確認）
commonGlyphNames = ["comma-han" , "period-han" , "wavedash" , "prolonged-kana"]
commonNumGlyphNames = ["comma"]



import GlyphsApp

Glyphs.clearLog()	#マクロウィンドウのログ消去

f = Glyphs.font

f.disableUpdateInterface() #フォントビューの表示更新をOFFにする

# オフセットフィルターを選択
for offsetFilter in Glyphs.filters:
	if offsetFilter.__class__.__name__ == 'GlyphsFilterOffsetCurve':
		break

hiraganas = []	#ひらがなリスト
katakanas = []	#カタカナリスト
numbersHalf = []	#全角数字リスト

for g in f.glyphs:
	if g.unicodes != None and g.category == 'Letter':	#Unicodeが存在、かつカテゴリーが「Letter」の場合
		if g.name[-4:] == 'hira':	#名前の末尾が「hira」の場合はひらがなリストにレイヤーを追加
			hiraganas.append(g.layers[0])
		elif g.name[-4:] == 'kata':	#名前の末尾が「kata」の場合はカタカナリストにレイヤーを追加
			katakanas.append(g.layers[0])

	if g.unicodes != None and g.category == 'Number':	#同様に数字リストの作成を実行
		if g.name[-5:] != '.full':
			numbersHalf.append(g.layers[0])

print("NumbersHalf_count:" + str(len(numbersHalf)))

commons = []	#その他一般リスト
for c in commonGlyphNames:	#commonGlyphNamesリストの文字列を参照して、その他一般リストにレイヤーを追加
	try:
		commons.append(f.glyphs[ c ].layers[0] )
	except:
		pass
commonNums = []	#その他数字追加リスト
for n in commonNumGlyphNames:	#commonGlyphNamesリストの文字列を参照して、その他一般リストにレイヤーを追加
	try:
		commonNums.append(f.glyphs[ n ].layers[0] )
	except:
		pass

# print(commons)

#濁点・半濁点用のレイヤーリストを設定
additionals = [ f.glyphs['voicedcomb-kana'].layers[0], f.glyphs['semivoicedcomb-kana'].layers[0] ]

#マスク用レイヤーの作成
if do_Offset is True:
	layersToMask = hiraganas + katakanas + numbersHalf + commons + commonNums + additionals	#マスクが必要なレイヤーのリストを設定
	for l in layersToMask:
		g = l.parent
		print('create mask: ',g.name)
		if not f.glyphs[ "_mask."+g.name ]:						#過去にマスク用グリフを作成していない場合
			f.addGlyphCopy_(g)									#コピー元のグリフを複製
			f.glyphs[g.name + ".001"].name = "_mask."+g.name	#複製したグリフ（拡張子001のグリフ）の名前を、先頭を「_mask.」にしたグリフ名に変更
			maskLayer = f.glyphs[ "_mask."+g.name ].layers[0]	#maskLayerの設定
			maskLayer.parent.setColorIndex_(3)					#グリフのカラーラベルを「黄色」に設定
			
		else: 													#すでに同名のマスク用グリフが存在している場合
			maskLayer = f.glyphs[ "_mask."+g.name ].layers[0]	#maskLayerの設定
			maskLayer.shapes = []								#maskLayerのシェイプを消去
			for s in l.shapes:
				maskLayer.shapes.append(s.copy())				#コピー元のシェイプをマスク用レイヤーにコピー

		maskGlyph = maskLayer.parent		#maskGlyphの設定
		maskGlyph.export = False			#出力時に含めない
		maskGlyph.leftMetricsKey = None		#メトリクスキーを消去
		maskGlyph.rightMetricsKey = None
		maskGlyph.widthMetricsKey = None

		maskLayer.decomposeComponents()		#全てのコンポーネントを分解
		maskLayer.removeOverlap()			#オーバーラップ輪郭の削除
		thi = str(offsetThickness/2)		#アウトラインの1/2の太さを設定
		offsetFilter.processLayer_withArguments_(maskLayer, ['GlyphsFilterOffsetCurve', thi, thi, '0', '0'])	#オフセットの実行
		maskLayer.background.shapes = []	#背景レイヤーのシェイプを消去
		for s in l.shapes:
			maskLayer.background.shapes.append(s.copy())	#背景レイヤーにコピー元のシェイプをコピー

#オルタネート用グリフの作成(def)
def makeComponents(layers):
	for l0 in layers:			#レイヤー「l0」を設定
		g0 = l0.parent			#グリフ「g0」を設定
		for l1 in layers:		#レイヤー「l1」を設定
			toChange = False	#「toChange」（変更の必要性）フラグをFalseに設定
			g1 = l1.parent		#かじる側のグリフ「g1」を設定
			print('bited',g0.name,'by',g1.name)
			suffix = g1.name
			ngName = "%s.%s" % (g0.name, suffix)	#作成するグリフ名を設定
			if not f.glyphs[ngName]: 	#作成するオルタネートグリフ名がまだ作成されていない場合
				toChange = True			#「toChange」フラグをTrueに変更
				f.addGlyph_(GSGlyph(ngName))	#グリフを新規追加
			ng = f.glyphs[ngName]		#グリフ「ng」（オルタネートグリフ）を設定
			nl = ng.layers[0]			#レイヤー「nl」（オルタネートグリフ）を設定
			#カーニング量の取得
			kernValue = f.kerningForPair(f.selectedFontMaster.id, g1.name , g0.name)
			# print('kerning Value:',kernValue)

			# if toChange is False:
			# 	try:
			# 		toChange = True if ng.colorIndex != 8 else toChange				#オルタネートグリフのカラーラベルが紫でなければ「toChange」をTrueに変更
			# 		toChange = True if nl.width != l0.width-overlap else toChange	#オルタネートグリフのレイヤーの幅が「元のグリフ幅-重なり量」でなければ「toChange」をTrueに変更
			# 		toChange = True if nl.shapes[0].x != -overlap else toChange		#オルタネートグリフの1番目のシェイプのx座標が「-重なり量」の位置でなければ「toChange」をTrueに変更
			# 		toChange = True if nl.shapes[1].x != -l1.width else toChange	#オルタネートグリフの2番目のシェイプのx座標が「-（かじる側のグリフ幅）」の位置でなければ「toChange」をTrueに変更
			# 	except:
			# 		toChange = True

			toChange = True

			if toChange:
				ng.setColorIndex_(8)	#オルタネートグリフのカラーラベルを紫に設定
				nl.shapes = []			#オルタネートグリフのシェイプを消去
				ng.widthMetricsKey = "=%s-%s" % (g0.name, overlap)	#文字幅メトリクスを「元のグリフ幅-重なり量」に設定
				nl.addShape_(GSComponent(g0.name))					#オルタネートグリフに右側（かじられる側）グリフのシェイプをコピー
				nl.addShape_(GSComponent('_mask.'+g1.name))			#オルタネートグリフに左側（マスク用のかじる側）グリフシェイプをコピー

				if prev_overlaps_later:
					ng.leftMetricsKey = ""						#右メトリクスキーに右側（かじられる側）グリフの名前を設定
					ng.rightMetricsKey = g0.name						#右メトリクスキーに右側（かじられる側）グリフの名前を設定
				else:
					ng.leftMetricsKey = g0.name						#右メトリクスキーに右側（かじられる側）グリフの名前を設定
					ng.rightMetricsKey = ""						#右メトリクスキーに右側（かじられる側）グリフの名前を設定


				c0, c1 = nl.shapes[0], nl.shapes[1]					#c0に「かじられる側」、c1に「かじる側」のシェイプを設定
				c0.makeDisableAlignment()							#c0,c1の整列を解除
				c1.makeDisableAlignment()
				c1.setAttribute_forKey_(1, 'mask')					#c1をmaskに設定
				if prev_overlaps_later:
					c0.x = - overlap									#c0のx座標を「-重なり量」の位置に移動
					c1.x = - l1.width									#c1のx座標を「-（かじる側のグリフ幅）」に移動
				else:
					c0.x = 0									#c0のx座標を「-重なり量」の位置に移動
					c1.x = l0.width - overlap									#c1のx座標を「-（かじる側のグリフ幅）」に移動
				nl.syncMetrics()									#メトリクスを更新

if do_Components is True:		#do_ComponentフラグがTrueなら実行
	if len(hiraganas) > 0:		#ひらがなが存在するときmakeComponentsを実行
		makeComponents(hiraganas+commons)
	if len(katakanas) > 0:		#カタカナが存在するときmakeComponentsを実行
		makeComponents(katakanas+commons)
	if len(numbersHalf) > 0:	#半角数字が存在するときmakeComponentsを実行
		makeComponents(numbersHalf+commonNums)

#フィーチャーの設定

if do_Features is True:										#do_FeaturesフラグがTrueなら実行
	classPrefixCode = ''									#プレフィックステキスト用変数の初期設定
	caltFeatureCode = "lookup BITE useExtension {\n"		#caltフィーチャーテキストの初期設定
	hiraganaNames = [l.parent.name for l in hiraganas]		#グリフ名リスト「hiraganaNames」を定義
	katakanaNames = [l.parent.name for l in katakanas]		#グリフ名リスト「katakanaNames」を定義
	commonsNames = [l.parent.name for l in commons]			#グリフ名リスト「commonsName」を定義
	commonNumsNames = [l.parent.name for l in commonNums]			#グリフ名リスト「commonNumsName」を定義
	numbersHalfNames = [l.parent.name for l in numbersHalf]		#グリフ名リスト「numbersHalf」を定義

	if len(hiraganas) > 0:
		#かじられていないプレーンなひらがなグループを追記
		classPrefixCode += "@clean_hira=[$[name endswith '-hira' and countOfUnicodes > 0 and category == 'Letter'] %s ];\n" % " ".join(commonsNames)
		for hn in hiraganaNames:
			#かじる側グリフ（Widthが重なり分小さいグリフ）グループを追記
			classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (hn, hn)
			# classPrefixCode += "@biting_%s=[$[name beginswith '%s'] %s ];\n" % (hn, hn, " ".join([hn + "." + commonsNameWithSuffix for commonsNameWithSuffix in commonsNames]))
		for hn in hiraganaNames:
			#かじられる側グリフグルーブを追記
			classPrefixCode += "@bit_by_%s=[$[name endswith '-hira.%s'] %s ];\n" % (hn, hn, " ".join([commonsNameWithSuffix + "." + hn for commonsNameWithSuffix in commonsNames]))
			#ひらがな用caltフィーチャーを追記
			if prev_overlaps_later:
				caltFeatureCode +="sub @biting_%s @clean_hira' by @bit_by_%s;\n" % (hn, hn)
			else:
				caltFeatureCode +="sub @clean_hira' @biting_%s by @bit_by_%s;\n" % (hn, hn)
				# caltFeatureCode +="sub @biting_%s' @clean_hira by @bit_by_%s;\n" % (hn, hn)


	if len(katakanas) > 0:
		classPrefixCode += "@clean_kata=[%s];\n" % " ".join(katakanaNames+commonsNames)
		for kn in katakanaNames:
			classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (kn, kn)
		for kn in katakanaNames:
			classPrefixCode += "@bit_by_%s=[$[name endswith '-kata.%s'] %s ];\n" % (kn, kn, " ".join([commonsNameWithSuffix + "." + kn for commonsNameWithSuffix in commonsNames]))			
			#カタカナ用caltフィーチャーを追記
			if prev_overlaps_later:
				caltFeatureCode +="sub @biting_%s @clean_kata' by @bit_by_%s;\n" % (kn, kn)
			else:
				caltFeatureCode +="sub @clean_kata' @biting_%s by @bit_by_%s;\n" % (kn, kn)

	# cleanH = "@clean_hira" if len(hiraganas) > 0 else ""
	# cleanK = "@clean_kata" if len(katakanas) > 0 else ""

	classPrefixCode += "@clean_hira_and_kata=[%s];\n" % " ".join(hiraganaNames+katakanaNames+commonsNames)

	for cn in commonsNames:
		classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (cn, cn)
		classPrefixCode += "@bit_by_%s=[$[name endswith '.%s']];\n" % (cn, cn)
		# caltFeatureCode +="sub @biting_%s [@clean_hira_and_kata]' by @bit_by_%s;\n" % (cn, cn)
		#コモングリフ用caltフィーチャーを追記
		if prev_overlaps_later:
			caltFeatureCode +="sub @biting_%s [@clean_hira_and_kata]' by @bit_by_%s;\n" % (cn, cn)
		else:
			caltFeatureCode +="sub [@clean_hira_and_kata]' @biting_%s by @bit_by_%s;\n" % (cn, cn)

	if len(numbersHalf) > 0:
		classPrefixCode += "@clean_numHalf=[%s];\n" % " ".join(numbersHalfNames+commonNumsNames)
		for nh in numbersHalfNames:
			classPrefixCode += "@biting_%s=[$[name beginswith '%s' AND NOT name contains '.full']];\n" % (nh, nh)
		for nh in numbersHalfNames:
			classPrefixCode += "@bit_by_%s=[$[name endswith '.%s'] ];\n" % (nh, nh)			
			#半角数字用caltフィーチャーを追記
			if prev_overlaps_later:
				caltFeatureCode +="sub @biting_%s @clean_numHalf' by @bit_by_%s;\n" % (nh, nh)
			else:
				caltFeatureCode +="sub @clean_numHalf' @biting_%s by @bit_by_%s;\n" % (nh, nh)

	classPrefixCode += "@clean_nums=[%s];\n" % " ".join(numbersHalfNames+commonNumsNames)

	for cnn in commonNumsNames:
		classPrefixCode += "@biting_%s=[$[name beginswith '%s']];\n" % (cnn, cnn)
		classPrefixCode += "@bit_by_%s=[$[name endswith '.%s']];\n" % (cnn, cnn)
		# caltFeatureCode +="sub @biting_%s [@clean_hira_and_kata]' by @bit_by_%s;\n" % (cn, cn)
		#コモングリフ用caltフィーチャーを追記
		if prev_overlaps_later:
			caltFeatureCode +="sub @biting_%s [@clean_nums]' by @bit_by_%s;\n" % (cnn, cnn)
		else:
			caltFeatureCode +="sub [@clean_nums]' @biting_%s by @bit_by_%s;\n" % (cnn, cnn)

	caltFeatureCode +="} BITE;"

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


f.enableUpdateInterface() #フォントビューの表示更新をONに戻す

print('マクロ処理完了')
