#Python Text Based Game Engine

So somehow you've stumbled upon this little engine and want to know
how to use it.

Very well then.

##Creating a Game

First import the needed classes

```python
from textgame.world import *
from textgame.scene import *
from textgame.item  import *
from textgame.utils import *
from textgame.input import *
```

And make sure that works, if not, modify your PYTHONPATH to include 
your working directory.

Create a game

```python
world = World()
```

It's that simple!

next comes actually adding content to your game.

##Adding a world map

```python
#Declare the size of the world map
SIZE_X = 3
SIZE_Y = 4

#Create our world map
worldMap = WorldMap(SIZE_X, SIZE_Y)
```

And now, to add scenes to the map

##Creating Scenes

All of the game will take place within an array of scenes, luckily these are quite
simple to create.

```python

#Give the player something to read
short_scene_description = "Hello this is a scene"
long_scene_description = "This is a slightly more detailed description of the scene"

#Put items in the scene (See 'Creating Items')
scene_items = [item1, item2, item3, etc, et, cetera]

#Create the scene object
myScene = Scene(short_scene_description, long_scene_description, scene_items)
```

##Add scenes to the worldmap

Now you have your world map and your scenes, it's time to combine them!

```python
#Where the scene will be located on the map
scene_X = 0
scene_Y = 0

#Add the scene
worldMap.addScene(myScene, scene_X, scene_Y)
```

###Alternative method

If all that creating scenes is a wee bit repetative for you, you can add them as 
part of an array;

```python
#Create the array - 0 means "cannot visit here"
scenes = [
            [scene1, scene2],
            [0,      scene3]
         ]

world.addWorldMap(scenes)
```

##Creating Items - InDev!!!

Now to put things in the scene.

```python
#Create the item
myItem = Item("ItemName", "ItemDescription", "LongerDescription", True)
##The last argument is "can pick up" - i.e can you put it in your inventory?

#Add it to the scene

scene.addItem(myItem)

#You can pick it up later with world.pickUp(myItem)
```


##Input engine

The user has to be able to control the player!
I've provided textgame.input to help with that!

Just create it and run it, i.e

```python
#Create the input engine
input = Input()

#Start the game
input.mainloop()
```
 
