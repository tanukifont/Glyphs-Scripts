#MenuTitle:	Select Corner Points
# -*- coding: utf-8 -*-
#Edit by Tanukizamurai

__doc__="""
コーナーポイント（青四角）及び線端を一括選択します。
Select only off-curve points (blue square).
"""

font = Glyphs.font
thisLayer = font.selectedLayers[0]

for thisPath in thisLayer.paths:
	for thisNode in thisPath.nodes:
		if thisNode.smooth == False:
			thisNode.selected = True