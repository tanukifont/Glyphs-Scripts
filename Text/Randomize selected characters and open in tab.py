#MenuTitle: 選択した文字をランダムにしてタブで開く
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
選択した文字をランダムにしてタブで開きます
Randomize selected characters and open in tab.
"""
from GlyphsApp import *
import random

Font = Glyphs.font

# 選択されたグリフのstringをリスト形式で取得する
def get_selected_glyphs_characters():
    characters = []
    for layer in Glyphs.font.selectedLayers:
        glyph = layer.parent
        characters.append("/" + glyph.name)
    return characters

# ユーザーにメッセージを表示する関数
def show_message(message):
    Glyphs.showNotification("スクリプトメッセージ", message)
    print(message)  # マクロパネルにもメッセージを出力

# 選択されたグリフのstringをリスト形式で取得する
characters = get_selected_glyphs_characters()

if len(characters) == 0:
    show_message("選択したグリフがありません。")
else:
    # 文字列をランダム生成
    random.shuffle(characters)
    rdmChr = ''.join(characters)

    # 新しいタブでランダムな文字列を開く
    Font.newTab(rdmChr)
    show_message("新しいタブが開かれました。\n" + rdmChr)
