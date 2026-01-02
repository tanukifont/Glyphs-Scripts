#MenuTitle: 選択した文字をランダムに並び替えたタブを作成
# -*- coding: utf-8 -*-
__doc__="""
現在選択しているグリフをランダムにシャッフルし、新しいタブで開きます。
"""

from GlyphsApp import *
import random

def main():
    # 1. フォントオブジェクトの取得確認
    font = Glyphs.font
    if not font:
        Message("エラー", "フォントが開かれていません。")
        return

    # 2. 選択されたグリフオブジェクト自体を取得
    # 名前だけでなくグリフオブジェクト(layer.parent)を取得して操作します
    selected_glyphs = [layer.parent for layer in font.selectedLayers]

    # 3. 選択チェック
    if not selected_glyphs:
        Glyphs.showNotification("スクリプトメッセージ", "グリフが選択されていません。")
        print("グリフが選択されていません。")
        return

    # 4. シャッフル処理
    random.shuffle(selected_glyphs)
    
    # 5. 文字列の生成処理
    
    # A. タブ用文字列（Glyphs内部用: /uni4E00/close-han ...）
    # 必ずスラッシュ付きのグリフ名にして、確実にそのグリフを表示させます
    tab_text = "".join(["/%s" % g.name for g in selected_glyphs])

    # B. 表示用文字列（人間用: 一〆三...）
    display_chars = []
    for g in selected_glyphs:
        # グリフに割り当てられた文字(Unicode)があるか確認
        if g.string:
            display_chars.append(g.string)
        else:
            # Unicodeがないグリフ（合字など）は分かりやすく名前で表記
            display_chars.append("(%s)" % g.name)
            
    display_text = "".join(display_chars)

    # 6. 新しいタブで開く
    font.newTab(tab_text)

    # 7. 結果の通知
    # マクロパネルへ出力
    print("-" * 20)
    print(f"{len(selected_glyphs)} 個のグリフを並べ替えました。")
    print(f"内容: {display_text}")
    print(f"内部名: {tab_text}")
    print("-" * 20)

    # 通知ダイアログ（改行を含めて見やすく表示）
    # Glyphs.showNotification は短い通知用なので、長文が見やすいMessage等も検討できますが
    # ここでは通知スタイルで内容を表示します。
    notification_msg = f"内容: {display_text}"
    Glyphs.showNotification(f"{len(selected_glyphs)} 個を並べ替え", notification_msg)

if __name__ == '__main__':
    main()