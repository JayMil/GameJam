import pyglet
from pyglet.window import key

import levelone
from menu import MainMenu
from pause import PauseMenu
from gameover import GameOverMenu

DEBUG = False


class GameController:
    """ Main Game Object to handle overall game logic """

    def __init__(self, window):
        self.window = window
        self.active_env = None
        self.levelone_env = self.init_levelone()

        self.main_menu_env = MainMenu(
            on_start_game=self.start_game, on_exit=self.exit, window=self.window
        )

        self.pause_env = PauseMenu(
            on_resume=self.start_game, on_restart=self.restart, on_exit=self.exit, window=self.window
        )

        self.game_over_env = GameOverMenu(
            on_restart=self.restart, on_exit=self.exit, window=self.window
        )

        self.start_menu()

    def init_levelone(self):
        return levelone.LevelOne(self.window, on_pause=self.pause_game,
                                 on_restart=self.restart, on_game_over=self.game_over,
                                 on_exit=self.exit, debug=DEBUG)

    def start_game(self):
        self.switch_env(self.levelone_env)

    def start_menu(self):
        self.switch_env(self.main_menu_env)

    def pause_game(self):
        self.switch_env(self.pause_env)

    def game_over(self):
        self.switch_env(self.game_over_env)

    def restart(self):
        self.deactivate_active_env()
        del self.levelone_env
        self.levelone_env = self.init_levelone()
        self.start_game()

    def switch_env(self, env):
        self.deactivate_active_env()
        self.activate_env(env)

    def deactivate_active_env(self):
        if self.active_env:
            for handler in self.active_env.handlers:
                self.window.remove_handlers(handler)
            self.window.remove_handlers(self.active_env)

    def activate_env(self, env):
        self.active_env = env
        self.window.push_handlers(self.active_env)
        for handler in self.active_env.handlers:
            self.window.push_handlers(handler)


    def exit(self):
        pyglet.app.exit()

    def draw(self):
        """ Main draw method """
        self.window.clear()
        if self.active_env:
            self.active_env.draw()

    def update(self, dt):
        if self.active_env:
            self.active_env.update(dt)


WIDTH = 1024
HEIGHT = 768


window = None

"""
if DEBUG:
"""
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
display = pyglet.canvas.get_display()
screens = display.get_screens()
main_monitor = screens[0]
# Not working as expected. Figure out how to set to center screen
# window.set_location(main_monitor.width//2, main_monitor.height//2)
window.set_location(200, 0)
"""
else:
    window = pyglet.window.Window(fullscreen=True)

"""


gameController = GameController(window)
pyglet.clock.schedule_interval(gameController.update, 1 / 120.0)


@window.event
def on_draw():
    gameController.draw()


pyglet.app.run()
