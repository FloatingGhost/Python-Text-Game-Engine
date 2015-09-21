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
    

  def mainloop(self):
    last_input = ""
    while last_input not in self.quitwords:
      last_input = input(self.promptText + " ").strip()
      #Process the input
      command = last_input.split(" ").lower()
      cmd = command[0]
      if cmd in self.quitwords:
        print("Bye!")
        sys.exit(0)  
      elif cmd in self.movewords:
        #Move
        pass
      elif cmd in self.lookwords:
        #Look around/at an item
        pass
      elif cmd in takewords: 
        #Take an item
        pass
      else:
        print("I don't know how to do that.")
