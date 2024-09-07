import pygame


# A class to handle the explosion of grenade into the screen
class Explosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_list = []

        for num in range(1, 6):
            img = pygame.image.load(f"Grenade Explosion/exp{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (110, 110))
            self.explosion_list.append(img)

        self.explosion_index = 0
        self.image = self.explosion_list[self.explosion_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0  # cool down

    # A method to display the update the explosion of the grenade
    def update(self):
        explosion_speed = 4

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
