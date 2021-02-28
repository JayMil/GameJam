import pyglet
from pyglet.window import key

from gameenvironment import GameEnvironment
from resources import controls_image

RESUME = 0
EXIT = 1
RESTART = 2


class PauseMenu(GameEnvironment):
    def __init__(self, on_resume, on_restart, on_exit, window):
        super().__init__("Pause", window)

        # functions to call when finished
        self.on_resume = on_resume
        self.on_restart = on_restart
        self.on_exit = on_exit

        self.active_item = RESUME
        self.finished = False
        self.resume = pyglet.text.Label(
            "Resume",
            font_name="Times New Roman",
            font_size=24,
            x=self.window.width // 2,
            y=(self.window.height // 2) + 30,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )

        self.restart = pyglet.text.Label(
            "Restart",
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

        scale = .75
        self.controls = pyglet.sprite.Sprite(
            img=controls_image,
            batch=self.batch,
            x=self.window.width // 2 - (400 * scale),
            y=self.window.height // 2 - 90 - (controls_image.height * scale),
        )
        self.controls.scale = scale

    def update(self, dt):
        if self.active_item == RESUME:
            self.resume.bold = True
            self.restart.bold = False
            self.exit.bold = False
        elif self.active_item == RESTART:
            self.resume.bold = False
            self.restart.bold = True
            self.exit.bold = False
        else:
            self.resume.bold = False
            self.restart.bold = False
            self.exit.bold = True

        if self.finished:
            self.finished = False
            if self.active_item == RESUME:
                print("Calling on_resume")
                self.on_resume()
            elif self.active_item == RESTART:
                print("Calling on_restart")
                self.on_restart()
            else:
                self.on_exit()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.active_item += 1
        elif symbol == key.DOWN:
            self.active_item -= 1
        elif symbol == key.ENTER:
            self.finished = True

        if self.active_item > RESTART:
            self.active_item = 0
        elif self.active_item < 0:
            self.active_item = 2

    def on_key_release(self, symbol, modifiers):
        pass
