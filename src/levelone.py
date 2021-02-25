import pyglet
from pyglet.window import key

import gameenvironment
from gameenvironment import GameEnvironment
import gamemap
from hero import Hero
from enemy import Enemy

import level
from level import Level
import resources
import collisionobject
from collisionobject import CollisionObject
from collisionobject import Interaction

from inventory import Inventory
from movablerock import MovableRock

from healthpotion import HealthPotion


class LevelOne(Level):
    def __init__(self, window, on_pause, on_restart, on_game_over, on_exit, *args, **kwargs):
        super().__init__(
            background_image=resources.background_image,
            name="LevelOne",
            window=window,
            *args,
            **kwargs
        )

        # self.create_labels()
        # self.map = gamemap.GameMap(window, self.batch, self.background_layer)

        self.on_pause = on_pause
        self.on_restart = on_restart
        self.on_game_over = on_game_over
        self.on_exit = on_exit

        tile_size = 32

        self.inventory = Inventory(
            batch=self.batch,
            foreground_underlay_layer=self.foreground_underlay_layer,
            foreground_layer=self.foreground_layer,
            foreground_overlay_layer=self.foreground_overlay_layer,
        )

        self.hero = Hero(
            self.inventory.update_inventory,
            x=tile_size * 4,
            y=tile_size * 15,
            window=self.window,
            batch=self.batch,
            group=self.foreground_layer,
        )

        self.handlers.append(self.hero)

        self.enemies = []
        self.enemies.append(
            Enemy(
                x=tile_size * 8,
                y=tile_size * 15,
                target=self.hero.hit_boxes["feet"],
                window=self.window,
                batch=self.batch,
                group=self.foreground_layer,
            )
        )

        self.create_level_bounds()

    def create_level_bounds(self):
        """ Create object in environment """
        tile_size = 32

        block_color = (100, 100, 100)

        self.environment_matrix = [
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, ],
            [ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        ]

        self.level_interactable_objects.append(
            MovableRock(
                tile_size * 2,
                tile_size * 4,
                self.window,
                group=self.background_overlay_layer,
                batch=self.batch,
            )
        )
        self.level_interactable_objects.append(
            MovableRock(
                tile_size * 26,
                tile_size * 15,
                self.window,
                group=self.background_overlay_layer,
                batch=self.batch,
            )
        )
        self.level_interactable_objects.append(
            MovableRock(
                tile_size * 23,
                tile_size * 10,
                self.window,
                group=self.background_overlay_layer,
                batch=self.batch,
            )
        )

        # self.level_interactable_objects.append(
        #     HealthPotion(
        #         tile_size * 16,
        #         tile_size * 10,
        #         self.window,
        #         group=self.background_overlay_layer,
        #         batch=self.batch,
        #     )
        # )

        # self.level_interactable_objects.append(
        #     HealthPotion(
        #         tile_size * 7,
        #         tile_size * 8,
        #         self.window,
        #         group=self.background_overlay_layer,
        #         batch=self.batch,
        #     )
        # )

        # self.level_interactable_objects.append(
        #     HealthPotion(
        #         tile_size * 9,
        #         tile_size * 13,
        #         self.window,
        #         group=self.background_overlay_layer,
        #         batch=self.batch,
        #     )
        # )

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

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            self.on_exit()
        elif symbol == key.E:
            self.on_pause()
        elif symbol == key.R:
            self.on_restart()

    def update(self, dt):
        self.hero.update(dt)

        if self.hero.moving:
            self.handle_environment_collisions(self.hero, [1, 2])
            self.handle_interactable_object_collisions(self.hero)

        for enemy in self.enemies:
            enemy.update(dt)
            self.handle_environment_collisions_enemy(enemy, [1, 2])

        if self.hero.dead():
            self.on_game_over()

    def draw(self):
        super().draw()

        rectangle = pyglet.shapes.Rectangle(
            self.hero.hit_boxes["feet"].x,
            self.hero.hit_boxes["feet"].y,
            self.hero.hit_boxes["feet"].width,
            self.hero.hit_boxes["feet"].height,
            color=(255, 0, 0),
        )
        rectangle.opacity = 125
        rectangle.draw()

        """
        # DEBUG
        if DEBUG:
            pass
            #self.draw_env_bounds()
            # draw player pos dot
            #height = self.hero.height-14
            #rectangle = pyglet.shapes.Rectangle(self.hero.hit_box.x, self.hero.self.hit_boxes["feet"].yhit_box.y, self.hero.width, height, color=(255, 0, 0))
            #rectangle.opacity = 125
            #rectangle.draw()
        """
