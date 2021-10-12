from __future__ import unicode_literals

#MenuTitle: Hiragana-Sand
# -*- coding: utf-8 -*-
# Edit by Tanukizamurai

__doc__="""
選択中の文字を「カタカナ」で挟んだテキストのタブを作成します。
Create tab of selected characters sandwiched in Hiragana.
"""
 
import GlyphsApp

Glyphs.clearLog()

font = Glyphs.font
selectedLayers = font.selectedLayers

breads = [
	"a-kata",
	"asmall-kata",
	"i-kata",
	"ismall-kata",
	"u-kata",
	"usmall-kata",
	"e-kata",
	"esmall-kata",
	"o-kata",
	"osmall-kata",
	"ka-kata",
	"kasmall-kata",
	"ga-kata",
	"ki-kata",
	"gi-kata",
	"ku-kata",
	"gu-kata",
	"ke-kata",
	"kesmall-kata",
	"ge-kata",
	"ko-kata",
	"go-kata",
	"sa-kata",
	"za-kata",
	"si-kata",
	"zi-kata",
	"su-kata",
	"zu-kata",
	"se-kata",
	"ze-kata",
	"so-kata",
	"zo-kata",
	"ta-kata",
	"da-kata",
	"ti-kata",
	"di-kata",
	"tu-kata",
	"tusmall-kata",
	"du-kata",
	"te-kata",
	"de-kata",
	"to-kata",
	"do-kata",
	"na-kata",
	"ni-kata",
	"nu-kata",
	"ne-kata",
	"no-kata",
	"ha-kata",
	"ba-kata",
	"pa-kata",
	"hi-kata",
	"bi-kata",
	"pi-kata",
	"hu-kata",
	"bu-kata",
	"pu-kata",
	"he-kata",
	"be-kata",
	"pe-kata",
	"ho-kata",
	"bo-kata",
	"po-kata",
	"ma-kata",
	"mi-kata",
	"mu-kata",
	"me-kata",
	"mo-kata",
	"ya-kata",
	"yasmall-kata",
	"yu-kata",
	"yusmall-kata",
	"yo-kata",
	"yosmall-kata",
	"ra-kata",
	"ri-kata",
	"ru-kata",
	"re-kata",
	"ro-kata",
	"wa-kata",
	"wasmall-kata",
	"va-kata",
	"wi-kata",
	"vi-kata",
	"we-kata",
	"ve-kata",
	"wo-kata",
	"vo-kata",
	"n-kata",
	"vu-kata"
	]
tabText = ""
 
for n in selectedLayers:
	for i in breads:
		tabText += "/" + n.parent.name
		tabText += "/" + i
	tabText += "/" + n.parent.name + '\n\n'
 
font.newTab(tabText)
