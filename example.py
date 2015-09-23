#!/usr/bin/env python3

from textgame.world import *
from textgame.scene import *
from textgame.item  import *
from textgame.utils import *
from textgame.input import *

world = World()

SIZE_X = 2
SIZE_Y = 2

worldMap = WorldMap(SIZE_X, SIZE_Y)

scene_1_items = [
                  Item("Mobile Phone", "Your trusty handheld telecom device",
                        can_pick_up=True),
                  Item("Lamp", "A bedside lamp", False)
                ]

def fn():
  print( "It's low on battery :(")

scene_1_items[0].setOnLook(fn)

scene_1 = Scene("Your Bedroom", "The place where you go to sleep every night",
                scene_1_items)

scene_2_items = [
                  Item("Phone charger", "A way to charge up electrical devices")
                ]

def chargePhone():
  print("You put your phone on to charge.")
  
scene_1_items[0].addInteraction(scene_2_items[0], chargePhone)

scene_2 = Scene("Your living room", "The room that you spend most of your time in",
                scene_2_items)
scenes = [
          [scene_1, scene_2],
          [0,0]
         ]

worldMap.setMap(scenes)

world.addWorldMap(worldMap)

i = Input(world)

i.mainloop()
