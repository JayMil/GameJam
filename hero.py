from enum import Enum
import pyglet
from pyglet.window import key

import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from race import Race, Facing


class Hero(Race):
    ''' Hero Sprite Class '''
    def __init__(self, update_inventory, x=20, y=200, health=5, *args, **kwargs):
        super().__init__(race_images=resources.HeroImages(), x=x, y=y, health=health, *args, **kwargs)

        self.update_inventory = update_inventory

        # adjust hit box height
        #print(self.height)
        #self.hit_box.height -= 55

    def update_stats(self, value, stat_type):
        pass

        
    def update(self, dt):
        super().update(dt)

    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        if symbol == key.SPACE:
            if self.facing == Facing.RIGHT:
                if self.image != self.race_images.attack_right:
                    self.image = self.race_images.attack_right
            elif self.facing == Facing.LEFT:
                if self.image != self.race_images.attack_left:
                    self.image = self.race_images.attack_left
            elif self.facing == Facing.UP:
                if self.image != self.race_images.attack_up:
                    self.image = self.race_images.attack_up
            elif self.facing == Facing.DOWN:
                if self.image != self.race_images.attack_down:
                    self.image = self.race_images.attack_down


