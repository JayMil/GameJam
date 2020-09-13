from enum import Enum
from pyglet.window import key

from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction

class Race(PhysicalSpriteObject):
    def __init__(self, health, race_images, *args, **kwargs):
        super().__init__(img=race_images.face_down, interaction=Interaction.BLOCKING, *args, **kwargs)

        self.race_images = race_images
        
        self.health = health

        self.facing = Facing.DOWN
        self.moving = []

        self.speed = 2
        self.fast = False

        self.inventory = []
        self.displayed_items  = []

    def update(self, dt):
        if self.fast:
            self.speed = 4
        else:
            self.speed = 2

        if self.moving:
            if self.moving[0] == Facing.UP:
                if self.image != self.race_images.walk_up:
                    self.image = self.race_images.walk_up
                self.hit_box.y += self.speed
            elif self.moving[0] == Facing.DOWN:
                if self.image != self.race_images.walk_down:
                    self.image = self.race_images.walk_down
                self.hit_box.y -= self.speed
            elif self.moving[0] == Facing.LEFT:
                if self.image != self.race_images.walk_left:
                    self.image = self.race_images.walk_left
                self.hit_box.x -= self.speed
            elif self.moving[0] == Facing.RIGHT:
                if self.image != self.race_images.walk_right:
                    self.image = self.race_images.walk_right
                self.hit_box.x += self.speed
        else:
            # if not moving, set to still image
            if self.image == self.race_images.walk_up:
                self.image = self.race_images.face_up
            elif self.image == self.race_images.walk_down:
                self.image = self.race_images.face_down
            elif self.image == self.race_images.walk_left:
                self.image = self.race_images.face_left
            elif self.image == self.race_images.walk_right:
                self.image = self.race_images.face_right

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

        for item in self.displayed_items:
            item.update(dt, self.moving, self.facing, xdiff, ydiff)



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


class Facing(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

