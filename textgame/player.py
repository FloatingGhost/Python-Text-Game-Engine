#!/usr/bin/env python3
from textgame.inventory import *
from textgame.item import *
class Player:
    def __init__(self, name, x, y, inventory=[]):
        self.name = name
        self.x = x
        self.y = y
        self.inventory = inventory
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move_north(self):
        self.y -= 1

    def move_south(self):
        self.y += 1

    def move_west(self):
        self.x -= 1

    def move_east(self):
        self.x += 1

    def add_item(self, item):
        try:
            assert(type(item) == type(Item()))
            self.inventory.add_item(item)
        except AssertionError:
            print("Passed an invalid item to Player")
    def remove_item(self, item):
        try:
            assert(inventory.has(item))
            inventory.remove_item(item)
        except AssertionError:
            print("That item isn't in the inventory")


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
