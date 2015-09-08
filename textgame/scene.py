#!/usr/bin/env python3

from textgame import item

class Scene:
    def __init__(self, scene_description="Basic Desc", longer="Longer Desc",
                 items=[]):
        self.items = items
        self.scene_description = scene_description
        self.longer_desc = longer 
        
    def __repr__(self):
        rep = "You are standing in "+self.scene_description+"\n"
        rep += "\n"+self.longer_desc
        rep += "\nYou can see:"
        if len(self.items) == 0:
            rep += "\nNothing of note"
        else:
            for i in self.items:
                rep += "\n{}".format(str(i))
        return rep

    def setDesc(self,desc):
        self.scene_description = desc

    def getDesc(self,desc):
        return self.scene_description

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)
