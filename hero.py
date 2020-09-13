from enum import Enum
import pyglet
from pyglet.window import key

import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from race import Race, Facing


HERO_IMAGES = resources.HeroImages()

class Hero(Race):
    ''' Hero Sprite Class '''
    def __init__(self, x=20, y=200, health=5, *args, **kwargs):
        super().__init__(img=HERO_IMAGES.face_down, x=x, y=y, health=health, *args, **kwargs)

        self.moving = []

        # adjust hit box height
        #print(self.height)
        #self.hit_box.height -= 55
        
    def update(self, dt):
        super().update(dt)

        if self.moving:
            if self.moving[0] == Facing.UP:
                if self.image != HERO_IMAGES.walk_up:
                    self.image = HERO_IMAGES.walk_up
                self.hit_box.y += self.speed
            elif self.moving[0] == Facing.DOWN:
                if self.image != HERO_IMAGES.walk_down:
                    self.image = HERO_IMAGES.walk_down
                self.hit_box.y -= self.speed
            elif self.moving[0] == Facing.LEFT:
                if self.image != HERO_IMAGES.walk_left:
                    self.image = HERO_IMAGES.walk_left
                self.hit_box.x -= self.speed
            elif self.moving[0] == Facing.RIGHT:
                if self.image != HERO_IMAGES.walk_right:
                    self.image = HERO_IMAGES.walk_right
                self.hit_box.x += self.speed
        else:
            # if not moving, set to still image
            if self.image == HERO_IMAGES.walk_up:
                self.image = HERO_IMAGES.face_up
            elif self.image == HERO_IMAGES.walk_down:
                self.image = HERO_IMAGES.face_down
            elif self.image == HERO_IMAGES.walk_left:
                self.image = HERO_IMAGES.face_left
            elif self.image == HERO_IMAGES.walk_right:
                self.image = HERO_IMAGES.face_right


    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.insert(0, Facing.UP)

        if symbol == key.DOWN:
            self.moving.insert(0, Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.insert(0, Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.insert(0, Facing.RIGHT)

        if symbol == key.F:
            self.fast = True


    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.remove(Facing.UP)

        if symbol == key.DOWN:
            self.moving.remove(Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.remove(Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.remove(Facing.RIGHT)
            
        if symbol == key.F:
            self.fast = False

