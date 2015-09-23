#!/usr/bin/env python3

from textgame.scene import *
import sys
import os

try:
  debug = os.environ["debug"] == "on"
except:
  debug = False


if debug:
    print("Imported WorldMap")

class WorldMap:
    """World map
      for managing scenes within the game"""

    def __init__(self, width, height):
        self.scenes = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            self.scenes.append(row)
        self.SIZE_Y = height
        self.SIZE_X = width    
    def get(self,x,y):
        """Return the scene at x,y (or try to)"""
        if x < 0 or y < 0:
          return 0
        try:
            return self.scenes[y][x]
        except IndexError:
            #print("That scene is not part of the worldmap")
            return 0

    def can_move_to(self, x,y):
        if x < 0 or y < 0:
            return False
        if x > self.SIZE_X or y > self.SIZE_Y:
            return False
        #print("Getting {},{}".format(x,y))
        try:
            return self.scenes[y][x] != 0 
        except Exception as ex:
            #print(ex)
            return False

    def getCurrent(self):
        return self.scenes[self.player.x][self.player.y]

    def pickUp(self, item):
      if item in self.getCurrent().getItems():
        #self.world.player.addItem(item)
        self.getCurrent().removeItem(item)
      else:
        print("I can't see that!")


    def addScene(self, scene, x, y):
        """Add the specified scene"""
        try:
            assert(type(scene) == type(Scene()) or scene==0)
            self.scenes[x][y] = scene
        except AssertionError:
            print("The scene you tried to add was not actually a scene")
            sys.exit(1)
        except IndexError:
            print("You tried to add  a scene outside of the world bounds :(")
            sys.exit(1)


    def setMap(self, newmap):
        """Completely change the map to a new array of scenes"""
        try:
            #Test for valid map passing
            #There musr be at LEAST 1 scene
            testScene = newmap[0][0]
            for i in newmap:
                for j in i:
                    assert(type(j) == type(Scene()) or j==0)
            self.scenes = newmap
        except AssertionError as ass_er: #hehehhe
            print("There was a problem creating the map")
            print("Are you sure the array was populated with Scenes?")
            print("If you want the scene to be non-enterable, make it 0 (int)")
            sys.exit(1)

        except IndexError as in_er:
            print("There were no scenes in your array")
            print("(or you passed a 1-dimensional array)")
            sys.exit(1)
