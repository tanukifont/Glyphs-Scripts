#MenuTitle: サイドベアリング一括増減
# -*- coding: utf-8 -*-
__doc__="""
フォントのメトリクスを調整するためのダイアログを表示します。
左サイドベアリング（LSB）、右サイドベアリング（RSB）、上サイドベアリング（TSB）、下サイドベアリング（BSB）の変更量を入力できます。
全てのグリフに対して調整するか、選択したグリフのみに調整するかを選択できます。
"""

# Vanillaをインポート
from vanilla import *

# ダイアログクラスを定義
class MetricsAdjustmentDialog:
    def __init__(self):
        self.w = Window((385, 200), "メトリクス調整")  # 横幅を400、縦幅を300に設定
        
        # 全体または選択グリフのオプション
        self.w.allGlyphsCheckbox = CheckBox((10, 10, 380, 20), "全てのグリフに対して調整（オフ：選択グリフのみ）", callback=self.updateCheckbox)
        
        # LSB変更量の入力フィールド
        self.w.LSBLabel = TextBox((10, 40, 250, 20), "左サイドベアリング（LSB）の変更量:")
        self.w.LSBInput = EditText((270, 40, 100, 20), "0")

        # RSB変更量の入力フィールド
        self.w.RSBLabel = TextBox((10, 70, 250, 20), "右サイドベアリング（RSB）の変更量:")
        self.w.RSBInput = EditText((270, 70, 100, 20), "0")

        # TSB変更量の入力フィールド
        self.w.TSBLabel = TextBox((10, 100, 250, 20), "上サイドベアリング（TSB）の変更量:")
        self.w.TSBInput = EditText((270, 100, 100, 20), "0")

        # BSB変更量の入力フィールド
        self.w.BSBLabel = TextBox((10, 130, 250, 20), "下サイドベアリング（BSB）の変更量:")
        self.w.BSBInput = EditText((270, 130, 100, 20), "0")

        # 実行ボタン
        self.w.runButton = Button((10, 160, 360, 30), "実行", callback=self.run)
        
        self.w.open()

    def updateCheckbox(self, sender):
        # チェックボックスの状態に応じて入力フィールドを更新
        if self.w.allGlyphsCheckbox.get():
            self.w.LSBLabel.set("全てのグリフに対する左サイドベアリング（LSB）の変更量:")
            self.w.RSBLabel.set("全てのグリフに対する右サイドベアリング（RSB）の変更量:")
            self.w.TSBLabel.set("全てのグリフに対する上サイドベアリング（TSB）の変更量:")
            self.w.BSBLabel.set("全てのグリフに対する下サイドベアリング（BSB）の変更量:")
        else:
            self.w.LSBLabel.set("左サイドベアリング（LSB）の変更量:")
            self.w.RSBLabel.set("右サイドベアリング（RSB）の変更量:")
            self.w.TSBLabel.set("上サイドベアリング（TSB）の変更量:")
            self.w.BSBLabel.set("下サイドベアリング（BSB）の変更量:")

    def run(self, sender):
        try:
            # 入力値を取得
            LSB_adjustment = float(self.w.LSBInput.get())
            RSB_adjustment = float(self.w.RSBInput.get())
            TSB_adjustment = float(self.w.TSBInput.get())
            BSB_adjustment = float(self.w.BSBInput.get())
        except ValueError:
            print("無効な数値が入力されました。")
            return
        
        # Glyphsのフォントオブジェクトを取得
        font = Glyphs.font
        
        # 全体に対して調整する場合
        if self.w.allGlyphsCheckbox.get():
            for glyph in font.glyphs:
                for layer in glyph.layers:
                    # 現在のメトリクスを保存
                    original_LSB = layer.LSB
                    original_RSB = layer.RSB
                    original_TSB = layer.TSB
                    original_BSB = layer.BSB

                    # メトリクスを変更
                    layer.LSB += LSB_adjustment
                    layer.RSB += RSB_adjustment
                    layer.BSB += BSB_adjustment
                    layer.TSB += TSB_adjustment
                    
                    # グリフごとにメトリクスの変更を出力
                    print(f"グリフ: {glyph.name} - 修正前: TSB: {original_TSB}, BSB: {original_BSB}, LSB: {original_LSB}, RSB: {original_RSB} | 修正後: TSB: {layer.TSB}, BSB: {layer.BSB}, LSB: {layer.LSB}, RSB: {layer.RSB}")

        # 選択されたグリフに対して調整する場合
        else:
            selectedGlyphs = font.selectedLayers
            for layer in selectedGlyphs:
                glyph = layer.parent  # レイヤーの親グリフを取得
                
                # 現在のメトリクスを保存
                original_LSB = layer.LSB
                original_RSB = layer.RSB
                original_TSB = layer.TSB
                original_BSB = layer.BSB

                # メトリクスを変更
                layer.LSB += LSB_adjustment
                layer.RSB += RSB_adjustment
                layer.BSB += BSB_adjustment
                layer.TSB += TSB_adjustment
                
                # グリフごとにメトリクスの変更を出力
                print(f"グリフ: {glyph.name} - 修正前: TSB: {original_TSB}, BSB: {original_BSB}, LSB: {original_LSB}, RSB: {original_RSB} | 修正後: TSB: {layer.TSB}, BSB: {layer.BSB}, LSB: {layer.LSB}, RSB: {layer.RSB}")

# ダイアログを開く
MetricsAdjustmentDialog()
