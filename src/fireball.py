import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction


class Fireball(PhysicalSpriteObject):
    """ A physical sprite object """

    def __init__(
        self,
        x,
        y,
        x_addition,
        y_addition,
        window,
        group,
        batch,
        interaction=Interaction.MOVABLE,
        *args,
        **kwargs
    ):
        super().__init__(
            window=window,
            group=group,
            batch=batch,
            interaction=interaction,
            img=resources.FireballImages().fireball_animation,
        )

        self.x = x
        self.y = y
        self.x_addition = x_addition
        self.y_addition = y_addition
        self.hit_box.x = self.x
        self.hit_box.y = self.y
        self.interaction = interaction

        self.hit_box.width = 16
        self.hit_box.height = 16

        def update(self, dt):
            self.x += 10
            self.hit_box.x = self.x
