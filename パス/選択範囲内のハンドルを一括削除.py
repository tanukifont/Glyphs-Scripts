# MenuTitle: 選択範囲内のハンドルを一括削除
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
選択範囲の中から、オフカーブノードのみを一括削除します。
Removes off-curve nodes from the selected area.
"""

import GlyphsApp

# フォントオブジェクトを取得
layer = Glyphs.font.selectedLayers[0]

# 選択されたノードがあるか確認
testSelection = len(layer.selection) > 0

# 各パスを処理
for path in layer.paths:
    # クローズパスの場合は-1まで、オープンパスの場合は0まで
    start = -1 if path.closed else 0
    
    # ノードのインデックスリストを逆順で作成
    for idx in range(len(path.nodes) - 1, start, -1):
        node = path.nodes[idx]

        # エラー処理: パスが選択されていない場合はスキップ
        if not testSelection:
            continue

        # ノードが選択されていない場合はスキップ
        if testSelection and not node.selected:
            continue

        # オフカーブノードの場合のみ処理を実行
        if node.type == OFFCURVE:
            path.removeNodeCheck_(node)  # ノードを削除

print("選択範囲からオフカーブノードが削除されました。")
