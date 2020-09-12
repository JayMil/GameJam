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

DEBUG = True
WIDTH = 1024
HEIGHT = 768


window = None
if DEBUG:
    window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
    display = pyglet.canvas.get_display()
    screens = display.get_screens()
    main_monitor = screens[0]
    # Not working as expected. Figure out how to set to center screen
    # window.set_location(main_monitor.width//2, main_monitor.height//2)
    window.set_location(200, 0)
else:
    window = pyglet.window.Window(fullscreen=True)



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
