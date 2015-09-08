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

    def get_current(self):
        return self.worldmap.get(self.player.getX(),
                                 self.player.getY())

    def print_scene_description(self):
        """Tell the user where they are"""
        print(str(self.worldmap.get(self.player.getX(),
                                    self.player.getY())))

    def move_north(self):
        if self.player.getY() - 1 >= 0 and \
            self.worldmap.get(self.player.getX(), self.player.getY()-1) != 0:
                self.player.move_north()
        else:
            print("There isn't anything that way!")
    
    def move_south(self):
        if self.player.getY() + 1 < self.worldmap.SIZE_Y and \
            self.worldmap.get(self.player.getX(), self.player.getY() +1) != 0:
                self.player.move_south()
        else:
            print("There isn't anything that way!")

    def move_east(self):
        if self.player.getX() + 1 < self.worldmap.SIZE_X and \
            self.worldmap.get(self.player.getX() + 1, self.player.getY()) != 0:
                self.player.move_south()
        else:
            print("There isn't anything that way!")

    def move_west(self):
        if self.player.getX() - 1 >= 0 and \
            self.worldmap.get(self.player.getX()-1, self.player.getY()) != 0:
                self.player.move_south()
        else:
            print("There isn't anything that way!")
 
