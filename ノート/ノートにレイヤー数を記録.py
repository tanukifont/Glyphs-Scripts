# MenuTitle: ノートにレイヤー数を記録
# -*- coding: utf-8 -*-
# 作成者: Tanukizamurai
__doc__="""
選択したグリフのレイヤー数をカウントし、グリフのノート（メモ）にその値を追加します。
ノートをクリアするオプションも追加しました。
"""

import vanilla

def add_layer_count_to_note():
    # Glyphsアプリ内のフォントオブジェクトを取得
    font = Glyphs.font

    # 選択したレイヤーを取得
    selectedLayers = font.selectedLayers

    # 選択したレイヤーが存在しない場合の処理
    if not selectedLayers:
        print("選択されたレイヤーがありません。")
        return

    # ダイアログUIを作成
    class LayerCountDialog:
        def __init__(self):
            self.w = vanilla.FloatingWindow((220, 100), "レイヤー数カウント")
            self.w.text = vanilla.TextBox((10, 10, -10, 20), "ノートにレイヤー数を追加します。")
            self.w.clear_note = vanilla.CheckBox((10, 40, -10, 20), "既存のノートをクリアして書き込む", value=False)
            self.w.run_button = vanilla.Button((-80, -30, -10, -10), "実行", callback=self.run)
            self.w.open()

        def run(self, sender):
            # 既存のノートをクリアするかどうかを取得
            clear_note = self.w.clear_note.get()

            # 選択した各レイヤーに対して処理を実行
            for thisLayer in selectedLayers:
                # レイヤーが所属するグリフオブジェクトを取得
                thisGlyph = thisLayer.parent

                # グリフのレイヤー数をカウント
                layerCount = len(thisGlyph.layers)

                # グリフ名を取得
                glyphName = thisGlyph.name

                # 既存のノートをクリアする場合
                if clear_note:
                    thisGlyph.note = 'layercount:' + str(layerCount)
                else:
                    # グリフのノートを取得
                    glyphNote = thisGlyph.note or ''

                    # ノートをスペースで分割してリスト化
                    splitNote = glyphNote.split()

                    # レイヤー数をノートの先頭に挿入
                    splitNote.insert(0, 'layercount:' + str(layerCount))

                    # リスト内の要素をスペースで結合して最終的なノートを作成
                    finalNote = ' '.join(splitNote)

                    # グリフのノートを更新
                    thisGlyph.note = finalNote

                # 処理の結果をログに表示
                print(f'ノートに追加: グリフ名: {glyphName} レイヤー数: {layerCount}')

            # ダイアログを閉じる
            self.w.close()

    LayerCountDialog()

add_layer_count_to_note()
