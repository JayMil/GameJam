import pyglet

class GameController:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window

    def draw(self):
        ''' Main draw method '''
        self.window.clear()

    def update(self, dt):
        pass

window = pyglet.window.Window(1024, 768)
window.set_location(400, 50)
gameController = GameController(window)
pyglet.clock.schedule_interval(gameController.update, 1/120.0)
class GameController:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window

@window.event
def on_draw():
    gameController.draw()

pyglet.app.run()
