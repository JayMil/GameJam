import pyglet
from pyglet.window import key

import gameenvironment
from gameenvironment import GameEnvironment
import gamemap
import resources
from race import Facing


class Level(GameEnvironment):
    def __init__(self, background_image, name, window, *args, **kwargs):
        super().__init__(name, window, *args, **kwargs)

        self.background_image = background_image
        self.create_background()
        self.level_bounds = []
        self.level_objects = []

        

    def create_background(self):
        ''' Create sprite for the background image '''
        self.background_image = pyglet.sprite.Sprite(img=self.background_image, 
                                            batch=self.batch, group=self.background_layer, 
                                            x=0, y=0)
            
    def handle_environment_collisions(self, other_object):
        """ Detect and handle collisions with object and enviornment"""

        for obj in self.level_bounds:
            if obj.collides_with(other_object):
                if other_object.moving:
                    if other_object.moving.peek() == Facing.UP:
                        other_object.hit_box.y -= other_object.current_speed
                    elif other_object.moving.peek() == Facing.DOWN:
                        other_object.hit_box.y += other_object.current_speed
                    elif other_object.moving.peek() == Facing.LEFT:
                        other_object.hit_box.x += other_object.current_speed  
                    elif other_object.moving.peek() == Facing.RIGHT:
                        other_object.hit_box.x -= other_object.current_speed
                    else:
                        print("Unhandled Collision!")



        # self.background_layer = pyglet.graphics.OrderedGroup(0)
        # self.background_overlay_layer = pyglet.graphics.OrderedGroup(1)
        # self.foreground_underlay_layer = pyglet.graphics.OrderedGroup(2)
        # self.foreground_layer = pyglet.graphics.OrderedGroup(3)
        # self.foreground_overlay_layer = pyglet.graphics.OrderedGroup(4)
        # self.fg_overlay_group = pyglet.graphics.OrderedGroup(2)

        # # self.create_labels()
        # self.map = gamemap.GameMap(window, self.batch, self.background_layer)
        # self.hero = Hero(handle_sword_collisions=self.map.handle_sword_collisions, start_pos=(40, self.window.height-200), 
        #                 window=self.window, batch=self.batch, 
        #                 underlay_group=self.foreground_underlay_layer, 
        #                 overlay_group=self.foreground_overlay_layer,
        #                 group=self.foreground_layer)

        # self.window.push_handlers(self.hero)



    # def on_key_press(self, symbol, modifiers):
    #     if symbol == key.Q:
    #         self.on_exit()

    def update(self, dt):
        pass
        # self.hero.update(dt)
        # self.map.update(dt, self.hero)

    def draw(self):
        super().draw()

        '''
        # DEBUG
        if DEBUG:
            pass
            #self.draw_env_bounds()
            # draw player pos dot
            #height = self.hero.height-14
            #rectangle = pyglet.shapes.Rectangle(self.hero.hit_box.x, self.hero.hit_box.y, self.hero.width, height, color=(255, 0, 0))
            #rectangle.opacity = 125
            #rectangle.draw()
        '''
