#!/usr/bin/env python3
import os
import sys
from textgame.worldmap import *
from textgame.player import *


debug= os.environ["debug"] == "on"

if debug:
    print("Imported world")

class World:
    """Highest class - for managing the game"""

    def __init__(self,playername="Player",start_x=0, start_y=0):
        self.worldmap = WorldMap(3,3)
        self.player = Player(playername, start_x, start_y)

    def addWorldMap(self, worldmap):
        """Set the world in which to play"""
        try:
            assert(type(worldmap) == type(WorldMap(3,3)))
            self.worldmap = worldmap
        except AssertionError as ass_err:
            print("You passed a malformed WorldMap to World")
            sys.exit(1)

    def print_scene_description(self):
        """Tell the user where they are"""
        print(str(self.worldmap.get(x,y)))
