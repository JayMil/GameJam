class CollisionObject():
    
    ''' Generic collision object class '''
    def __init__(self, x, y, height, width, interaction):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.interaction = interaction

    def collides_with(self, other_object):
        # rectangle collision
        x1 = self.x
        y1 = self.y
        x2 = other_object.x
        y2 = other_object.y

        if (x1 < x2 + other_object.width and
           x1 + self.width > x2 and
           y1 < y2 + other_object.height and
           y1 + self.height > y2):
            return True
        else:
            return False

class InteractionEnum(Enum):
    BLOCKING = 1
    MOVABLE = 2
    NONE = 3