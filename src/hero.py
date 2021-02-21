from enum import Enum
import pyglet
from pyglet.window import key

import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from race import Race, Facing

from inventory import InventoryType


class Hero(Race):
    """ Hero Sprite Class """

    def __init__(self, update_inventory, x=20, y=200, health=5, *args, **kwargs):
        super().__init__(
            race_images=resources.HeroImages(), x=x, y=y, health=health, *args, **kwargs
        )

        self.update_inventory = update_inventory
        self.inventory.update({"health_potion": 0})

        # make feet hit_box smaller so that the player can move around easier.
        self.hit_boxes["feet"].x += 42
        self.hit_boxes["feet"].y += 32
        self.hit_boxes["feet"].height = 5
        self.hit_boxes["feet"].width = 15

    def update_stats(self, value, stat_type):
        if stat_type == InventoryType.HEALTH:
            if value + self.health > 5:
                self.health = 5
            elif value + self.health < 0:
                self.health = 0
            else:
                self.health += value

            self.update_inventory(self.health, stat_type)
        elif stat_type == InventoryType.HEALING_POTIONS:

            if self.inventory["health_potion"] + value < 0:
                self.inventory["health_potion"] = 0
            else:
                self.inventory["health_potion"] += value

            new_potion_count = self.inventory["health_potion"]
            self.update_inventory(new_potion_count, stat_type)

    def update(self, dt):
        super().update(dt)

    def update_health():
        pass

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
            self.attacking = True
