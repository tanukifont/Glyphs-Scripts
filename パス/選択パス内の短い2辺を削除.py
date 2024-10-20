# MenuTitle: 選択パス内の短い2辺を削除
# -*- coding: utf-8 -*-
__doc__="""
閉じたパスを選択し、そのうちの短い2辺を削除します。
"""

Glyphs.clearLog()

font = Glyphs.font
layer = font.selectedLayers[0]
glyph = layer.parent

try:
    layer.beginChanges()

    pathArray = [] 
    delArray = []

    if len(layer.paths) > 0:  # レイヤーにパスがある場合
        for pathIndex, path in enumerate(layer.paths):
            if path.selected and path.closed:  # 閉じられた選択パスがある場合
                selectedNodes = [node for node in path.nodes if node.selected and node.type != OFFCURVE]

                if len(selectedNodes) > 0:  # パスにオンカーブポイントがある場合
                    nodeDic = {}
                    for nodeIndex, node in enumerate(selectedNodes):
                        # ノードの終点判定
                        node1 = node
                        node2 = selectedNodes[(nodeIndex + 1) % len(selectedNodes)]  # 循環参照

                        # パスの長さを計算
                        pathLength = round(((node2.x - node1.x) ** 2 + (node2.y - node1.y) ** 2) ** 0.5)
                        nodeDic[nodeIndex] = pathLength

                    # 対になるパスとの合計で短辺を決定
                    calcEdge = [nodeDic[i] + nodeDic[i + len(selectedNodes)//2] for i in range(len(selectedNodes)//2)]
                    minEdge = min(calcEdge)
                    cutId1 = calcEdge.index(minEdge)
                    cutId2 = cutId1 + len(selectedNodes) // 2

                    # 新しいパスを作成
                    newPath1 = GSPath()
                    newPath2 = GSPath()

                    # 一本目の線
                    for i in range(cutId1 + 1, cutId2 + 1):
                        newPath1.addNode_(path.nodes[i].copy())
                    pathArray.append(newPath1)

                    # 二本目の線
                    for i in range(cutId2 + 1, len(path.nodes)):
                        newPath2.addNode_(path.nodes[i].copy())
                    for i in range(0, cutId1 + 1):
                        newPath2.addNode_(path.nodes[i].copy())
                    pathArray.append(newPath2)

                delArray.append(pathIndex)  # 削除リストに追加

        # オリジナルのパスを削除
        for delIndex in reversed(delArray):
            del(layer.shapes[delIndex])
            
        # 新しいパスを適用
        for newPath in pathArray:
            layer.shapes.append(newPath)

finally:
    layer.endChanges()

print("短い辺が削除され、新しいパスが作成されました。")
