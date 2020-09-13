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


