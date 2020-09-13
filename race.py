from enum import Enum
from pyglet.window import key

from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction

class Race(PhysicalSpriteObject):
    def __init__(self, health, race_images, *args, **kwargs):
        super().__init__(img=race_images.face_down, interaction=Interaction.BLOCKING, *args, **kwargs)

        self.race_images = race_images
        
        self.health = health

        self.moving = Stack()

        self.speed = 2
        self.fast = False

        self.inventory = []
        self.displayed_items  = []

    def update(self, dt):
        if self.moving:
            if self.moving.peek() == Facing.UP:
                if self.image != self.race_images.walk_up:
                    self.image = self.race_images.walk_up
                self.hit_box.y += self.speed
            elif self.moving.peek() == Facing.DOWN:
                if self.image != self.race_images.walk_down:
                    self.image = self.race_images.walk_down
                self.hit_box.y -= self.speed
            elif self.moving.peek() == Facing.LEFT:
                if self.image != self.race_images.walk_left:
                    self.image = self.race_images.walk_left
                self.hit_box.x -= self.speed
            elif self.moving.peek() == Facing.RIGHT:
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

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.push(Facing.UP)

        if symbol == key.DOWN:
            self.moving.push(Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.push(Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.push(Facing.RIGHT)

        if symbol == key.F:
            self.fast = True


    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.pop(Facing.UP)

        if symbol == key.DOWN:
            self.moving.pop(Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.pop(Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.pop(Facing.RIGHT)
            
        if symbol == key.F:
            self.fast = False

class Stack():
    def __init__(self):
        self.list = []

    def __bool__(self):
        return len(self.list) > 0

    def push(self, item):
        self.list.append(item)

    def pop(self, item=None):
        if(item):
            self.list.remove(item)
        else:
            return self.list.pop()


    def peek(self):
        return self.list[len(self.list)-1]




class Facing(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

