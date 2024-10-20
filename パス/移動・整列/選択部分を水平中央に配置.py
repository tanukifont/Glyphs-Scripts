#MenuTitle: 選択部分を水平中央に配置
# -*- coding: utf-8 -*-
__doc__="""
選択したノードをグループ化した状態で仮想ボディの中央に水平移動します。
バウンディングボックスを基準にして位置を取得するため、極点を追加しておく方が正確な移動ができます。
"""

import GlyphsApp

font = Glyphs.font

try:
    if not font.selectedLayers:
        raise ValueError("グリフが選択されていません。")
    
    # 選択したレイヤーを取得
    selected_layer = font.selectedLayers[0]
    
    # 選択されたノードがあるかチェック
    if len(selected_layer.selection) == 0:
        raise ValueError("ノードが選択されていません。")
    
    # レイヤーの情報を取得
    ascender = selected_layer.ascender
    descender = selected_layer.descender
    layer_width = selected_layer.width
    selection_bounds = selected_layer.selectionBounds
    sel_width = selection_bounds.size.width
    sel_min_x = selection_bounds.origin.x
    
    # 中央座標を計算
    layer_width_center = layer_width / 2
    sel_width_center = sel_min_x + sel_width / 2
    
    # 選択されたノードを移動
    for path in selected_layer.paths:
        for node in path.nodes:
            if node.selected:
                node.x += layer_width_center - sel_width_center
                # y座標の変更は行わない（水平移動のみ）

    Glyphs.showNotification("配置完了", "選択したパスを水平中央に配置しました。")
    
except Exception as e:
    Glyphs.showNotification("エラー", str(e))
