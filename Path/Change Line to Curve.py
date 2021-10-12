#MenuTitle:	Change line to curve
# -*- coding: utf-8 -*-

__doc__="""
直線からハンドルを持ったカーブに変換します。
change line to curve.
"""

import GlyphsApp
from Foundation import NSPoint

# ハンドル用ノードの座標計算 t=挿入位置係数 a,b=2点の座標  
def lerp(t, a, b):
	return NSPoint(int((1-t)*a.x + t*b.x), int((1-t)*a.y + t*b.y))

font = Glyphs.font
layer = font.selectedLayers[0]
selectedNodeFlag = len(layer.selection) > 0	#>0をつけることで、True　or Flaseの返り値になる

for p in layer.paths:
	if p.closed:
		start = -1	#クローズパスの場合は-1まで
	else:
		start = 0	#オープンパスの場合は0まで
	nodeIdxList = range(len(p.nodes) - 1, start, -1)	#パスのノード数分のインデックスリストを作成
	for idx in nodeIdxList:
		node = p.nodes[idx]
		if selectedNodeFlag and not node.selected:		#パスが選択されていて、かつ現在のパスが選択パスではない場合は、処理をスキップ
			continue
		if node.type == LINE:	#選択されたノードの属性が直線の場合のみ、処理を実行
			prevNode = p.nodes[idx - 1]
			off1 = GSNode(lerp(0.33, prevNode.position, node.position), OFFCURVE)	#パスの1/3の位置にノードオブジェクト（off1）を作成
			off2 = GSNode(lerp(0.66, prevNode.position, node.position), OFFCURVE)	#パスの2/3の位置にノードオブジェクト（off2）を作成
			p.nodes.insert(idx, off2)	#ノードoff2をidxの次の位置に挿入
			p.nodes.insert(idx, off1)	#ノードoff1をidxの次の位置に挿入
			node.type = CURVE	#選択されたノードの属性を曲線に変更
			node.connection = GSSMOOTH

