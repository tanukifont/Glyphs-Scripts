#MenuTitle: 選択したレイヤーのLTTR/INKを有効化
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai
__doc__="""
選択したレイヤーのLTTR/INK設定をオンにします。表示更新にはまだ未対応です。
"""

# GlyphsApp モジュールをインポート
import GlyphsApp

# GlyphsApp 内のフォントを取得
font = Glyphs.font

# 選択したレイヤーを取得
layers = font.selectedLayers

# ログをクリア
Glyphs.clearLog()

# 選択したレイヤーがない場合の処理
if not layers:
    print("選択されたレイヤーがありません。")
else:
    # 選択した各レイヤーに対してループ処理
    for layer in layers:
        # LetterInk の設定を取得
        letterink_status = layer.userData.get("Letterink-ComputationAllowed", "NO")
        
        # もし既に LetterInk が有効になっている場合
        if letterink_status == "YES":
            print(f"{layer.parent.name} の LetterInk はすでに有効です。")
        else:
            # LetterInk をオンにし、メッセージを表示
            layer.userData["Letterink-ComputationAllowed"] = "YES"
            print(f"{layer.parent.name} の LetterInk をオンにしました。")
