#MenuTitle: 2番目以降のレイヤーのパスをすべて最上位のレイヤーにコピー（フォールバック用グリフの作成_ダイアログ）
# -*- coding: utf-8 -*-
import vanilla

__doc__="""
一番上以外のレイヤーのパスをすべて一番上にコピー（フォールバック用グリフの作成）
"""

class CopyPathsDialog:
    def __init__(self):
        # ウィンドウの設定
        self.w = vanilla.FloatingWindow((300, 100), "フォールバック用グリフ作成処理対象の選択")
        
        # テキストラベル
        self.w.text = vanilla.TextBox((15, 12, -15, 14), "選択したグリフに対して処理を行いますか？")
        
        # ラジオボタンで選択肢を提供
        self.w.radioGroup = vanilla.RadioGroup((15, 30, -15, 40), ["選択グリフのみ", "すべてのグリフ"], isVertical=True)
        self.w.radioGroup.set(0)  # デフォルトで選択グリフのみを選択
        
        # OKボタン
        self.w.okButton = vanilla.Button((15, 70, -15, 20), "OK", callback=self.okCallback)
        
        self.w.open()
        self.w.makeKey()
    
    def okCallback(self, sender):
        # マクロパネルを開く
        Glyphs.clearLog()  # ログをクリア
        Glyphs.showMacroWindow()  # マクロパネルを開く

        # ユーザーが選択したラジオボタンの値を取得
        choice = self.w.radioGroup.get()

        # Glyphsのすべてのフォントでアクティブなフォントを取得
        font = Glyphs.font

        if choice == 0:  # 選択グリフのみを処理
            glyphs = font.selection
            print("選択グリフに対して処理を行います...")
        else:  # すべてのグリフを処理
            glyphs = font.glyphs
            print("すべてのグリフに対して処理を行います...")

        # 各グリフに対して処理
        for glyph in glyphs:
            layers = glyph.layers
            # 一番上のレイヤーを取得
            topLayer = layers[0]

            # 一番上のレイヤーの既存のパスをクリア
            for path in reversed(topLayer.paths):
                for node in reversed(path.nodes):
                    path.removeNodeCheck_(node)
            
            # 一番上のレイヤー以外のパスをコピー
            for otherLayer in layers[1:]:
                for path in otherLayer.paths:
                    newPath = path.copy()
                    topLayer.paths.append(newPath)

            # 処理が完了したグリフの名前を表示
            print(f"処理完了: {glyph.name}")

        print("\n全ての処理が完了しました。")
        
        # ウィンドウを閉じる
        self.w.close()

# ダイアログを開く
CopyPathsDialog()
