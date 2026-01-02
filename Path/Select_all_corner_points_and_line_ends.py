# MenuTitle: コーナーポイント及び線端を一括選択
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
コーナーポイント（青四角）及び線端を一括選択します。
Select only corner points (blue square) and endpoints.
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
            # スムースでないノード（コーナーポイントまたは線端）の場合は選択
            if not thisNode.smooth:
                thisNode.selected = True

    print("コーナーポイントと線端が選択されました。")
