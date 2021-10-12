#MenuTitle:	Select On-Curve Points
# -*- coding: utf-8 -*-
#Edit by Tanukizamurai

__doc__="""
スムースなオンカープポイント（緑丸）を一括選択します。
Select only smooth on-curve points (green circles).
"""

font = Glyphs.font
thisLayer = font.selectedLayers[0]

for thisPath in thisLayer.paths:
	for thisNode in thisPath.nodes:
		if thisNode.smooth == True:
			thisNode.selected = True