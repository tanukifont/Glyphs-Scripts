from __future__ import unicode_literals

#MenuTitle: Hiragana-Sand
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
選択中の文字を「ひらがな」で挟んだテキストのタブを作成します。
Create tab of selected characters sandwiched in Hiragana.
"""
 
import GlyphsApp

Glyphs.clearLog()

font = Glyphs.font
selectedLayers = font.selectedLayers
breads = [
	"a-hira",
	"asmall-hira",
	"i-hira",
	"ismall-hira",
	"u-hira",
	"usmall-hira",
	"e-hira",
	"esmall-hira",
	"o-hira",
	"osmall-hira",
	"ka-hira",
	"ga-hira",
	"ki-hira",
	"gi-hira",
	"ku-hira",
	"gu-hira",
	"ke-hira",
	"ge-hira",
	"ko-hira",
	"go-hira",
	"sa-hira",
	"za-hira",
	"si-hira",
	"zi-hira",
	"su-hira",
	"zu-hira",
	"se-hira",
	"ze-hira",
	"so-hira",
	"zo-hira",
	"ta-hira",
	"da-hira",
	"ti-hira",
	"di-hira",
	"tu-hira",
	"tusmall-hira",
	"du-hira",
	"te-hira",
	"de-hira",
	"to-hira",
	"do-hira",
	"na-hira",
	"ni-hira",
	"nu-hira",
	"ne-hira",
	"no-hira",
	"ha-hira",
	"ba-hira",
	"pa-hira",
	"hi-hira",
	"bi-hira",
	"pi-hira",
	"hu-hira",
	"bu-hira",
	"pu-hira",
	"he-hira",
	"be-hira",
	"pe-hira",
	"ho-hira",
	"bo-hira",
	"po-hira",
	"ma-hira",
	"mi-hira",
	"mu-hira",
	"me-hira",
	"mo-hira",
	"ya-hira",
	"yasmall-hira",
	"yu-hira",
	"yusmall-hira",
	"yo-hira",
	"yosmall-hira",
	"ra-hira",
	"ri-hira",
	"ru-hira",
	"re-hira",
	"ro-hira",
	"wa-hira",
	"wasmall-hira",
	"wi-hira",
	"we-hira",
	"wo-hira",
	"n-hira",
	"vu-hira"
	]
tabText = ""
 
for n in selectedLayers:
	for i in breads:
		tabText += "/" + n.parent.name
		tabText += "/" + i
	tabText += "/" + n.parent.name + '\n\n'
 
font.newTab(tabText)
