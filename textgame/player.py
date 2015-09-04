#!/usr/bin/env python3
from textgame.inventory import *
from textgame.item import *
class Player:
    def __init__(self, name, x, y, inventory=[]):
        self.name = name
        self.x = x
        self.y = y
        self.inventory = inventory
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


