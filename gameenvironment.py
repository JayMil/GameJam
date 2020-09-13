import pyglet

class GameEnvironment():
    ''' A game enviornment - menu screen - level - etc.. '''
    def __init__(self, name, window, debug=False):

        self.name = name
        self.window = window
        self.batch = pyglet.graphics.Batch()
        self.debug_batch = pyglet.graphics.Batch()
        self.group = pyglet.graphics.OrderedGroup(0)
        self.group1 = pyglet.graphics.OrderedGroup(1)
        self.debug = debug

    def draw(self):
        self.batch.draw()
        if self.debug:
            self.debug_batch.draw()

    def update(self,dt):
        pass