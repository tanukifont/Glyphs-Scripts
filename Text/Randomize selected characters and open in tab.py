#MenuTitle: 選択した文字をランダムにしてタブで開く
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
選択した文字をランダムにしてタブで開きます
Randomize selected characters and open in tab.
"""
from GlyphsApp import *

Font = Glyphs.font

# 選択されたグリフのstringをリスト形式で取得する
def get_selected_glyphs_characters():
    characters = []
    for layer in Glyphs.font.selectedLayers:
        glyph = layer.parent
        characters.append(glyph.string)
    return characters

# 選択されたグリフのstringをリスト形式で取得する
characters = get_selected_glyphs_characters()

# 文字列をランダム生成
random.shuffle(characters)
rdmChr = ''.join(characters)

Font.newTab(rdmChr)
print(rdmChr)
