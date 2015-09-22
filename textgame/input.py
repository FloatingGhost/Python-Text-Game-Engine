#!/usr/bin/env python3

import sys


class Input:
  def __init__(self, world, promptText=">"):
    self.world = world
    self.promptText = promptText

    ##Define command words
    self.quitwords = ["q", "quit", "exit", "bye"]
    self.movewords = ["go", "move", "walk"]
    self.lookwords = ["look", "view", "read"]
    self.takewords = ["take", "grab", "get"]
   
  def item_match(self, item_array):
    scene_items = self.world.get_current().getItems()
    for i in item_array:
      for j in scene_items:
        if i.lower() in str(j).lower():
          return j
    return 0

  def mainloop(self):
    self.world.print_scene_description()
    last_input = ""
    while last_input not in self.quitwords:
      last_input = input(self.promptText + " ").strip()
      #Process the input
      command = last_input.lower().split(" ")
      cmd = command[0]
      if cmd in self.quitwords:
        print("Bye!")
        sys.exit(0)  
      elif cmd in self.movewords:
        #Move
        pass
      elif cmd in self.lookwords:
        #Look around/at an item
        if len(command) == 1:
          self.world.print_scene_description()
        else:
          print(str(self.item_match(command[1:])))
      elif cmd in self.takewords: 
        #Take an item
        pass
      else:
        print("I don't know how to do that.")
