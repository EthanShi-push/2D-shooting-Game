import pygame


class SpriteSheet(object):
    def __init__(self, image):
        self.sprite = image

    def get_image(self, frame, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (80, 67))
        return image
