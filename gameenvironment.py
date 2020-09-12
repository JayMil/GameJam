import pyglet

class GameEnvironment():
    ''' A game enviornment - menu screen - level - etc.. '''
    def __init__(self, name, window):
        self.name = name
        self.window = window
        self.batch = pyglet.graphics.Batch()
        self.group = pyglet.graphics.OrderedGroup(0)

    def draw(self):
        self.batch.draw()

    def update(self,dt):
        pass