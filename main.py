import pyglet
from pyglet.window import key

import levelone

class GameController:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window
        self.active_env = None
        self.levelone_env = levelone.Level(self.window)
        self.start_game()

    def start_game(self):
        self.window.remove_handlers(self.active_env)
        self.active_env = self.levelone_env
        self.window.push_handlers(self.active_env)

    def draw(self):
        ''' Main draw method '''
        self.window.clear()
        if self.active_env:
            self.active_env.draw()

    def update(self, dt):
        if self.active_env:
            self.active_env.update(dt)

window = pyglet.window.Window(1024, 768)
window.set_location(400, 50)
gameController = GameController(window)
pyglet.clock.schedule_interval(gameController.update, 1/120.0)


@window.event
def on_draw():
    gameController.draw()

pyglet.app.run()
