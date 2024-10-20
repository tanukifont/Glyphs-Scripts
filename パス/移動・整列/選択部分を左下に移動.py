# MenuTitle: 選択部分を左下に移動
# -*- coding: utf-8 -*-
__doc__="""
左下の座標が（0, ディセンダー値）になるようにパスを移動します。
"""

# ログをクリア
Glyphs.clearLog()

# フォントオブジェクトを取得
font = Glyphs.font
layer = font.selectedLayers[0]

# レイヤーのディセンダー値とバウンディングボックスの取得
descender = layer.descender
nodeMinX = layer.bounds.origin.x
nodeMinY = layer.bounds.origin.y

# パスのノード座標を移動する
for thisPath in layer.paths:
    for thisNode in thisPath.nodes:
        # ノードの座標を更新
        thisNode.x += -nodeMinX  # x座標を左に移動
        thisNode.y += descender - nodeMinY  # y座標を下に移動

print("すべてのパスの位置が左下に移動しました。")
