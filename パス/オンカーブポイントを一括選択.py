# MenuTitle: オンカーブポイントを一括選択
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
スムースなオンカーブポイント（緑丸）を一括選択します。
Select only smooth on-curve points (green circles).
"""

# フォントオブジェクトを取得
font = Glyphs.font
thisLayer = font.selectedLayers[0]

# 選択したレイヤーが存在するか確認
if not thisLayer:
    print("選択されたレイヤーがありません。")
else:
    # 各パスを処理
    for thisPath in thisLayer.paths:
        # 各ノードを処理
        for thisNode in thisPath.nodes:
            # スムースなオンカーブポイントの場合は選択
            if thisNode.smooth:
                thisNode.selected = True

    print("スムースなオンカーブポイントが選択されました。")
