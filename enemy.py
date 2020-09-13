from enum import Enum
import pyglet

import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from race import Race, Facing


class Enemy(Race):
    ''' Enemy Sprite Class '''
    def __init__(self, x=20, y=200, health=5, target=None, *args, **kwargs):
        super().__init__(race_images=resources.EnemyImages(), x=x, y=y, health=health, *args, **kwargs)

        self.target = target

        self.pattern = [Facing.LEFT, Facing.LEFT, Facing.LEFT, Facing.RIGHT, Facing.RIGHT, Facing.RIGHT]

        self.pattern_pos = 0

        # adjust hit box height
        #print(self.height)
        #self.hit_box.height -= 55
        
    def update(self, dt):

        '''
        if(self.target):
            super().update(dt)
        else:
        '''
        #self.moving.push(self.pattern[self.pattern_pos%len(self.pattern)])
        self.moving.push(Facing.LEFT)
        self.pattern_pos += 1
        super().update(dt)
        self.moving.pop()
        





