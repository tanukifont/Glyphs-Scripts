#MenuTitle: LTTR/INK設定値を出力
# -*- coding: utf-8 -*-

__doc__="""
LTTR/INKプラグインに関する設定値を出力します。
"""

# GlyphsApp モジュールをインポート
import GlyphsApp

# GlyphsApp 内のフォントを取得
font = Glyphs.font

# ログをクリア
Glyphs.clearLog()

# Letterink プラグインの設定値を出力
try:
    # Letterink プラグインのファイルバージョンを出力
    print("Letterink-FileVersion:", font.userData.get("Letterink-FileVersion", "未設定"))

    # Letterink プラグインの最小互換性マーケティングバージョンを出力
    print("Letterink-MinimumCompatibleMarketingVersion:", font.userData.get("Letterink-MinimumCompatibleMarketingVersion", "未設定"))

    # フォント内の Nib Styles の数を出力
    nib_styles = font.userData.get("Letterink-NibStyles", [])
    print("Letterink-NibStyles:", len(nib_styles))

    # マスターとそれぞれの Nib Styles の設定値を出力
    print('--------')
    print('Masters')
    print('--------')

    for master in font.masters:
        print(master.name)
        print(master.userData.get("Letterink-NibData", "未設定"))

    print('--------')
    print('Nib Styles')
    print('--------')

    # Nib Styles の詳細情報を出力
    print('#AngleInDegrees: ｘ軸方向（右）を0°とする回転角度の、マスターからの差分')
    print('#MainAxisWidth: 楕円のx軸（横軸）方向の直径の、マスターからの差分')
    print('#MinorAxisWidth: 楕円のy軸（縦軸）方向の直径の、マスターからの差分')
    print('#ValidForParentMainAxisWidth: マスターの楕円のx軸（横軸）方向の直径')
    print('#ValidForParentMinorAxisWidth: マスターの楕円のy軸（縦軸）方向の直径')

    # 各 Nib Styles の情報を出力
    for style in nib_styles:
        print(style)
        print('--------')

    print('--------')
    print('LTTR/INK が有効なレイヤー')
    print('--------')

    # 各グリフの各レイヤーで Letterink が有効になっている場合、グリフ名を出力
    for glyph in font.glyphs:
        for layer in glyph.layers:
            if layer.userData.get("Letterink-ComputationAllowed", False):
                print(layer.parent.name)

except Exception as e:
    print("エラーが発生しました:", e)

print("--------")
