#MenuTitle: 選択部分を垂直中央に配置
# -*- coding: utf-8 -*-
__doc__="""
選択したノードをグループ化した状態で仮想ボディの中央に垂直移動します。
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
    layer_height = ascender - descender
    selection_bounds = selected_layer.selectionBounds
    sel_height = selection_bounds.size.height
    sel_min_y = selection_bounds.origin.y
    
    # 中央座標を計算
    layer_height_center = layer_height / 2
    sel_height_center = sel_min_y + sel_height / 2
    
    # 選択されたノードを移動
    for path in selected_layer.paths:
        for node in path.nodes:
            if node.selected:
                node.y += layer_height_center + descender - sel_height_center
    
    Glyphs.showNotification("配置完了", "選択したパスを垂直中央に配置しました。")
    
except Exception as e:
    Glyphs.showNotification("エラー", str(e))
