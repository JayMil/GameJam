import pyglet
from pyglet.window import key

import gameenvironment
from gameenvironment import GameEnvironment
import gamemap
import resources
from race import Facing

from healthpotion import HealthPotion
from movablerock import MovableRock

from inventory import InventoryType
from collisionobject import Interaction

class Level(GameEnvironment):
    def __init__(self, background_image, name, window, *args, **kwargs):
        super().__init__(name, window, *args, **kwargs)

        self.background_image = background_image
        self.create_background()
        self.level_bounds = []
        self.level_interactable_objects = []

        

    def create_background(self):
        ''' Create sprite for the background image '''
        self.background_image = pyglet.sprite.Sprite(img=self.background_image, 
                                            batch=self.batch, group=self.background_layer, 
                                            x=0, y=0)
            
    def handle_environment_collisions(self, other_object):
        """ Detect and handle collisions with object and enviornment"""

        for obj in self.level_bounds:
            if obj.collides_with(other_object.hit_boxes["feet"]):
                if other_object.moving:
                    if other_object.moving.peek() == Facing.UP:
                        other_object.update_pos(0, -other_object.current_speed)
                        break
                    elif other_object.moving.peek() == Facing.DOWN:
                        other_object.update_pos(0, other_object.current_speed)
                        break
                    elif other_object.moving.peek() == Facing.LEFT:
                        other_object.update_pos(other_object.current_speed, 0)
                        break
                    elif other_object.moving.peek() == Facing.RIGHT:
                        other_object.update_pos(-other_object.current_speed, 0)
                        break
                    else:
                        print("Unhandled Collision!")
        
    def handle_interactable_object_collisions(self, other_object):
        """ Detect and handle collisions with object and enviornment"""

        items_to_delete = []


        for obj in self.level_interactable_objects:
            if obj.hit_box.collides_with(other_object.hit_boxes["feet"]):
                if type(obj) is HealthPotion:
                    items_to_delete.append(obj)
                    other_object.update_stats(1, InventoryType.HEALING_POTIONS)
                elif type(obj) is MovableRock:
                    if other_object.moving:
                        if other_object.moving.peek() == Facing.UP:
                            other_object.update_pos(0, other_object.current_speed * -0.75)
                            obj.y += other_object.current_speed * 0.25
                            obj.hit_box.y += other_object.current_speed * 0.25

                            if self.check_if_rock_collides_with_bounds(obj):
                                other_object.update_pos(0, other_object.current_speed * -0.25)
                                obj.y -= other_object.current_speed * 0.25
                                obj.hit_box.y -= other_object.current_speed * 0.25

                        elif other_object.moving.peek() == Facing.DOWN:
                            other_object.update_pos(0, other_object.current_speed * 0.75)
                            obj.y -= other_object.current_speed * 0.25
                            obj.hit_box.y -= other_object.current_speed * 0.25

                            if self.check_if_rock_collides_with_bounds(obj):
                                other_object.update_pos(0, other_object.current_speed * 0.25)
                                obj.y += other_object.current_speed * 0.25
                                obj.hit_box.y += other_object.current_speed * 0.25

                        elif other_object.moving.peek() == Facing.LEFT:
                            other_object.update_pos(other_object.current_speed * 0.75, 0)
                            obj.x -= other_object.current_speed * 0.25
                            obj.hit_box.x -= other_object.current_speed * 0.25

                            if self.check_if_rock_collides_with_bounds(obj):
                                other_object.update_pos(other_object.current_speed * 0.25, 0)
                                obj.x += other_object.current_speed * 0.25
                                obj.hit_box.x += other_object.current_speed * 0.25

                        elif other_object.moving.peek() == Facing.RIGHT:
                            other_object.update_pos(other_object.current_speed * -0.75, 0)
                            obj.x += other_object.current_speed * 0.25
                            obj.hit_box.x += other_object.current_speed * 0.25

                            if self.check_if_rock_collides_with_bounds(obj):
                                other_object.update_pos(other_object.current_speed * -0.25, 0)
                                obj.x -= other_object.current_speed * 0.25
                                obj.hit_box.x -= other_object.current_speed * 0.25

                        else:
                            print("Unhandled Collision!")


        if items_to_delete != []:
            for obj in items_to_delete:
                self.level_interactable_objects.remove(obj)
                


        
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


    def check_if_rock_collides_with_bounds(self, obj):
        for level_bound in self.level_bounds:
            if obj.hit_box.collides_with(level_bound):
                if level_bound.interaction == Interaction.BLOCKING:
                    return True
                    break
      

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
