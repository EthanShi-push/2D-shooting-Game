import pygame


# This class handle the explosion of the riffle bullet
class RiffleExplosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_list = []

        for num in range(4):
            img = pygame.image.load(f"Riffle Explosion/Riffle_Explosion{num}.png")
            img = pygame.transform.scale(img, (20, 20))
            self.explosion_list.append(img)

        self.explosion_index = 0
        self.image = self.explosion_list[self.explosion_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0  # cool down

    # This method update the explosion effect into the screen
    def update(self):
        explosion_speed = 2

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

