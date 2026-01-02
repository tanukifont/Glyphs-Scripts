# MenuTitle: カラーラベルを🩷マゼンタに変更
# -*- coding: utf-8 -*-
__doc__ = """
このスクリプトは、選択したグリフのカラーラベルを🩷マゼンタに設定します。
"""

# カラーラベルの設定値
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

# カラーラベルの設定値
color = 9  # 🩷マゼンタのカラーラベル

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
        # グリフオブジェクトを取得
        glyph = layer.parent
        
        if glyph:
            # グリフのカラーラベルを指定したカラーラベルに設定
            glyph.color = color
            # ログにメッセージを出力
            print("%s（%s）のカラーラベルを🩷マゼンタに変更しました" % (glyph.name, glyph.string))
        else:
            print("グリフが見つかりません。")

    # GlyphsアプリケーションのUI更新を再度有効化
    Font.enableUpdateInterface()
