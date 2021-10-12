#MenuTitle:	Apply Segment Components 
# -*- coding: utf-8 -*-
__doc__="""
Apply Segment Components.
"""

node = Layer.selection[0]
newSeg = GSHint()
newSeg.type = 19 #SEGMENT
newSeg.originNode = node
newSeg.name = "_segment.brush"
Layer.hints.append(newSeg)