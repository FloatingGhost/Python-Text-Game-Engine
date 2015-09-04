#!/usr/bin/env python3

from textgame import item

class Scene:
    def __init__(self, scene_description="Basic Desc", items=[]):
        self.items = items
        self.scene_description = scene_description

    def __repr__(self):
        rep = scene_description
        if len(self.items) > 0:
            rep += "\nYou can see:"
        for i in self.items:
            rep += "\n{}".format(str(i))

    def setDesc(self,desc):
        self.scene_description = desc

    def getDesc(self,desc):
        return self.scene_description

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)
