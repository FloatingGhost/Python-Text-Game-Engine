#!/usr/bin/env python3
from textgame.item import *

class Inventory:
    """The player's inventory"""
    def __init__(self, initial=[]):
        self.items = initial

    def has(self, item):
        """Returns whether we have the specified item"""
        return item in self.items

    def add_item(self, item):
        """Add an item to the inventory"""
        try:
            assert(type(item) == type(Item()))
            self.items.append(item)
        except AssertionError:
            print("That was not an item you tried to add to the inventory")

    def get_item_by_index(self, i):
        return self.items[i]
  
    def getItems(self):
        return self.items

    def get_item_by_name(self, name):
        for i in self.items:
            if i.getName() == name:
                return i
        return None
    def printInventory(self):
      if len(self.items) == 0:
        print("You're not holding anything")
      else:
        for i in self.items:
          print(str(i))
