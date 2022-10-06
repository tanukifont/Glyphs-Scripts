#MenuTitle: 長方形の短辺を削除
# -*- coding: utf-8 -*-
__doc__="""
閉じた選択パス中の、短い2辺を削除します。
"""


Glyphs.clearLog()


font = Glyphs.font
layer = font.selectedLayers[0]
glyph = layer.parent


try:
	layer.beginChanges()

	pathArray = [] 
	delArray = []

	if len(layer.paths) > 0:	# レイヤーにパスがある場合
		for pathIndex, path in enumerate(layer.paths):
			if path.selected and path.closed:	#閉じられた選択パスがある場合
				selectedNodes = []
				for node in path.nodes:
					if node.selected and node.type != OFFCURVE:
						selectedNodes.append(node)
				if len(selectedNodes) > 0:		# パスにオンカーブポイントがある場合
#					newPath = GSPath()
					nodeDic = {}
					for nodeIndex, node in enumerate(selectedNodes):
						
						# ノードの終点判定
						if node == selectedNodes[-1]:
							node1 = node
							node2 = selectedNodes[0]
						else:
							node1 = node
							node2 = selectedNodes[nodeIndex + 1]

						pathLength = round(((node2.x-node1.x)**2 + (node2.y - node1.y)**2)**0.5)
						(index, length) = node1.index , pathLength
						print(index,length)
						nodeDic[index] = length

					print(nodeDic, len(nodeDic))
					
					nodeDic2 = sorted(nodeDic.items(), key=lambda x:x[1])
					print(nodeDic2)
					print(nodeDic2[0][0],nodeDic2[1][0])
					cutNode1 = path.nodes[nodeDic2[0][0]]
					cutNode2 = path.nodes[nodeDic2[1][0]]
					cutId1 = nodeDic2[0][0]
					cutId2 = nodeDic2[1][0]
					print(cutId1, cutId2, len(nodeDic))
#					print(selectedNodes)
					newPath1 = GSPath()
					newPath2 = GSPath()

					# 一本目の線
					for i in range(cutId1+1,cutId2+1):
						#print(selectedNodes[i])
						newPath1.addNode_(path.nodes[i].copy())

					pathArray.append(newPath1)

					#二本目の線
					for i in range(cutId2+1,len(path.nodes)):
						#print(i)
						newPath2.addNode_(path.nodes[i].copy())
					for i in range(0,cutId1+1):
						#print(i)
						newPath2.addNode_(path.nodes[i].copy())

					pathArray.append(newPath2)
					
					
					print(pathArray)

				delArray.append(pathIndex) # 削除リストに追加

		# オリジナルのパスを削除
		for delIndex in reversed(delArray):
			del(layer.shapes[delIndex])
			
		# 開いたパスを適用
		for path in pathArray:
			layer.shapes.append(path)


finally:
	layer.endChanges()

