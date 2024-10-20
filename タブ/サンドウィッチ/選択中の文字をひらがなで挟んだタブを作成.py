#MenuTitle: 選択中の文字をひらがなで挟んだタブを作成
# -*- coding: utf-8 -*-
__doc__="""
選択中の文字を「ひらがな」で挟んだテキストのタブを作成します。
"""

import GlyphsApp

# ログをクリア
Glyphs.clearLog()

# フォントオブジェクトを取得
font = Glyphs.font
selectedLayers = font.selectedLayers

# ひらがなを挟むための文字リスト
breads = [
    "a-hira", "asmall-hira", "i-hira", "ismall-hira", "u-hira", "usmall-hira",
    "e-hira", "esmall-hira", "o-hira", "osmall-hira", "ka-hira", "ga-hira",
    "ki-hira", "gi-hira", "ku-hira", "gu-hira", "ke-hira", "ge-hira",
    "ko-hira", "go-hira", "sa-hira", "za-hira", "si-hira", "zi-hira",
    "su-hira", "zu-hira", "se-hira", "ze-hira", "so-hira", "zo-hira",
    "ta-hira", "da-hira", "ti-hira", "di-hira", "tu-hira", "tusmall-hira",
    "du-hira", "te-hira", "de-hira", "to-hira", "do-hira", "na-hira",
    "ni-hira", "nu-hira", "ne-hira", "no-hira", "ha-hira", "ba-hira",
    "pa-hira", "hi-hira", "bi-hira", "pi-hira", "hu-hira", "bu-hira",
    "pu-hira", "he-hira", "be-hira", "pe-hira", "ho-hira", "bo-hira",
    "po-hira", "ma-hira", "mi-hira", "mu-hira", "me-hira", "mo-hira",
    "ya-hira", "yasmall-hira", "yu-hira", "yusmall-hira", "yo-hira",
    "yosmall-hira", "ra-hira", "ri-hira", "ru-hira", "re-hira", "ro-hira",
    "wa-hira", "wasmall-hira", "wi-hira", "we-hira", "wo-hira", "n-hira",
    "vu-hira"
]

# タブに追加するテキストを初期化
tabText = ""

# 選択したレイヤーがない場合のエラーハンドリング
if not selectedLayers:
    Glyphs.showNotification("エラー", "レイヤーが選択されていません。")
else:
    # 選択したレイヤーごとに処理
    for layer in selectedLayers:
        # 各レイヤーに対してひらがなを挟む処理を行う
        for hira in breads:
            tabText += f"/{layer.parent.name}/{hira}"
        tabText += f"/{layer.parent.name}\n\n"
    
    # 新しいタブを作成
    font.newTab(tabText)
    Glyphs.showNotification("タブ作成完了", "ひらがなで挟んだタブを作成しました。")
