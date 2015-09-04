#!/usr/bin/env python3
import os
print("Setting environment variables")
os.environ["debug"] = "on"
print("Testing imports...")
from textgame.world import *
from textgame.scene import *
print("Imports succesful.")

print("Creating world")
world = World()
print("Created world")

print("Creating initial worldmap")
wmap = WorldMap(2,2)
print("Created worldmap")

print("Creating test scenes")
baseScene = Scene("A test scene", "A longer test scene")
nextScene = Scene("One to the right of main", "Longer to the right")
rightDown = Scene("A third scene", "Right and down one")

print("Adding scenes to map by x y")
wmap.addScene(baseScene,0,0)
wmap.addScene(nextScene,0,1)
wmap.addScene(rightDown,1,1)
print("Added by XY")

print("Adding by array")
newmap = [
            [baseScene, nextScene],
            [0,rightDown]
        ]
wmap.setMap(newmap)
print("Added by array")

print("Passed tests.")
