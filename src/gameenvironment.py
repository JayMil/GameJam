import pyglet


class GameEnvironment:
    """ A game enviornment - menu screen - level - etc.. """

    def __init__(self, name, window, debug=False):

        self.name = name
        self.window = window
        self.batch = pyglet.graphics.Batch()
        self.debug_batch = pyglet.graphics.Batch()
        self.background_layer = pyglet.graphics.OrderedGroup(0)
        self.background_overlay_layer = pyglet.graphics.OrderedGroup(1)
        self.foreground_underlay_layer = pyglet.graphics.OrderedGroup(2)
        self.foreground_layer = pyglet.graphics.OrderedGroup(3)
        self.foreground_overlay_layer = pyglet.graphics.OrderedGroup(4)
        self.debug = debug
        self.handlers = []

    def draw(self):
        self.batch.draw()
        if self.debug:
            self.debug_batch.draw()

    def update(self, dt):
        pass
