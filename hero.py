from enum import Enum
import pyglet

import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from race import Race, Facing


class Hero(Race):
    ''' Hero Sprite Class '''
    def __init__(self, x=20, y=200, health=5, *args, **kwargs):
        super().__init__(race_images=resources.HeroImages(), x=x, y=y, health=health, *args, **kwargs)




        # adjust hit box height
        #print(self.height)
        #self.hit_box.height -= 55
        
    def update(self, dt):
        super().update(dt)

        if self.fast:
            self.speed = 4
        else:
            self.speed = 2

        # prevent going out of border
        min_x = 0
        min_y = 0
        max_x = self.window.width
        max_y = self.window.height

        if self.hit_box.x < min_x:
            self.hit_box.x = min_x
        elif (self.hit_box.x+self.hit_box.width) > max_x:
            self.hit_box.x = (max_x - self.hit_box.width)
        if self.hit_box.y < min_y:
            self.hit_box.y = min_y
        elif (self.hit_box.y+self.hit_box.height) > max_y:
            self.hit_box.y = (max_y - self.hit_box.height)

        xdiff = self.x - self.hit_box.x
        ydiff = self.y - self.hit_box.y
        self.x = self.hit_box.x
        self.y = self.hit_box.y

