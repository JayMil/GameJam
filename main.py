import pyglet
from pyglet.window import key

import levelone
from menu import MainMenu

DEBUG = False

class GameController:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window
        self.active_env = None
        self.levelone_env = levelone.LevelOne(self.window, debug=DEBUG)
        self.main_menu_env = MainMenu(on_start_game=self.start_game, on_exit=self.exit, window=self.window)
        self.start_menu()

    def start_game(self):
        if self.active_env:
            for handler in self.active_env.handlers:
                self.window.remove_handlers(handler)
            self.window.remove_handlers(self.active_env)
        self.active_env = self.levelone_env
        self.window.push_handlers(self.active_env)
        for handler in self.active_env.handlers:
            self.window.push_handlers(handler)

    def start_menu(self):
        if self.active_env:
            for handler in self.active_env.handlers:
                self.window.remove_handlers(handler)
            self.window.remove_handlers(self.active_env)
        self.active_env = self.main_menu_env
        self.window.push_handlers(self.active_env)
        for handler in self.active_env.handlers:
            self.window.push_handlers(handler)

    def exit(self):
        pyglet.app.exit()

    def draw(self):
        ''' Main draw method '''
        self.window.clear()
        if self.active_env:
            self.active_env.draw()

    def update(self, dt):
        if self.active_env:
            self.active_env.update(dt)


WIDTH = 1024
HEIGHT = 768


window = None

'''
if DEBUG:
'''
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
display = pyglet.canvas.get_display()
screens = display.get_screens()
main_monitor = screens[0]
# Not working as expected. Figure out how to set to center screen
# window.set_location(main_monitor.width//2, main_monitor.height//2)
window.set_location(200, 0)
'''
else:
    window = pyglet.window.Window(fullscreen=True)

'''


gameController = GameController(window)
pyglet.clock.schedule_interval(gameController.update, 1/120.0)


@window.event
def on_draw():
    gameController.draw()

pyglet.app.run()
