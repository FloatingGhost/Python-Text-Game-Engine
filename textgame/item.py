#!/usr/bin/env python3

class Item:
    """Item class - items are within a scene
       Items have a description and an action"""
    def __init__(self,name="An item",short_desc="A short description",
                 desc="A longer description", can_pick_up=False):
        self.desc = desc
        self.short_desc = short_desc
        self.can_pick_up = can_pick_up
        self.name = name
        self.interactions = {self:(lambda: print("You can't use an item on itself!"))}

    def __repr__(self):
        return self.name + ": " + self.short_desc

    def setDesc(self, desc):
        """Set the description after the item has been created"""
        self.desc = desc

    def setShortDesc(self, desc):
        self.short_desc = desc

    def getDesc(self):
        """Get the item description"""
        return self.desc

    def getShortDesc(self):
        return self.short_desc

    def pickUp(self):
        return self.can_pick_up

    def getName(self):
        return self.name

    def addInteraction(self, other_item, interaction):
        if other_item in self.interactions:
          self.interactions[other_item] = interaction
        else:
          self.interactions.update({other_item:interaction})
    
    def useItem(self, other_item):
        if other_item in self.interactions:
          func = self.interactions[other_item]
          return func()
        else:
          print("There's nothing I can do there...")

    class Stat:
      def __init__(self, value):
        self.value = value

      def setValue(self, n):
        self.value = value

      def getValue(self):
        return self.value

      def increment(self):
        self.value += 1

      def decrement(self):
        self.value -= 1

      def add(self,n):
        self.value += n

      def sub(self,n):
        self.value -= n

      def scale(self,n):
        self.value *= n

