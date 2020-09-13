import pyglet
from pyglet.window import key

import gameenvironment
from gameenvironment import GameEnvironment
import gamemap

import level
from level import Level
import resources
import collisionobject
from collisionobject import CollisionObject
from collisionobject import InteractionEnum

class LevelOne(Level):
    def __init__(self, window, *args, **kwargs):
        super().__init__(background_image=resources.background_image , name="LevelOne", window=window, *args, **kwargs)

        
        # self.create_labels()
        # self.map = gamemap.GameMap(window, self.batch, self.background_layer)

        self.create_level_bounds()


    def create_level_bounds(self):
        """ Create object in environment """
        tile_size = 32

        border_object_1 = CollisionObject(x=0, y=tile_size*5, height=288, width=tile_size*1, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_2 = CollisionObject(x=0, y=448, height=256, width=tile_size*2, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_3 = CollisionObject(x=tile_size*2, y=672, height=tile_size*1, width=352, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_4 = CollisionObject(x=416, y=tile_size*20, height=tile_size*2, width=tile_size*15, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_5 = CollisionObject(x=896, y=288, height=416, width=128, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_6 = CollisionObject(x=tile_size*2, y=tile_size*6, height=32, width=64, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_7 = CollisionObject(x=tile_size*23, y=tile_size*17, height=tile_size*2, width=tile_size*1, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_8 = CollisionObject(x=tile_size*25, y=tile_size*14, height=tile_size*3, width=tile_size*1, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_9 = CollisionObject(x=tile_size*26, y=tile_size*18, height=tile_size*1, width=tile_size*2, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_10 = CollisionObject(x=tile_size*0, y=tile_size*3, height=tile_size*2, width=tile_size*2, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_11 = CollisionObject(x=tile_size*0, y=tile_size*0, height=tile_size*3, width=tile_size*32, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_12 = CollisionObject(x=tile_size*4, y=tile_size*3, height=tile_size*2, width=tile_size*7, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))
        border_object_13 = CollisionObject(x=tile_size*28, y=tile_size*3, height=tile_size*4, width=tile_size*4, interaction=InteractionEnum.BLOCKING, group=self.group1, batch=self.debug_batch, color=(255, 255, 0))

        self.level_bounds.append(border_object_1)
        self.level_bounds.append(border_object_2)
        self.level_bounds.append(border_object_3)
        self.level_bounds.append(border_object_4)
        self.level_bounds.append(border_object_5)
        self.level_bounds.append(border_object_6)
        self.level_bounds.append(border_object_7)
        self.level_bounds.append(border_object_8)
        self.level_bounds.append(border_object_9)
        self.level_bounds.append(border_object_10)
        self.level_bounds.append(border_object_11)
        self.level_bounds.append(border_object_12)
        self.level_bounds.append(border_object_13)
        # self.hero = Hero(handle_sword_collisions=self.map.handle_sword_collisions, start_pos=(40, self.window.height-200), 
        #                 window=self.window, batch=self.batch, 
        #                 underlay_group=self.foreground_underlay_layer, 
        #                 overlay_group=self.foreground_overlay_layer,
        #                 group=self.foreground_layer)

        # self.window.push_handlers(self.hero)


    # def create_labels(self):
    #     ''' Create helper lables '''
    #     self.title = pyglet.text.Label('Top - View Proof of Concept',
    #                                 font_name='Times New Roman',
    #                                 font_size=24,
    #                                 x=self.window.width//2, y=self.window.height-30,
    #                                 anchor_x='center', batch=self.batch,
    #                                 group=self.foreground_layer)


    #     pyglet.text.Label('Move with direction keys',
    #                                 font_name='Times New Roman',
    #                                 font_size=16,
    #                                 x=20, y=self.window.height-60,
    #                                 batch=self.batch, group=self.foreground_layer)

    #     pyglet.text.Label("Move fast with 'f' key",
    #                                 font_name='Times New Roman',
    #                                 font_size=16,
    #                                 x=20, y=self.window.height-90,
    #                                 batch=self.batch, group=self.foreground_layer)

    #     pyglet.text.Label("Press 'q' to quit",
    #                                 font_name='Times New Roman',
    #                                 font_size=16,
    #                                 x=20, y=self.window.height-120,
    #                                 batch=self.batch, group=self.foreground_layer)

    # def on_key_press(self, symbol, modifiers):
    #     if symbol == key.Q:
    #         self.on_exit()

    def update(self, dt):
        pass
        # self.hero.update(dt)
        # self.map.update(dt, self.hero)

    def draw(self):
        super().draw();

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
