#!/usr/bin/env python3
import os
print("--Setting environment variables\n")
os.environ["debug"] = "on"
print("--Testing imports...\n")
from textgame.world import *
from textgame.scene import *
from textgame.item  import *
from textgame.utils import *

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
print("--Testing intro scene\n")
assert(str(world.get_current()).lower() == scene_expect.lower())


scene_2_expect = """You are standing in One to the right of main

Longer to the right

You can See:
Nothing of note"""
print("--Moving East")
#We should only be able to move East from here
try:
    world.move_north()
    print("** Could move north! Exiting!")
    sys.exit(1)
except SystemExit:
    sys.exit(1)
except MovementError: 
    print(":) Could not move North")

try:
    world.move_west()
    print("** Could move west! Exiting!")
    sys.exit(1)
except SystemExit:
    sys.exit(1)
except MovementError:
    print(":) Could not move West")

try:
    world.move_south()
    print("** Could move south! Exiting!")
    sys.exit(1)
except SystemExit:
    sys.exit(1)
except MovementError:
    print(":) Could not move South")

world.move_east()


assert(str(world.get_current()).lower() == scene_2_expect.lower()) 

print("--Moving South")
#Should now only be able to go south/west
try:
    world.move_north()
except SystemExit:
    sys.exit(1)
except MovementError:
    print(":) Could not move North")
    
try:
    world.move_east()
    sys.exit(1)
except SystemExit:
    sys.exit(1)
except MovementError:
    print(":) Could not move East")

world.move_south()

scene_3_expect = """You are standing in a third scene

Right and down one

You can see:
Excalibur: Massive sword"""

assert(str(world.get_current()).lower() == scene_3_expect.lower())

print("--Testing player statistics")

def mod_player_function(p):
  p.hp = p.Stat(10)

world.modifyPlayer(mod_player_function)

p = world.getPlayer()

assert(p.hp.value == 10)
print("--That hacky method worked!")

print("--Testing Item Interaction")

i = Item("Test", "Testing", "Testing Testing", True)

i.useItem(i)

assert("y" == input("\nDoes the last line read \"You can't use an item on itself!\"?(y/n)".lower()))

j = Item("Test1", "memes", "double memes", True)

def item_interact():
  return "WERKZ!"

j.addInteraction(i, item_interact)
assert("WERKZ!" == j.useItem(i))
assert("WERKZ!" == i.useItem(j))
print("\n--Item usage works")

print("\n\n--Passed tests.\n")
