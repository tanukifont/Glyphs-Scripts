#MenuTitle:	Delete Curve Node From Selected
# -*- coding: utf-8 -*-
#Edit by Tanukizamurai

__doc__="""
選択範囲の中から、オフカーブノードのみを一括選択します。
Removes curve nodes from the selected area.
"""

import GlyphsApp

Layer = Glyphs.font.selectedLayers[0]
testSelection = len(Layer.selection) > 0	#パスが選択されていればTrue

for p in Layer.paths:
	if p.closed:
		start = -1	#クローズパスの場合は-1まで
	else:
		start = 0	#オープンパスの場合は0まで
	for idx in range(len(p.nodes) - 1, start, -1):	#パスのノード数分のインデックスリストを作成
		node = p.nodes[idx]
		### エラー処理ここから
		if testSelection == False:	#パスが選択されていない場合は、処理をスキップ
			continue
		### エラー処理ここまで
		if testSelection and not node.selected:	#パスが選択されていても、選択されていないノードの場合は処理をスキップ
			continue
		if node.type == OFFCURVE:	#選択されたノードの属性がオフカーブポイントの場合のみ処理を実行
			p.removeNodeCheck_(node)	#ノードを削除


