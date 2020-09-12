import pyglet

class GameEnvironment():
    ''' A game enviornment - menu screen - level - etc.. '''
    def __init__(self, name, window):
        self.name = name
        self.window = window
        self.batch = pyglet.graphics.Batch()

    def draw(self):
        self.batch.draw()

    def update(self):
        pass