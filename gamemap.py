import pyglet

class GameMap():
    def __init__(self, window, batch, group):
        self.window = window
        self.batch = batch
        self.group = group
        self.create_background()
        self.environment_objs = self.create_environment()


    def create_environment(self):
        """ Create object in environment """
        objs = []
        return objs

    def create_background(self):
        ''' Create sprite for the background image '''
        self.background_image = pyglet.sprite.Sprite(img="rescoures.Map_1_Bound", 
                                            batch=self.batch, group=self.group, 
                                            x=0, y=0)



    def handle_enviornment_collisions(self,hero):
        """ Detect and handle collisions with object and enviornment"""
        pass

    def update(self, dt):
        pass
   

