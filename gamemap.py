import pyglet
import resources

import collisionobject
from collisionobject import CollisionObject
from collisionobject import Interaction

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

        # border_object_1 = CollisionObject(x=0, y=0, height=32, width=32, interaction=Interaction.BLOCKING)
        # border_object_2 = CollisionObject(x=0, y=0, height=32, width=32, interaction=Interaction.BLOCKING)
        # border_object_3 = CollisionObject(x=0, y=0, height=32, width=32, interaction=Interaction.BLOCKING)
        # border_object_4 = CollisionObject(x=0, y=0, height=32, width=32, interaction=Interaction.BLOCKING)

        objs.append(border_object_1)


        return objs

    def create_background(self):
        ''' Create sprite for the background image '''
        self.background_image = pyglet.sprite.Sprite(img=resources.background_image, 
                                            batch=self.batch, group=self.group, 
                                            x=0, y=0)



    def handle_enviornment_collisions(self,hero):
        """ Detect and handle collisions with object and enviornment"""
        pass

    def update(self, dt):
        pass
   

