#MenuTitle: 選択した文字をランダムに並び替えたタブを作成
# -*- coding: utf-8 -*-
__doc__="""
選択した文字をランダムに並び替えたタブを作成します。
"""

from GlyphsApp import *
import random

# フォントオブジェクトを取得
font = Glyphs.font

# 選択されたグリフの名前をリスト形式で取得する関数
def get_selected_glyphs_characters():
    characters = []
    for layer in font.selectedLayers:
        glyph = layer.parent
        characters.append("/" + glyph.name)
    return characters

# ユーザーにメッセージを表示する関数
def show_message(message):
    Glyphs.showNotification("スクリプトメッセージ", message)
    print(message)  # マクロパネルにもメッセージを出力

# 選択されたグリフの名前を取得
characters = get_selected_glyphs_characters()

if len(characters) == 0:
    show_message("選択したグリフがありません。")
else:
    # 文字列をランダムに生成
    random.shuffle(characters)
    rdmChr = ''.join(characters)

    # 新しいタブでランダムな文字列を開く
    font.newTab(rdmChr)
    show_message("新しいタブが開かれました。\n" + rdmChr)
