from enum import Enum

from physicalspriteobject import PhysicalSpriteObject

class Race(PhysicalSpriteObject):
    def __init__(self, health, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
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


class Facing(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

