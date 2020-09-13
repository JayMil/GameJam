import pyglet

from collisionobject import CollisionObject

class PhysicalSpriteObject(pyglet.sprite.Sprite):
    ''' A physical sprite object '''
    def __init__(self, interaction, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = window
        self.hit_box = CollisionObject(self.x, self.y, self.width, self.height, interaction)
