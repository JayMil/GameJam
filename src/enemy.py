from enum import Enum
import pyglet

import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction
from race import Race, Facing


class Enemy(Race):
    """ Enemy Sprite Class """

    def __init__(self, x=20, y=200, health=5, target=None, *args, **kwargs):
        super().__init__(
            race_images=resources.EnemyImages(),
            speed=0.5,
            x=x,
            y=y,
            health=health,
            *args,
            **kwargs
        )

        self.target = target

        self.pattern = [Facing.LEFT, Facing.RIGHT]

        self.pattern_pos = 0

        # adjust hit box height
        # print(self.height)
        # self.hit_box.height -= 55

    def update(self, dt):

        if not self.target:
            self.pattern_pos += 1
            if self.pattern[self.pattern_pos % len(self.pattern)] == Facing.LEFT:
                self.target = CollisionObject(
                    self.x - 100, self.y, 1, 1, Interaction.BLOCKING
                )
            else:
                self.target = CollisionObject(
                    self.x + 100, self.y, 1, 1, Interaction.BLOCKING
                )
                # def __init__(self, x, y, height, width, interaction, group=None, batch=None, color=(255,255,255)):

        if not self.hit_box.collides_with(self.target):
            xmov = self.target.x - self.x
            ymov = self.target.y - self.y

            absxmov = abs(xmov)
            absymov = abs(ymov)

            if absymov == 0:
                self.move_x(xmov, absxmov)
            elif absxmov == 0:
                self.move_y(ymov, absymov)
            elif absxmov < absymov:
                self.move_x(xmov, absxmov)
            else:
                self.move_y(ymov, absymov)

        if self.current_speed == 0:
            if self.image == self.race_images.walk_up:
                self.image = self.race_images.face_up
            elif self.image == self.race_images.walk_down:
                self.image = self.race_images.face_down
            elif self.image == self.race_images.walk_left:
                self.image = self.race_images.face_left
            elif self.image == self.race_images.walk_right:
                self.image = self.race_images.face_right

        # self.moving.push(self.pattern[self.pattern_pos%len(self.pattern)])
        # self.moving.push(Facing.LEFT)
        super().update(dt)
        if self.moving:
            self.moving.pop()

    def move_y(self, ymov, absymov):
        self.current_speed = self.speed
        if absymov < self.speed:
            self.current_speed = absymov

        if ymov < 0:
            self.moving.push(Facing.DOWN)
        else:
            self.moving.push(Facing.UP)

    def move_x(self, xmov, absxmov):
        self.current_speed = self.speed
        if absxmov < self.speed:
            self.current_speed = absxmov

        if xmov < 0:
            self.moving.push(Facing.LEFT)
        else:
            self.moving.push(Facing.RIGHT)
