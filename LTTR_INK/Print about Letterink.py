#MenuTitle: Print about Letterink
# -*- coding: utf-8 -*-
#Edit by Tanukizamurai

__doc__="""
Letterinkに関する設定値を出力します。
"""


font = Glyphs.font

Glyphs.clearLog()



#AngleInDegrees :　ｘ軸方向（右）を0°とする回転角度の、マスターからの差分
#MainAxisWidth : 楕円のx軸（横軸）方向の直径の、マスターからの差分
#MinorAxisWidth : 楕円のy軸（縦軸）方向の直径の、マスターからの差分
#ValidForParentMainAxisWidth : マスターの楕円のx軸（横軸）方向の直径
#ValidForParentMinorAxisWidth : マスターの楕円のy軸（縦軸）方向の直径


print("Letterink-FileVersion:" , font.userData["Letterink-FileVersion"])
print("Letterink-MinimumCompatibleMarketingVersion:" , font.userData["Letterink-MinimumCompatibleMarketingVersion"])


print("Letterink-NibStyles:" , len(font.userData["Letterink-NibStyles"]))

print('--------')
print('Masters')
print('--------')

for master in font.masters:
	print(master.name)
	print(master.userData["Letterink-NibData"])


print('--------')
print('Nib Styles')
print('--------')

print('#AngleInDegrees :　ｘ軸方向（右）を0°とする回転角度の、マスターからの差分')
print('#MainAxisWidth : 楕円のx軸（横軸）方向の直径の、マスターからの差分')
print('#MinorAxisWidth : 楕円のy軸（縦軸）方向の直径の、マスターからの差分')
print('#ValidForParentMainAxisWidth : マスターの楕円のx軸（横軸）方向の直径')
print('#ValidForParentMinorAxisWidth : マスターの楕円のy軸（縦軸）方向の直径')


for i in font.userData["Letterink-NibStyles"]:
	print(i)
#	print('--len_i--',len(i))
	print('--------')

print('--------')
print('LTTR/INK Stroke On this glyps layer')
print('--------')

for glyph in font.glyphs:
	for layer in glyph.layers:		
		if layer.userData["Letterink-ComputationAllowed"]:
			print(layer.parent.name)
print("--------")


