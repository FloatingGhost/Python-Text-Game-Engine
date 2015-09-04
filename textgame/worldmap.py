#!/usr/bin/env python3

from textgame.scene import *
import sys
import os

debug = os.environ["debug"] == "on"

if debug:
    print("Imported WorldMap")

class WorldMap:
    def __init__(self, width, height):
        self.scenes = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            self.scenes.append(row)
    def get(self,x,y):
        try:
            return self.scenes[y][x]
        except IndexError:
            print("That scene is not part of the worldmap")

    def addScene(self, scene, x, y):
        try:
            assert(type(scene) == type(Scene()) or scene==0)
            self.scenes[y][x] = scene
        except AssertionError:
            print("The scene you tried to add was not actually a scene")
            sys.exit(1)
        except IndexError:
            print("You tried to add  a scene outside of the world bounds :(")
            sys.exit(1)


    def setMap(self, newmap):
        try:
            #Test for valid map passing
            #There musr be at LEAST 1 scene
            testScene = newmap[0][0]
            for i in newmap:
                for j in i:
                    assert(type(j) == type(Scene()) or j==0)
        except AssertionError as ass_er: #hehehhe
            print("There was a problem creating the map")
            print("Are you sure the array was populated with Scenes?")
            print("If you want the scene to be non-enterable, make it 0 (int)")
            sys.exit(1)

        except IndexError as in_er:
            print("There were no scenes in your array")
            print("(or you passed a 1-dimensional array)")
            sys.exit(1)
