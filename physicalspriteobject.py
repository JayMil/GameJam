class PhysicalSpriteObject(pyglet.sprite.Sprite):
    ''' A physical sprite object '''
    def __init__(self, window, group=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = window
        self.group = group
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.hit_box = CollisionObject(self.x, self.y, self.width, self.height)
