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
