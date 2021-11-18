#MenuTitle:	Select Off-curve Points
# -*- coding: utf-8 -*-
#Edit by Tanukizamurai

__doc__="""
ハンドルのみを一括選択します。
Select only off-curve points (blue square).
"""

font = Glyphs.font
thisLayer = font.selectedLayers[0]

for thisPath in thisLayer.paths:
	for thisNode in thisPath.nodes:
		print(thisNode.type, thisNode.smooth)
		if thisNode.type == "offcurve":
			thisNode.selected = True