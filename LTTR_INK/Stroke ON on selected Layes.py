#MenuTitle: LetterInk On with selected layer
# -*- coding: utf-8 -*-
#Edit by Tanukizamurai
__doc__="""
選択したレイヤーのLetterInk(LTTR/INK)設定をオンにします。表示更新にはまだ非対応。
"""

font = Glyphs.font
layers = font.selectedLayers

Glyphs.clearLog()

#print(layer.userData)
#print(layer.userData["Letterink-ComputationAllowed"])

for layer in layers:

	if layer.userData["Letterink-ComputationAllowed"] == "YES":
		print("LetterInk is already on about this layer.")
	else:
		print("Turned LetterInk ON " + str(layer.parent.name))
		layer.userData["Letterink-ComputationAllowed"] = "YES"
	
