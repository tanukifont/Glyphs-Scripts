# MenuTitle: 直線からカーブに変換
# -*- coding: utf-8 -*-

__doc__="""
直線からハンドルを持ったカーブに変換します。
"""

import GlyphsApp
from Foundation import NSPoint

# ハンドル用ノードの座標計算 t=挿入位置係数 a,b=2点の座標  
def lerp(t, a, b):
    return NSPoint(int((1 - t) * a.x + t * b.x), int((1 - t) * a.y + t * b.y))

# フォントオブジェクトを取得
font = Glyphs.font
layer = font.selectedLayers[0]

# 選択されたノードが存在するか確認
selectedNodeFlag = len(layer.selection) > 0

# 各パスを処理
for p in layer.paths:
    # クローズパスの場合は-1まで、オープンパスの場合は0まで
    start = -1 if p.closed else 0
    nodeIdxList = range(len(p.nodes) - 1, start, -1)  # パスのノードインデックスリストを作成

    # 各ノードを処理
    for idx in nodeIdxList:
        node = p.nodes[idx]

        # ノードが選択されていない場合、スキップ
        if selectedNodeFlag and not node.selected:
            continue

        # ノードが直線の場合に処理を実行
        if node.type == LINE:
            prevNode = p.nodes[idx - 1]

            # ハンドル用のオフカーブノードを生成
            off1 = GSNode(lerp(0.33, prevNode.position, node.position), OFFCURVE)
            off2 = GSNode(lerp(0.66, prevNode.position, node.position), OFFCURVE)

            # ノードを挿入
            p.nodes.insert(idx, off2)
            p.nodes.insert(idx, off1)

            # 直線ノードをカーブノードに変更
            node.type = CURVE
            # node.connection = GSSMOOTH  # 必要に応じて接続タイプを変更

print("直線がカーブに変換されました。")
