#MenuTitle: 選択ノードにセグメントコンポーネントを適用
# -*- coding: utf-8 -*-
__doc__="""
選択したノードにセグメントコンポーネントを適用します。
"""

# GlyphsApp モジュールをインポート
import GlyphsApp

# 選択したレイヤーを取得
font = Glyphs.font
layer = font.selectedLayers[0]  # 最初の選択されたレイヤーを取得

# 選択したノードを取得
selected_nodes = layer.selection

# ノードが選択されているか確認
if not selected_nodes:
    print("ノードが選択されていません。")
else:
    # 最初のノード（制御点）を取得
    node = selected_nodes[0]

    # 新しいセグメントコンポーネントを作成します。
    newSeg = GSHint()

    # セグメントコンポーネントのタイプを19に設定します。タイプ19はセグメントを示します。
    newSeg.type = 19

    # セグメントの元となるノード（制御点）を指定します。
    newSeg.originNode = node

    # セグメントコンポーネントの名前を"_segment.brush"に設定します。
    newSeg.name = "_segment.brush"

    # 選択したレイヤーに新しいセグメントコンポーネントを追加します。
    layer.hints.append(newSeg)

    print(f"{node} にセグメントコンポーネントを適用しました。")
