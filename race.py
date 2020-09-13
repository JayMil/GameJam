from enum import Enum
from pyglet.window import key

from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction

class Race(PhysicalSpriteObject):
    def __init__(self, health, race_images, speed=2, *args, **kwargs):
        super().__init__(img=race_images.face_down, 
                        interaction=Interaction.BLOCKING, 
                        *args, **kwargs)

        self.race_images = race_images
        
        self.health = health

        self.moving = Stack()

        self.speed = speed
        self.current_speed = speed

        self.inventory = []
        self.displayed_items  = []

    def update(self, dt):
        speed = self.current_speed

        if self.moving:
            if self.moving.peek() == Facing.UP:
                if self.image != self.race_images.walk_up:
                    self.image = self.race_images.walk_up
                self.hit_box.y += speed
            elif self.moving.peek() == Facing.DOWN:
                if self.image != self.race_images.walk_down:
                    self.image = self.race_images.walk_down
                self.hit_box.y -= speed
            elif self.moving.peek() == Facing.LEFT:
                if self.image != self.race_images.walk_left:
                    self.image = self.race_images.walk_left
                self.hit_box.x -= speed
            elif self.moving.peek() == Facing.RIGHT:
                if self.image != self.race_images.walk_right:
                    self.image = self.race_images.walk_right
                self.hit_box.x += speed
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


    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.push(Facing.UP)

        if symbol == key.DOWN:
            self.moving.push(Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.push(Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.push(Facing.RIGHT)


    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.pop(Facing.UP)

        if symbol == key.DOWN:
            self.moving.pop(Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.pop(Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.pop(Facing.RIGHT)
            

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

