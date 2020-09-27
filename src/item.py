class Item:
    def __init__(self, parent):
        self.x = parent.x
        self.y = parent.y
        self.moving = parent.moving
        self.facing = parent.facing

    def update(dt, moving, facing, xdiff, ydiff):
        pass
