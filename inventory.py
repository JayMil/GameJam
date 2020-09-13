from pyglet import shapes
import pyglet
import resources
from enum import Enum

class InventorySprite(pyglet.sprite.Sprite):
    ''' A health bar sprite '''
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.x = x
        self.y = y


class Inventory():
    ''' An object for inventory item sprites and shapes '''    
    def __init__(self, batch, foreground_underlay_layer, foreground_layer, foreground_overlay_layer):

        self.batch = batch
        self.foreground_underlay_layer = foreground_underlay_layer
        self.foreground_layer = foreground_layer
        self.foreground_overlay_layer = foreground_overlay_layer
        self.health_hearts = self.create_health_hearts()
        self.create_health_potion_counter()

    def create_health_hearts(self):

        tile_size = 32
        heart_y = tile_size*22.5
        self.health_holder = InventorySprite(tile_size*11, tile_size*22, img=resources.heart_holder, batch=self.batch, group=self.foreground_underlay_layer)

        # Create the empty heart that will go behind the filled hearts
        self.health_heart_empty1 = InventorySprite(tile_size*11.5, heart_y, img=resources.health_bar_heart_empty, batch=self.batch, group=self.foreground_layer)
        self.health_heart_empty2 = InventorySprite(tile_size*13.5, heart_y, img=resources.health_bar_heart_empty, batch=self.batch, group=self.foreground_layer)
        self.health_heart_empty3 = InventorySprite(tile_size*15.5, heart_y, img=resources.health_bar_heart_empty, batch=self.batch, group=self.foreground_layer)
        self.health_heart_empty4 = InventorySprite(tile_size*17.5, heart_y, img=resources.health_bar_heart_empty, batch=self.batch, group=self.foreground_layer)
        self.health_heart_empty5 = InventorySprite(tile_size*19.5, heart_y, img=resources.health_bar_heart_empty, batch=self.batch, group=self.foreground_layer)

        health_hearts = []

        # Create the filled hearts that represent a health point
        health_heart1 = InventorySprite(tile_size*11.5, heart_y, img=resources.health_bar_heart, batch=self.batch, group=self.foreground_overlay_layer)
        health_heart2 = InventorySprite(tile_size*13.5, heart_y, img=resources.health_bar_heart, batch=self.batch, group=self.foreground_overlay_layer)
        health_heart3 = InventorySprite(tile_size*15.5, heart_y, img=resources.health_bar_heart, batch=self.batch, group=self.foreground_overlay_layer)
        health_heart4 = InventorySprite(tile_size*17.5, heart_y, img=resources.health_bar_heart, batch=self.batch, group=self.foreground_overlay_layer)
        health_heart5 = InventorySprite(tile_size*19.5, heart_y, img=resources.health_bar_heart, batch=self.batch, group=self.foreground_overlay_layer)

        health_hearts.append(health_heart1)
        health_hearts.append(health_heart2)
        health_hearts.append(health_heart3)
        health_hearts.append(health_heart4)
        health_hearts.append(health_heart5)

        return health_hearts

    def create_health_potion_counter(self):

        tile_size = 32

        self.backpack_inventory = InventorySprite(tile_size*30, tile_size*22, img=resources.backpack_inventory, batch=self.batch, group=self.foreground_underlay_layer)
        self.health_potion_sprite = InventorySprite(tile_size*30.5, tile_size*22.5, img=resources.health_potion, batch=self.batch, group=self.foreground_layer)
        self.health_potion_counter = pyglet.text.Label('',
                                    font_name='Arial',
                                    font_size=10,
                                    x=self.health_potion_sprite.x+28, y=self.health_potion_sprite.y-4,
                                    batch=self.batch, group=self.foreground_layer)
        self.health_potion_sprite.visible = False

    def update_inventory(self, value, inventory_type):
        if inventory_type.HEALTH:
            update_health(value)
        elif inventory_type.HEALING_POTIONS:
            update_potions(value)



    # Update the health bar to the new health. Health is assumed to be based on 100 max health.
    def update_health(self, new_health):
        # Go through all of the hearts and change the image to an empty heart for any that represent health higher than what the player has.
        for index, obj in enumerate(self.health_hearts):
            if (new_health - 1) < index:
                obj.visible = False
            else:
                obj.visible = True

    def update_potions(self, new_potions_count):
        # print(new_potions_count)
        self.health_potion_counter.text = str(new_potions_count)

        if new_potions_count == 0:
            self.health_potion_counter.text = ""
            self.health_potion_sprite.visible = False
        else:
            self.health_potion_sprite.visible = True   

class InventoryType(Enum):
    HEALTH = 1
    HEALING_POTIONS = 2