#!/usr/bin/env python3
import os
import sys
from textgame.worldmap import *
from textgame.player import *


debug= os.environ["debug"] == "on"

if debug:
    print("Imported world")

class World:
    def __init__(self,playername="Player",start_x=0, start_y=0):
        self.worldmap = WorldMap(3,3)
        self.player = Player(playername, start_x, start_y)
    def addWorldMap(self, worldmap):
        try:
            assert(type(worldmap) == type(WorldMap(3,3)))
            self.worldmap = worldmap
        except AssertionError as ass_err:
            print("You passed a malformed WorldMap to World")
            sys.exit(1)
