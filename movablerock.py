
import resources
from physicalspriteobject import PhysicalSpriteObject
from collisionobject import Interaction

class MovableRock(PhysicalSpriteObject):
    ''' A physical sprite object '''
    def __init__(self, x, y, window, group, batch, interaction=Interaction.MOVABLE, img=resources.rock_image, *args, **kwargs):
        super().__init__(window=window, group=group, batch=batch, interaction=interaction, img=img)

        self.x = x
        self.y = y

        
