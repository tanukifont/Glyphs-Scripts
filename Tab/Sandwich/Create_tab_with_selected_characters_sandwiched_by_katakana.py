#MenuTitle: 選択中の文字をカタカナで挟んだタブを作成
# -*- coding: utf-8 -*-
__doc__="""
選択中の文字を「カタカナ」で挟んだテキストのタブを作成します。
"""

import GlyphsApp

# ログをクリア
Glyphs.clearLog()

# フォントオブジェクトを取得
font = Glyphs.font
selectedLayers = font.selectedLayers

# カタカナを挟むための文字リスト
breads = [
    "a-kata", "asmall-kata", "i-kata", "ismall-kata", "u-kata", "usmall-kata",
    "e-kata", "esmall-kata", "o-kata", "osmall-kata", "ka-kata", "kasmall-kata",
    "ga-kata", "ki-kata", "gi-kata", "ku-kata", "gu-kata", "ke-kata",
    "kesmall-kata", "ge-kata", "ko-kata", "go-kata", "sa-kata", "za-kata",
    "si-kata", "zi-kata", "su-kata", "zu-kata", "se-kata", "ze-kata",
    "so-kata", "zo-kata", "ta-kata", "da-kata", "ti-kata", "di-kata",
    "tu-kata", "tusmall-kata", "du-kata", "te-kata", "de-kata", "to-kata",
    "do-kata", "na-kata", "ni-kata", "nu-kata", "ne-kata", "no-kata",
    "ha-kata", "ba-kata", "pa-kata", "hi-kata", "bi-kata", "pi-kata",
    "hu-kata", "bu-kata", "pu-kata", "he-kata", "be-kata", "pe-kata",
    "ho-kata", "bo-kata", "po-kata", "ma-kata", "mi-kata", "mu-kata",
    "me-kata", "mo-kata", "ya-kata", "yasmall-kata", "yu-kata", "yusmall-kata",
    "yo-kata", "yosmall-kata", "ra-kata", "ri-kata", "ru-kata", "re-kata",
    "ro-kata", "wa-kata", "wasmall-kata", "va-kata", "wi-kata", "vi-kata",
    "we-kata", "ve-kata", "wo-kata", "vo-kata", "n-kata", "vu-kata"
]

# タブに追加するテキストを初期化
tabText = ""

# 選択したレイヤーがあるか確認
if not selectedLayers:
    Glyphs.showNotification("エラー", "レイヤーが選択されていません。")
else:
    # 選択したレイヤーごとに処理
    for layer in selectedLayers:
        for bread in breads:
            tabText += f"/{layer.parent.name}/{bread}"  # f文字列を使用
        tabText += f"/{layer.parent.name}\n\n"  # 最後に元のグリフ名を追加
    # 新しいタブを作成
    font.newTab(tabText)
    Glyphs.showNotification("タブ作成完了", "カタカナで挟んだタブを作成しました。")
