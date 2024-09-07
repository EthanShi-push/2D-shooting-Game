import pygame


# This is a class to display a player explode effect when one of the player loses all it live
class PlayerExplosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_list = []

        for num in range(10):
            img = pygame.image.load(f"Player_Explosion/Player_Explosion{num}.png")
            img = pygame.transform.scale(img, (150, 170))
            self.explosion_list.append(img)

        self.explosion_index = 0
        self.image = self.explosion_list[self.explosion_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0  # cool down

    # Display the explosion animation into the screen
    def update(self):
        explosion_speed = 10

        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed:
            self.counter = 0
            self.explosion_index += 1

            # check if the explosion complete
            if self.explosion_index >= len(self.explosion_list):
                self.kill()
            else:
                self.image = self.explosion_list[self.explosion_index]

