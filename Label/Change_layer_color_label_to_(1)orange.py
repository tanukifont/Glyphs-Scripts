# MenuTitle: レイヤーカラーラベルを🟠オレンジに変更
# -*- coding: utf-8 -*-
__doc__ = """
このスクリプトは、選択したグリフのレイヤーカラーラベルを🟠オレンジに設定します。
"""

# レイヤーカラーラベルの設定値
# 0: 赤
# 1: オレンジ
# 2: 茶色
# 3: 黄色
# 4: 明るい緑
# 5: 濃い緑
# 6: 明るい青
# 7: 濃い青
# 8: 紫
# 9: マゼンタ
# 10: 明るい灰色
# 11: 濃い灰色
# None: 未設定

# レイヤーカラーラベルの設定値
color = 1  # 🟠オレンジのレイヤーカラーラベル

# Glyphsアプリケーションのフォントオブジェクトを取得
Font = Glyphs.font

# 選択されたレイヤーを取得
layers = Font.selectedLayers

if not layers:
    print("選択されたレイヤーがありません。")
else:
    # GlyphsアプリケーションのUI更新を一時的に無効化
    Font.disableUpdateInterface()

    # 選択された各レイヤーに対してループ
    for layer in layers:
        # グリフのレイヤーカラーラベルを指定したレイヤーカラーラベルに設定
        layer.color = color
        # ログにメッセージを出力
        print("%s（%s）のレイヤーカラーラベルを🟠オレンジに変更しました" % (glyph.name, glyph.string))

    # GlyphsアプリケーションのUI更新を再度有効化
    Font.enableUpdateInterface()
