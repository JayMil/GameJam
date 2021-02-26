import pyglet
from pyglet.window import key

from gameenvironment import GameEnvironment


RESTART = 0
EXIT = 1

FIRST_ITEM = RESTART
LAST_ITEM = EXIT

class GameOverMenu(GameEnvironment):
    def __init__(self, on_restart, on_exit, window):
        super().__init__("Game Over", window)

        self.winner = False

        # functions to call when finished
        self.on_restart = on_restart
        self.on_exit = on_exit

        # initially highlighted option
        self.active_item = RESTART

        # if user has selected an option
        self.finished = False

        # labels
        self.win_status = pyglet.text.Label(
            "",
            font_name="Times New Roman",
            font_size=60,
            x=self.window.width // 2,
            y=(self.window.height // 2) + 150,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )

        self.game_over = pyglet.text.Label(
            "Game Over",
            font_name="Times New Roman",
            font_size=40,
            x=self.window.width // 2,
            y=(self.window.height // 2) + 50,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )

        self.restart = pyglet.text.Label(
            "New Game",
            font_name="Times New Roman",
            font_size=24,
            x=self.window.width // 2,
            y=(self.window.height // 2) - 10,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )

        self.exit = pyglet.text.Label(
            "Exit",
            font_name="Times New Roman",
            font_size=24,
            x=self.window.width // 2,
            y=self.window.height // 2 - 50,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )


    def update(self, dt):
        if self.active_item == RESTART:
            self.restart.bold = True
            self.exit.bold = False
        else:
            self.restart.bold = False
            self.exit.bold = True

        if self.finished:
            self.finished = False
            if self.active_item == RESTART:
                self.on_restart()
            else:
                self.on_exit()

        if self.winner:
            self.win_status.text = "Winner!"
        else:
            self.win_status.text = "You Died!"

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.active_item += 1
        elif symbol == key.DOWN:
            self.active_item -= 1
        elif symbol == key.ENTER:
            self.finished = True

        if self.active_item > LAST_ITEM:
            self.active_item = FIRST_ITEM
        elif self.active_item < FIRST_ITEM:
            self.active_item = LAST_ITEM

    def on_key_release(self, symbol, modifiers):
        pass
