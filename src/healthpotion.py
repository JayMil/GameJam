import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction

class HealthPotion(PhysicalSpriteObject):
    ''' A physical sprite object '''
    def __init__(self, x, y, window, group, batch, interaction=Interaction.NONE, img=resources.health_potion, *args, **kwargs):
        super().__init__(window=window, group=group, batch=batch, interaction=interaction, img=img)

        self.x = x
        self.y = y
        self.hit_box.x = x
        self.hit_box.y = y