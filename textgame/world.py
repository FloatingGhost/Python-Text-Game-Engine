#!/usr/bin/env python3
import os
import sys
from textgame.worldmap import *
from textgame.player import *
from textgame.utils import *


try:
    debug= os.environ["debug"] == "on"
except:
    debug = False

if debug:
    print("Imported world")

class World:
    """Highest class - for managing the game"""

    def __init__(self,playername="Player",start_x=0, start_y=0):
        self.worldmap = WorldMap(3,3)
        self.player = Player(playername, start_x, start_y)
    
    def getPlayer(self):
        return self.player

    def setPlayer(self, n):
        try:
          assert(type(n) == type(Player("", 0, 0)))
          self.player = n
        except AssertionError:
          print("That isn't a valid player")
          sys.exit(1)

    def modifyPlayer(self, function):
        function(self.player)

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
        x = self.player.getX()
        y = self.player.getY()
        nth = self.worldmap.get(x, y - 1)
        if nth != 0:
          print("\nTo the north: {}".format(nth.getDesc()))

        est = self.worldmap.get(x + 1, y)
        if est != 0:                         
          print("\nTo the east: {}".format(est.getDesc()))

        sth = self.worldmap.get(x, y + 1)
        if sth != 0:                         
          print("\nTo the south: {}".format(sth.getDesc()))

        wst = self.worldmap.get(x - 1, y)
        if wst != 0:                         
          print("\nTo the west: {}".format(wst.getDesc()))
          
            
    def move_north(self):
        if self.worldmap.can_move_to(self.player.getX(),
                                     self.player.getY()-1):
            self.player.move_north() 
        else:
            #print("There isn't anything that way!")
            raise MovementError("Can't go there! (Northbound)")
 
    def move_south(self):
        if self.worldmap.can_move_to(self.player.getX(),
                                     self.player.getY()+1):
                self.player.move_south()
        else:
            #print("There isn't anything that way!")
            raise MovementError("Can't go there! (Southbound)")

    def move_east(self):
        if self.worldmap.can_move_to(self.player.getX()+1,
                                     self.player.getY()):
                self.player.move_east()
            
        else:
            #print("There isn't anything that way!")
            raise MovementError("Can't go there! (Eastbound)")
    
    def move_west(self):
        if self.worldmap.can_move_to(self.player.getX()-1,
                                     self.player.getY()):
                self.player.move_west()
        else:
            #print("There isn't anything that way!")
            raise MovementError("Can't go there! (Westbound)")

    def printInventory(self):
      self.player.printInventory()

    def getInventory(self):
      return self.player.getInventory()

    def pickUp(self, item):
      if item in self.worldmap.get(self.player.getX(), self.player.getY()).getItems():
        self.player.addItem(item)
        self.worldmap.get(self.player.getX(), self.player.getY()).removeItem(item)
      else:
        print("I can't see that!")
