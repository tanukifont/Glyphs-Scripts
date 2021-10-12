#MenuTitle:	Count Layer and Edit Note
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai
__doc__="""
Count glyphs layers and add value to glyphs note.
"""


font = Glyphs.font
selectedLayers = font.selectedLayers


for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	layerCount = len(thisLayer.parent.layers)	#count layer
	glyphName = thisLayer.parent.name
	
	glyphNote = thisGlyph.note
	if glyphNote is None:
		glyphNote = ''
	splitNote = glyphNote.split()
	splitNote.insert(0, 'layercount:' + str(layerCount) + ' ')	#insert at head of note
	finalNote = ' '.join(splitNote)
	thisGlyph.note = finalNote	#update note
	print('add_note glyph:' + glyphName + ' ' + finalNote)
