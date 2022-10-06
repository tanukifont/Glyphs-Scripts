#MenuTitle: Move All Paths Position to Left Bottom
# -*- coding: utf-8 -*-
__doc__="""
左下の座標が（0,ディセンダー値）になるようにパスを移動
"""

Glyphs.clearLog()

font = Glyphs.font
layer = font.selectedLayers[0]

desc = layer.descender
nodeMinX = layer.bounds.origin.x
nodeMinY = layer.bounds.origin.y

#x,y座標を移動する
for thisPath in layer.paths:
	for thisNode in thisPath.nodes:
		thisNode.x += 0 - nodeMinX
		thisNode.y += desc - nodeMinY
