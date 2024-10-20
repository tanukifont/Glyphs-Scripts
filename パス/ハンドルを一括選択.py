# MenuTitle: ハンドルを一括選択
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
ハンドルのみを一括選択します。
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
            # ノードのタイプとスムース状態を確認
            print(thisNode.type, thisNode.smooth)
            # オフカーブノードの場合は選択状態にする
            if thisNode.type == "offcurve":
                thisNode.selected = True

    print("オフカーブノードが選択されました。")
