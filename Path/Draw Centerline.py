#MenuTitle: センターライン作成_Draw Centerline
# -*- coding: utf-8 -*-
__doc__="""
2つの選択パスの中間にパスを作成します
"""

font = Glyphs.font
selectedLayers = font.selectedLayers
layer = selectedLayers[0]
glyph = layer.parent


selectedPaths = []
for path in layer.paths:
	if path.selected:
		selectedPaths.append(path)
		print(selectedPaths)

Font.disableUpdateInterface()

if ( len(selectedPaths) == 2 ) and ( len(selectedPaths[0]) == len(selectedPaths[1]) ):
	newPath = GSPath()
	path_0 = selectedPaths[0]
	path_1 = selectedPaths[1]
	path_1.reverse()
	for thisNodeIndex in range(len(path_0.nodes)):
		thisNode = path_0.nodes[thisNodeIndex]
		foregroundPosition = thisNode.position
		backgroundPosition = path_1.nodes[thisNodeIndex].position
		newNode = GSNode()
		newNode.type = thisNode.type
		newNode.connection = thisNode.connection
		newNode.x = (foregroundPosition.x + backgroundPosition.x) * 0.5
		newNode.y = (foregroundPosition.y + backgroundPosition.y) * 0.5
		newPath.addNode_( newNode )
	if path_0.closed == True:
		newPath.setClosePath_(1)
	layer.paths.append( newPath )
	layer.roundCoordinates()
	
elif (len(selectedPaths) == 0):
	print("Paths are not selected.")	
else:
	print("Incorrect path has been selected. (len:%s,node:%s/%s)." % ( len(selectedPaths), len(selectedPaths[0]), len(selectedPaths[1])))

Font.enableUpdateInterface()
