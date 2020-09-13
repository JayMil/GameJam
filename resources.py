import pyglet

def center_image(image):
    """ Sets an image's anchor point to its center """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['resources']
pyglet.resource.reindex()



# animation example
'''
explosion_image = pyglet.resource.image("explosion.png")
explosion_seq = pyglet.image.ImageGrid(explosion_image, 4, 5)
explosion_seq1 = explosion_seq[5:9] + explosion_seq[:4]
explosion_seq2 = explosion_seq[15:] + explosion_seq[11:14]
'''


# slash_image = pyglet.resource.image("weapons_1.png")
health_bar_heart_empty = pyglet.resource.image("health_bar_heart_empty.png")
health_bar_heart = pyglet.resource.image("health_bar_heart.png")
heart_holder = pyglet.resource.image("heart_holder.png")
backpack_inventory = pyglet.resource.image("backpack_inventory.png")
health_potion = pyglet.resource.image("health_potion.png")

background_image = pyglet.resource.image("Map_1_Bound.png")
rock_image = pyglet.resource.image("Normal_Rock.png")
pink_rock_image = pyglet.resource.image("Pink_Rock.png")
blue_rock_image = pyglet.resource.image("Blue_Rock.png")
yellow_rock_image = pyglet.resource.image("Yellow_Rock.png")
rock_water_image = pyglet.resource.image("Rock_In_Water.png")

character_image = pyglet.resource.image("Character.png")
character_seq = pyglet.image.ImageGrid(character_image, 4, 3)
character_seq_walk_up = character_seq[:2]
character_seq_walk_right = character_seq[3:5]
character_seq_walk_left = character_seq[6:8]
character_seq_walk_down = character_seq[9:11]

character_face_up = character_seq[1]
character_face_right = character_seq[4]
character_face_left = character_seq[7]
character_face_down = character_seq[10]


class HeroImages():
    def __init__(self):
        self.walk_up = pyglet.image.Animation.from_image_sequence(character_seq_walk_up, duration=0.1,loop=True)
        self.walk_down = pyglet.image.Animation.from_image_sequence(character_seq_walk_down, duration=0.1,loop=True)
        self.walk_left = pyglet.image.Animation.from_image_sequence(character_seq_walk_left, duration=0.1,loop=True)
        self.walk_right = pyglet.image.Animation.from_image_sequence(character_seq_walk_right, duration=0.1,loop=True)

        self.face_up = character_face_up
        self.face_down = character_face_down
        self.face_left = character_face_left
        self.face_right = character_face_right

        '''

        self.slash = pyglet.image.Animation.from_image_sequence(slash_seq1, duration=0.05,loop=False)

        #self.sword = sword_image
        self.sword = pyglet.image.Animation.from_image_sequence(sword_seq, duration=0.1,loop=True)
        self.sword_still = sword_still

        '''

