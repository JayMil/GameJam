import pyglet


def center_image(image):
    """ Sets an image's anchor point to its center """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ["resources"]
pyglet.resource.reindex()


# animation example
"""
explosion_image = pyglet.resource.image("explosion.png")
explosion_seq = pyglet.image.ImageGrid(explosion_image, 4, 5)
explosion_seq1 = explosion_seq[5:9] + explosion_seq[:4]
explosion_seq2 = explosion_seq[15:] + explosion_seq[11:14]
"""


# slash_image = pyglet.resource.image("weapons_1.png")
health_bar_heart_empty = pyglet.resource.image("health_bar_heart_empty.png")
health_bar_heart = pyglet.resource.image("health_bar_heart.png")
heart_holder = pyglet.resource.image("heart_holder.png")
backpack_inventory = pyglet.resource.image("backpack_inventory.png")
health_potion = pyglet.resource.image("health_potion.png")

background_image = pyglet.resource.image("Map1.png")
rock_image = pyglet.resource.image("Normal_Rock.png")
fireball_image = pyglet.resource.image("Fire_Ball.png")
pink_rock_image = pyglet.resource.image("Pink_Rock.png")
blue_rock_image = pyglet.resource.image("Blue_Rock.png")
yellow_rock_image = pyglet.resource.image("Yellow_Rock.png")
rock_water_image = pyglet.resource.image("Rock_In_Water.png")

character_image = pyglet.resource.image("Character2.png")
enemy_image = pyglet.resource.image("Dragons.png")
character_attack_image = pyglet.resource.image("Sword_Animations.png")


class CharacterSeq:
    def __init__(self, image):
        self.seq = pyglet.image.ImageGrid(image, 4, 3)
        self.seq_walk_up = self.seq[:3]
        self.seq_walk_right = self.seq[3:6]
        self.seq_walk_left = self.seq[6:9]
        self.seq_walk_down = self.seq[9:12]

        self.face_up = self.seq[1]
        self.face_right = self.seq[4]
        self.face_left = self.seq[7]
        self.face_down = self.seq[10]


class RaceImages:
    def __init__(self, image):
        character_seq = CharacterSeq(image)
        self.walk_up = pyglet.image.Animation.from_image_sequence(
            character_seq.seq_walk_up, duration=0.1, loop=True
        )
        self.walk_down = pyglet.image.Animation.from_image_sequence(
            character_seq.seq_walk_down, duration=0.1, loop=True
        )
        self.walk_left = pyglet.image.Animation.from_image_sequence(
            character_seq.seq_walk_left, duration=0.1, loop=True
        )
        self.walk_right = pyglet.image.Animation.from_image_sequence(
            character_seq.seq_walk_right, duration=0.1, loop=True
        )

        self.face_up = character_seq.face_up
        self.face_down = character_seq.face_down
        self.face_left = character_seq.face_left
        self.face_right = character_seq.face_right


class HeroImages(RaceImages):
    def __init__(self, *args, **kwargs):
        super().__init__(image=character_image, *args, **kwargs)

        self.seq_attack = pyglet.image.ImageGrid(character_attack_image, 4, 3)
        self.seq_attack_up = self.seq_attack[:3]
        self.seq_attack_right = self.seq_attack[3:6]
        self.seq_attack_left = self.seq_attack[6:9]
        self.seq_attack_down = self.seq_attack[9:12]

        self.attack_up = pyglet.image.Animation.from_image_sequence(
            self.seq_attack_up, duration=0.1, loop=True
        )
        self.attack_down = pyglet.image.Animation.from_image_sequence(
            self.seq_attack_down, duration=0.1, loop=True
        )
        self.attack_left = pyglet.image.Animation.from_image_sequence(
            self.seq_attack_left, duration=0.1, loop=True
        )
        self.attack_right = pyglet.image.Animation.from_image_sequence(
            self.seq_attack_right, duration=0.1, loop=True
        )

        """

        self.slash = pyglet.image.Animation.from_image_sequence(slash_seq1, duration=0.05,loop=False)

        #self.sword = sword_image
        self.sword = pyglet.image.Animation.from_image_sequence(sword_seq, duration=0.1,loop=True)
        self.sword_still = sword_still

        """


class EnemyImages(RaceImages):
    def __init__(self, *args, **kwargs):
        super().__init__(image=enemy_image, *args, **kwargs)


class FireballImages:
    def __init__(self, *args, **kwargs):
        self.fireball_seq = pyglet.image.ImageGrid(fireball_image, 1, 8)
        self.fireball_animation = pyglet.image.Animation.from_image_sequence(
            self.fireball_seq, duration=0.1, loop=True
        )
