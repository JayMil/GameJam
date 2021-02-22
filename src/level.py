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
import math


class Level(GameEnvironment):
    def __init__(self, background_image, name, window, *args, **kwargs):
        super().__init__(name, window, *args, **kwargs)

        self.background_image = background_image
        self.create_background()
        self.level_bounds = []
        self.level_interactable_objects = []
        self.sunk_rocks = []

        self.tile_size = 32
        self.screen_height = self.tile_size * 25
        self.screen_width = self.tile_size * 32

    def create_background(self):
        """ Create sprite for the background image """
        self.background_image = pyglet.sprite.Sprite(
            img=self.background_image,
            batch=self.batch,
            group=self.background_layer,
            x=0,
            y=0,
        )

    def handle_environment_collisions(self, other_object, collision_array):
        """ Detect and handle collisions with object and enviornment"""

        if other_object.moving.peek() == Facing.UP:
            matrix_y = math.floor(
                (
                    self.screen_height
                    - other_object.hit_boxes["feet"].y
                    - other_object.hit_boxes["feet"].height
                )
                / self.tile_size
            )
            matrix_x1 = math.floor(other_object.hit_boxes["feet"].x / self.tile_size)
            matrix_x2 = math.floor(
                (
                    other_object.hit_boxes["feet"].x
                    + other_object.hit_boxes["feet"].width
                )
                / self.tile_size
            )

            if self.environment_matrix[matrix_y][matrix_x1] in collision_array:
                other_object.update_pos(0, -other_object.current_speed)
            elif self.environment_matrix[matrix_y][matrix_x2] in collision_array:
                other_object.update_pos(0, -other_object.current_speed)
        elif other_object.moving.peek() == Facing.DOWN:
            matrix_y = math.floor(
                (self.screen_height - other_object.hit_boxes["feet"].y) / self.tile_size
            )
            matrix_x1 = math.floor(other_object.hit_boxes["feet"].x / self.tile_size)
            matrix_x2 = math.floor(
                (
                    other_object.hit_boxes["feet"].x
                    + other_object.hit_boxes["feet"].width
                )
                / self.tile_size
            )
            if self.environment_matrix[matrix_y][matrix_x1] in collision_array:
                other_object.update_pos(0, other_object.current_speed)
            elif self.environment_matrix[matrix_y][matrix_x2] in collision_array:
                other_object.update_pos(0, other_object.current_speed)
        elif other_object.moving.peek() == Facing.LEFT:
            matrix_x = math.floor(other_object.hit_boxes["feet"].x / self.tile_size)
            matrix_y1 = math.floor(
                (
                    self.screen_height
                    - other_object.hit_boxes["feet"].y
                    - other_object.hit_boxes["feet"].height
                )
                / self.tile_size
            )
            matrix_y2 = math.floor(
                (self.screen_height - other_object.hit_boxes["feet"].y) / self.tile_size
            )

            if self.environment_matrix[matrix_y1][matrix_x] in collision_array:
                other_object.update_pos(other_object.current_speed, 0)
            elif self.environment_matrix[matrix_y2][matrix_x] in collision_array:
                other_object.update_pos(other_object.current_speed, 0)
        elif other_object.moving.peek() == Facing.RIGHT:
            matrix_x = math.floor(
                (
                    other_object.hit_boxes["feet"].x
                    + other_object.hit_boxes["feet"].width
                )
                / self.tile_size
            )
            matrix_y1 = math.floor(
                (
                    self.screen_height
                    - other_object.hit_boxes["feet"].y
                    - other_object.hit_boxes["feet"].height
                )
                / self.tile_size
            )
            matrix_y2 = math.floor(
                (self.screen_height - other_object.hit_boxes["feet"].y) / self.tile_size
            )

            if self.environment_matrix[matrix_y1][matrix_x] in collision_array:
                other_object.update_pos(-other_object.current_speed, 0)
            elif self.environment_matrix[matrix_y2][matrix_x] in collision_array:
                other_object.update_pos(-other_object.current_speed, 0)

    def handle_environment_collisions_enemy(self, other_object, collision_array):
        """ Detect and handle collisions with object and enviornment"""

        if other_object.facing == Facing.UP:
            matrix_y = math.floor(
                (
                    self.screen_height
                    - other_object.hit_boxes["feet"].y
                    - other_object.hit_boxes["feet"].height
                )
                / self.tile_size
            )
            matrix_x1 = math.floor(other_object.hit_boxes["feet"].x / self.tile_size)
            matrix_x2 = math.floor(
                (
                    other_object.hit_boxes["feet"].x
                    + other_object.hit_boxes["feet"].width
                )
                / self.tile_size
            )

            if self.environment_matrix[matrix_y][matrix_x1] in collision_array:
                other_object.update_pos(0, -other_object.current_speed)
                other_object.stop_movement_animation()
            elif self.environment_matrix[matrix_y][matrix_x2] in collision_array:
                other_object.update_pos(0, -other_object.current_speed)
                other_object.stop_movement_animation()

        elif other_object.facing == Facing.DOWN:
            matrix_y = math.floor(
                (self.screen_height - other_object.hit_boxes["feet"].y) / self.tile_size
            )
            matrix_x1 = math.floor(other_object.hit_boxes["feet"].x / self.tile_size)
            matrix_x2 = math.floor(
                (
                    other_object.hit_boxes["feet"].x
                    + other_object.hit_boxes["feet"].width
                )
                / self.tile_size
            )
            if self.environment_matrix[matrix_y][matrix_x1] in collision_array:
                other_object.update_pos(0, other_object.current_speed)
                other_object.stop_movement_animation()
            elif self.environment_matrix[matrix_y][matrix_x2] in collision_array:
                other_object.update_pos(0, other_object.current_speed)
                other_object.stop_movement_animation()
        elif other_object.facing == Facing.LEFT:
            matrix_x = math.floor(other_object.hit_boxes["feet"].x / self.tile_size)
            matrix_y1 = math.floor(
                (
                    self.screen_height
                    - other_object.hit_boxes["feet"].y
                    - other_object.hit_boxes["feet"].height
                )
                / self.tile_size
            )
            matrix_y2 = math.floor(
                (self.screen_height - other_object.hit_boxes["feet"].y) / self.tile_size
            )

            if self.environment_matrix[matrix_y1][matrix_x] in collision_array:
                other_object.update_pos(other_object.current_speed, 0)
                other_object.stop_movement_animation()
            elif self.environment_matrix[matrix_y2][matrix_x] in collision_array:
                other_object.update_pos(other_object.current_speed, 0)
                other_object.stop_movement_animation()
        elif other_object.facing == Facing.RIGHT:
            matrix_x = math.floor(
                (
                    other_object.hit_boxes["feet"].x
                    + other_object.hit_boxes["feet"].width
                )
                / self.tile_size
            )
            matrix_y1 = math.floor(
                (
                    self.screen_height
                    - other_object.hit_boxes["feet"].y
                    - other_object.hit_boxes["feet"].height
                )
                / self.tile_size
            )
            matrix_y2 = math.floor(
                (self.screen_height - other_object.hit_boxes["feet"].y) / self.tile_size
            )

            if self.environment_matrix[matrix_y1][matrix_x] in collision_array:
                other_object.update_pos(-other_object.current_speed, 0)
                other_object.stop_movement_animation()
            elif self.environment_matrix[matrix_y2][matrix_x] in collision_array:
                other_object.update_pos(-other_object.current_speed, 0)
                other_object.stop_movement_animation()

    def handle_interactable_object_collisions(self, other_object):
        """ Detect and handle collisions with object and enviornment"""

        items_to_delete = []

        for obj in self.level_interactable_objects:
            if obj.hit_box.collides_with(other_object.hit_boxes["feet"]):
                if type(obj) is HealthPotion:
                    items_to_delete.append(obj)
                    other_object.update_stats(1, InventoryType.HEALING_POTIONS)
                elif type(obj) is MovableRock:
                    if obj.interaction == Interaction.MOVABLE:
                        if other_object.moving.peek() == Facing.UP:
                            other_object.update_pos(
                                0, other_object.current_speed * -0.75
                            )
                            obj.y += other_object.current_speed * 0.25
                            obj.hit_box.y += other_object.current_speed * 0.25

                            bound_collision_check = (
                                self.check_if_rock_collides_with_bounds(obj)
                            )

                            if bound_collision_check == Interaction.BLOCKING:
                                other_object.update_pos(
                                    0, other_object.current_speed * -0.25
                                )
                                obj.y -= other_object.current_speed * 0.25
                                obj.hit_box.y -= other_object.current_speed * 0.25
                            elif bound_collision_check == Interaction.SHALLOW_WATER:
                                self.sink_rock_in_water(obj, Facing.UP)

                        elif other_object.moving.peek() == Facing.DOWN:
                            other_object.update_pos(
                                0, other_object.current_speed * 0.75
                            )
                            obj.y -= other_object.current_speed * 0.25
                            obj.hit_box.y -= other_object.current_speed * 0.25

                            bound_collision_check = (
                                self.check_if_rock_collides_with_bounds(obj)
                            )

                            if bound_collision_check == Interaction.BLOCKING:
                                other_object.update_pos(
                                    0, other_object.current_speed * 0.25
                                )
                                obj.y += other_object.current_speed * 0.25
                                obj.hit_box.y += other_object.current_speed * 0.25
                            elif bound_collision_check == Interaction.SHALLOW_WATER:
                                self.sink_rock_in_water(obj, Facing.DOWN)

                        elif other_object.moving.peek() == Facing.LEFT:
                            other_object.update_pos(
                                other_object.current_speed * 0.75, 0
                            )
                            obj.x -= other_object.current_speed * 0.25
                            obj.hit_box.x -= other_object.current_speed * 0.25

                            bound_collision_check = (
                                self.check_if_rock_collides_with_bounds(obj)
                            )

                            if bound_collision_check == Interaction.BLOCKING:
                                other_object.update_pos(
                                    other_object.current_speed * 0.25, 0
                                )
                                obj.x += other_object.current_speed * 0.25
                                obj.hit_box.x += other_object.current_speed * 0.25
                            elif bound_collision_check == Interaction.SHALLOW_WATER:
                                self.sink_rock_in_water(obj, Facing.LEFT)

                        elif other_object.moving.peek() == Facing.RIGHT:
                            other_object.update_pos(
                                other_object.current_speed * -0.75, 0
                            )
                            obj.x += other_object.current_speed * 0.25
                            obj.hit_box.x += other_object.current_speed * 0.25

                            bound_collision_check = (
                                self.check_if_rock_collides_with_bounds(obj)
                            )

                            if bound_collision_check == Interaction.BLOCKING:
                                other_object.update_pos(
                                    other_object.current_speed * -0.25, 0
                                )
                                obj.x -= other_object.current_speed * 0.25
                                obj.hit_box.x -= other_object.current_speed * 0.25
                            elif bound_collision_check == Interaction.SHALLOW_WATER:
                                self.sink_rock_in_water(obj, Facing.RIGHT)

                        else:
                            print("Unhandled Collision!")
                        break

        for obj in items_to_delete:
            self.level_interactable_objects.remove(obj)

    def handle_sunk_rock_collisions(self, other_object):
        for obj in self.sunk_rocks:
            if other_object.hit_boxes["feet"].collides_with(obj.hit_box):
                return True
        return False

    def check_if_rock_collides_with_bounds(self, obj):

        x1 = math.floor((obj.hit_box.x + obj.hit_box.width) / self.tile_size)
        x2 = math.floor(obj.hit_box.x / self.tile_size)
        y1 = math.floor(
            (self.screen_height - obj.hit_box.y - obj.hit_box.height) / self.tile_size
        )
        y2 = math.floor((self.screen_height - obj.hit_box.y) / self.tile_size)

        corner1 = self.environment_matrix[y1][x1]
        corner2 = self.environment_matrix[y1][x2]
        corner3 = self.environment_matrix[y2][x1]
        corner4 = self.environment_matrix[y2][x2]

        if corner1 == 1 or corner2 == 1 or corner3 == 1 or corner4 == 1:
            return Interaction.BLOCKING
        elif corner1 == 2 or corner2 == 2 or corner3 == 2 or corner4 == 2:
            return Interaction.SHALLOW_WATER

        return False

    def check_amount_of_overlap_for_two_rectangles(self, obj1, obj2):
        x_overlap = max(
            0,
            min(obj1.x + obj1.width, obj2.x + obj2.width) - max(obj1.x, obj2.x),
        )
        y_overlap = max(
            0,
            min(obj1.y + obj1.height, obj2.y + obj2.height) - max(obj1.y, obj2.y),
        )
        overlap_area = x_overlap * y_overlap
        return overlap_area

    def sink_rock_in_water(self, rock, push_direction):

        tile_position_x = rock.x / self.tile_size
        tile_position_y = rock.y / self.tile_size

        if push_direction == Facing.UP:
            tile_position_y += 1
        elif push_direction == Facing.DOWN:
            tile_position_y -= 1
        elif push_direction == Facing.RIGHT:
            tile_position_x += 1
        elif push_direction == Facing.LEFT:
            tile_position_x -= 1

        if (tile_position_x - math.floor(tile_position_x)) < 0.5:
            x_pos = math.floor(tile_position_x)
        else:
            x_pos = math.ceil(tile_position_x)

        if (tile_position_y - math.floor(tile_position_y)) < 0.5:
            y_pos = math.floor(tile_position_y)
        else:
            y_pos = math.ceil(tile_position_y)

        rock.x = x_pos * self.tile_size
        rock.y = y_pos * self.tile_size

        rock.interaction = Interaction.NONE
        rock.image = resources.rock_water_image
        rock.group = self.foreground_underlay_layer

        self.environment_matrix[24 - y_pos][x_pos] = 0

        rock.hit_box.x = rock.x
        rock.hit_box.y = rock.y

        self.level_interactable_objects.remove(rock)
        self.sunk_rocks.append(rock)

    def update(self, dt):
        pass
        # self.hero.update(dt)
        # self.map.update(dt, self.hero)

    def draw(self):
        super().draw()

        """
        # DEBUG
        if DEBUG:
            pass
            #self.draw_env_bounds()
            # draw player pos dot
            #height = self.hero.height-14
            #rectangle = pyglet.shapes.Rectangle(self.hero.hit_box.x, self.hero.hit_box.y, self.hero.width, height, color=(255, 0, 0))
            #rectangle.opacity = 125
            #rectangle.draw()
        """
