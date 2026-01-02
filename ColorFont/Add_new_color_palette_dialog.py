# MenuTitle: 新規カラーパレットを追加...
# -*- coding: utf-8 -*-
__doc__="""
カスタムパラメータ「Color Palettes」に新しいカラーパレットを追加するためのダイアログを表示します。
マスターを選び、パレット番号とRGB値を0-255の値で指定して新しいカラーパレットを追加します。
"""

# GlyphsAppモジュールをインポート
import GlyphsApp
from vanilla import Window, TextBox, EditText, Button, List

# ダイアログを作成するクラス
class ColorPaletteDialog:
    def __init__(self):
        font = Glyphs.font  # フォントオブジェクトを取得
        
        # ウィンドウサイズを(300, 400)に設定
        self.dialog = Window((300, 400), "新規カラーパレット追加")
        
        # マスターのリストボックス
        masterNames = [master.name for master in font.masters]
        self.dialog.masterListLabel = TextBox((10, 10, -10, 20), "マスターを選択:")
        self.dialog.masterList = List((10, 30, -10, 100), masterNames, 
                                      selectionCallback=self.masterSelectionChanged)
        
        # カラーパレット番号 (初期値0)
        self.dialog.paletteIndexLabel = TextBox((10, 140, -10, 20), "カラーパレットの番号 (0-9):")
        self.dialog.paletteIndex = EditText((10, 160, -10, 20), "0")

        # RGB値の入力 (初期値: R=255, G=0, B=0)
        self.dialog.redValueLabel = TextBox((10, 190, -10, 20), "R値 (0-255):")
        self.dialog.redValue = EditText((10, 210, -10, 20), "255")
        
        self.dialog.greenValueLabel = TextBox((10, 240, -10, 20), "G値 (0-255):")
        self.dialog.greenValue = EditText((10, 260, -10, 20), "0")
        
        self.dialog.blueValueLabel = TextBox((10, 290, -10, 20), "B値 (0-255):")
        self.dialog.blueValue = EditText((10, 310, -10, 20), "0")
        
        # 追加ボタン
        self.dialog.addButton = Button((10, 340, -10, 20), "追加", callback=self.addColor)

        self.dialog.open()

    # リストボックスで選択されたマスターが変更されたときに呼ばれるコールバック
    def masterSelectionChanged(self, sender):
        selectedMasterIndex = sender.getSelection()
        if selectedMasterIndex:
            selectedMasterName = Glyphs.font.masters[selectedMasterIndex[0]].name
            print(f"選択されたマスター: {selectedMasterName}")

    # 追加ボタンのコールバック
    def addColor(self, sender):
        font = Glyphs.font
        selectedMasterIndex = self.dialog.masterList.getSelection()

        if not selectedMasterIndex:
            print("エラー: マスターが選択されていません。")
            return

        try:
            # 入力値を取得
            paletteIndex = int(self.dialog.paletteIndex.get())
            rValue = int(self.dialog.redValue.get())
            gValue = int(self.dialog.greenValue.get())
            bValue = int(self.dialog.blueValue.get())
            
            # RGB値の範囲をチェック
            if not (0 <= rValue <= 255 and 0 <= gValue <= 255 and 0 <= bValue <= 255):
                raise ValueError("RGB値は0-255の範囲内でなければなりません。")
            
            # 追加する色（RGB値のリスト）
            newColor = [rValue, gValue, bValue]

            # 選択されたマスターを取得
            selectedMaster = font.masters[selectedMasterIndex[0]]
            colorPalettes = selectedMaster.customParameters['Color Palettes']
            if colorPalettes:
                # カラーパレットのリストをコピー
                updatedPalettes = [list(palette) for palette in colorPalettes]
                
                # 指定されたパレット番号に新しい色を追加
                if 0 <= paletteIndex < len(updatedPalettes):
                    updatedPalettes[paletteIndex].append(newColor)
                    # 更新されたカラーパレットを再設定
                    selectedMaster.customParameters['Color Palettes'] = updatedPalettes
                    print(f"Master: {selectedMaster.name}のカラーパレット {paletteIndex} に新しい色を追加しました：{newColor}")
                else:
                    print(f"指定されたカラーパレット番号 {paletteIndex} は無効です。")
            else:
                print(f"Master: {selectedMaster.name}にはカラーパレットが設定されていません。")
            
            # スクリプト実行後に変更内容を確認するためにフォントを保存
            font.save()

        except ValueError as e:
            print(f"エラー: {e}")

# ダイアログを表示
ColorPaletteDialog()
