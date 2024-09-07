import pygame


# The class to display the health bar of the red player and the yellow player
class HealthBar(object):
    RED = (255, 32, 32)
    GREEN = (60, 255, 32)
    ORANGE = (255, 176, 96)

    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        image1 = pygame.image.load("Player1_Helmet.png")
        self.player1_image = pygame.transform.scale(image1, (60, 60))
        image2 = pygame.image.load("Player2_Helmet.png")
        self.player2_image = pygame.transform.scale(image2, (60, 60))

    def draw(self, health, screen):
        # update with new health
        self.health = health
        # calculate ratio
        ratio = self.health / self.max_health

        pygame.draw.rect(screen, HealthBar.ORANGE, (18, 30, 54, 44))
        pygame.draw.rect(screen, HealthBar.ORANGE, (1328, 30, 54, 44))

        screen.blit(self.player1_image, (15, 30))
        screen.blit(self.player2_image, (1325, 30))

        pygame.draw.rect(screen, HealthBar.ORANGE, (self.x-2, self.y-2, 154, 24))
        pygame.draw.rect(screen, HealthBar.RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, HealthBar.GREEN, (self.x, self.y, 150*ratio, 20))