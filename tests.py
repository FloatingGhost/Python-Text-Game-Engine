#!/usr/bin/env python3
import os
print("--Setting environment variables\n")
os.environ["debug"] = "on"
print("--Testing imports...\n")
from textgame.world import *
from textgame.scene import *
from textgame.item  import *
print("\n--Imports succesful.\n")

print("--Creating world\n")
world = World()
print("--Created world\n")

print("--Creating initial worldmap\n")
wmap = WorldMap(2,2)
print("--Created worldmap\n")

print("--Creating test scenes\n")
baseScene = Scene("A test scene", "A longer test scene\n")
nextScene = Scene("One to the right of main", "Longer to the right\n")
rightDown = Scene("A third scene", "Right and down one\n", [
                                    Item("Excalibur", "Massive Sword",
                                         "Seriously who designed this", True)])

print("--Adding scenes to map by x y\n")
wmap.addScene(baseScene,0,0)
wmap.addScene(nextScene,0,1)
wmap.addScene(rightDown,1,1)
print("--Added by XY\n")
print("--Adding by array\n")
newmap = [
            [baseScene, nextScene],
            [0,rightDown]
        ]
wmap.setMap(newmap)
print("--Added by array\n")

world.addWorldMap(wmap)

print("--Testing scene config\n")


scene_expect = """You are standing in A test scene

A longer test scene

You can See:
Nothing of note"""

assert(str(world.get_current()).lower() == scene_expect.lower())


scene_2_expect = """You are standing in One to the right of main

Longer to the right

You can See:
Nothing of note"""
#We should only be able to move East from here
try:
    world.move_north()
    world.move_west()
    world.move_south()
    sys.exit(1)
except:
    pass
world.move_east()
assert(str(world.get_current()).lower() == scene_2_expect.lower()) 
print("\n\n--Passed tests.\n")
