#MenuTitle: Align Selection Group to Center
# -*- coding: utf-8 -*-
__doc__="""
選択したパスをグループ状態で位置調整（水平中心）
"""
#バウンディングボックスで位置状態を取得するので、極点を追加しておくのがベスト

Glyphs.clearLog()

font = Glyphs.font
layer = font.selectedLayers[0]
selectedNodeFlag = len(layer.selection) > 0	#>0をつけることで、True　or Flaseの返り値になる

#asc = layer.ascender
#desc = layer.descender

#print('asc:' + str(asc))
#print('desc:' + str(desc))

layerWidth = layer.width
#layerHeight = layer.ascender - layer.descender

#print('layerHeight:' + str(layerHeight))
#print('layerHeight:' + str(layerHeight))

selWidth = layer.selectionBounds.size.width
#selHeight = layer.selectionBounds.size.height

#print('selWidth:' + str(selWidth))
#print('selHeight:' + str(selHeight))

selMinX = layer.selectionBounds.origin.x
#selMinY = layer.selectionBounds.origin.y

#print('selMinX:' + str(selMinX))
#print('selMinY:' + str(selMinY))

layerWidthCenter = layerWidth/2
#layerHeightCenter = layerHeight/2
selWidthCenter = selMinX + selWidth/2
#selHeightCenter = selMinY + selHeight/2

#print('layerWidthCenter:' + str(layerWidthCenter))
#print('selWidthCenter:' + str(selWidthCenter))
#print('layerHeightCenter:' + str(layerHeightCenter))
#print('selHeightCenter:' + str(selHeightCenter))

#選択ノードのx,y座標を移動する
for thisPath in layer.paths:
	for thisNode in thisPath.nodes:
		if not thisNode.selected:		#選択ノードではない場合は、処理をスキップ
			continue
		thisNode.x += layerWidthCenter - selWidthCenter
#		thisNode.y += layerHeightCenter + desc - selHeightCenter
