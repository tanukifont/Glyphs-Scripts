#MenuTitle: Move All Paths Position to Left Bottom
# -*- coding: utf-8 -*-
__doc__="""
枠付きのパスを全体にフィットさせます。
"""

Glyphs.clearLog()

font = Glyphs.font
layer = font.selectedLayers[0]

asc = layer.ascender
desc = layer.descender

layerWidth = layer.width
layerHeight = layer.ascender - layer.descender

frameWidth = layer.bounds.size.width
frameHeight = layer.bounds.size.height

nodeMinX = layer.bounds.origin.x
nodeMinY = layer.bounds.origin.y

scaleX = layerWidth / frameWidth
scaleY = layerHeight / frameHeight

for thisPath in layer.paths:
	for thisNode in thisPath.nodes:
		thisNode.x -= nodeMinX
		thisNode.y -= nodeMinY
		thisNode.x *= scaleX
		thisNode.y *= scaleY
		thisNode.y += desc	#ディセンダーの値だけ下に移動