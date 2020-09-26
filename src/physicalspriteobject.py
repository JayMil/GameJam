import pyglet

from collisionobject import CollisionObject

class PhysicalSpriteObject(pyglet.sprite.Sprite):
    ''' A physical sprite object '''
    def __init__(self, interaction, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = window
        self.hit_boxes = {}
        self.hit_boxes["sprite"]  = CollisionObject(self.x, self.y, self.width, self.height, interaction)
        self.hit_box = self.hit_boxes["sprite"]
