#MenuTitle: 選択部分をボディ全体にフィット
# -*- coding: utf-8 -*-
__doc__="""
選択したレイヤー内のすべてのパスをボディ全体にフィットさせます。
"""

# ログをクリア
Glyphs.clearLog()

# Glyphsフォントオブジェクトを取得
font = Glyphs.font

if not font.selectedLayers:
    Glyphs.showNotification("エラー", "選択されたレイヤーがありません。")
else:
    for layer in font.selectedLayers:
        # アセンダーとディセンダーの取得
        asc = layer.ascender
        desc = layer.descender

        # レイヤーの幅と高さを取得
        layerWidth = layer.width
        layerHeight = asc - desc

        # フレームの幅と高さを取得
        frameWidth = layer.bounds.size.width
        frameHeight = layer.bounds.size.height

        # ノードの最小座標を取得
        nodeMinX = layer.bounds.origin.x
        nodeMinY = layer.bounds.origin.y

        # スケールを計算
        scaleX = layerWidth / frameWidth
        scaleY = layerHeight / frameHeight

        # 各パスのノードを移動
        for thisPath in layer.paths:
            for thisNode in thisPath.nodes:
                thisNode.x -= nodeMinX  # 左に移動
                thisNode.y -= nodeMinY  # 下に移動
                thisNode.x *= scaleX     # スケールを適用
                thisNode.y *= scaleY     # スケールを適用
                thisNode.y += desc       # ディセンダーの値だけ下に移動

    # 完了メッセージを表示
    Glyphs.showNotification("配置完了", "すべてのパスが左下に移動しました。")
