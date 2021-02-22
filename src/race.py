from enum import Enum
import threading
import time
from pyglet.window import key

from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from collisionobject import CollisionObject

from inventory import InventoryType


class Race(PhysicalSpriteObject):
    def __init__(self, health, race_images, speed=2, *args, **kwargs):
        super().__init__(
            img=race_images.face_down, interaction=Interaction.BLOCKING, *args, **kwargs
        )

        self.race_images = race_images

        self.health = health
        self.taking_damage = False

        self.moving = Stack()
        self.facing = Facing.DOWN

        self.speed = speed
        self.current_speed = speed

        self.inventory = {}

        self.hit_boxes["feet"] = CollisionObject(
            self.x,
            self.y,
            self.width,
            self.height,
            self.hit_boxes["sprite"].interaction,
        )
        self.hit_boxes["body"] = CollisionObject(
            self.x,
            self.y,
            self.width,
            self.height,
            self.hit_boxes["sprite"].interaction,
        )

    def update(self, dt):
        speed = self.current_speed

        ydiff = 0
        xdiff = 0

        if not self.taking_damage:
            if self.moving:
                self.facing = self.moving.peek()
                if self.moving.peek() == Facing.UP:
                    if self.image != self.race_images.walk_up:
                        self.image = self.race_images.walk_up
                    ydiff += speed
                elif self.moving.peek() == Facing.DOWN:
                    if self.image != self.race_images.walk_down:
                        self.image = self.race_images.walk_down
                    ydiff -= speed
                elif self.moving.peek() == Facing.LEFT:
                    if self.image != self.race_images.walk_left:
                        self.image = self.race_images.walk_left
                    xdiff -= speed
                elif self.moving.peek() == Facing.RIGHT:
                    if self.image != self.race_images.walk_right:
                        self.image = self.race_images.walk_right
                    xdiff += speed
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

            self.update_pos(xdiff, ydiff)

    def update_pos(self, xdiff, ydiff):
        # prevent going out of border
        min_x = 0
        min_y = 0
        max_x = self.window.width
        max_y = self.window.height

        if (self.hit_boxes["feet"].x + xdiff) < min_x:
            xdiff = self.hit_boxes["feet"].x - min_x
        elif (self.hit_boxes["feet"].x + self.hit_boxes["feet"].width + xdiff) > max_x:
            xdiff = self.hit_boxes["feet"].x - (max_x - self.hit_boxes["feet"].width)
        if (self.hit_boxes["feet"].y + ydiff) < min_y:
            ydiff = self.hit_boxes["feet"].y - min_y
        elif (self.hit_boxes["feet"].y + self.hit_boxes["feet"].height + ydiff) > max_y:
            ydiff = self.hit_boxes["feet"].y - (max_y - self.hit_boxes["feet"].height)

        for key in self.hit_boxes:
            self.hit_boxes[key].x += xdiff
            self.hit_boxes[key].y += ydiff

        self.x += xdiff
        self.y += ydiff

    def stop_movement_animation(self):
        if self.image == self.race_images.walk_up:
            self.image = self.race_images.face_up
        elif self.image == self.race_images.walk_down:
            self.image = self.race_images.face_down
        elif self.image == self.race_images.walk_left:
            self.image = self.race_images.face_left
        elif self.image == self.race_images.walk_right:
            self.image = self.race_images.face_right

    def damage(self):
        if not self.taking_damage:
            self.taking_damage = True
            print("Taking damage")
            self.stop_movement_animation()
            if self.facing == Facing.UP:
                self.image = self.race_images.damage_up
            elif self.facing == Facing.DOWN:
                self.image = self.race_images.damage_down
            elif self.facing == Facing.LEFT:
                self.image = self.race_images.damage_left
            elif self.facing == Facing.RIGHT:
                self.image = self.race_images.damage_right

            if self.health > 0:
                self.update_stats(-1, InventoryType.HEALTH)

            threading.Thread(target=self.__damageTimeout).start()

    def __damageTimeout(self):
        time.sleep(self.race_images.damage_right.get_duration())
        self.taking_damage = False

    def on_key_press(self, symbol, modifiers):
        if not self.taking_damage:
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

        if symbol == key.P:
            if "health_potion" in self.inventory:
                if self.inventory["health_potion"] > 0:
                    self.update_stats(-1, InventoryType.HEALING_POTIONS)
                    self.update_stats(1, InventoryType.HEALTH)

        if symbol == key.T:
            if self.health > 1:
                self.update_stats(-1, InventoryType.HEALTH)

        if self.moving:
            self.facing = self.moving.peek()


class Stack:
    def __init__(self):
        self.list = []

    def __bool__(self):
        return len(self.list) > 0

    def push(self, item):
        self.list.append(item)

    def pop(self, item=None):
        if item:
            if item in self.list:
                self.list.remove(item)
        else:
            return self.list.pop()

    def peek(self):
        return self.list[len(self.list) - 1]


class Facing(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
