import pygame
from pygame import mixer


# Default Bullet deals will all the information and action regarding the default weapon bullet
class DefaultBullet(pygame.sprite.Sprite):
    bullet_image_right = pygame.image.load("Default_Bullet/Default_Bullet.png")
    bullet_image_right = pygame.transform.scale(bullet_image_right, (24, 23))

    bullet_image_left = pygame.image.load("Default_Bullet/Default_Bullet2.png")
    bullet_image_left = pygame.transform.scale(bullet_image_left, (24, 23))

    """ the constructor of this class set the speed and the damage of the default weapon,
    it also set or gain all the attributes which will be using in this class
    :parameter
    direction: indicates which direction should the bullet goes
    x:set the x value of rectangle center
    y: set the y value of the rectangle center
    """
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = DefaultBullet.bullet_image_right
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.damage = 5
        self.plays_sounds = True

    # update bullet movement
    def update(self, player, another_player, player_bullet_group):
        default_bullet_sound = mixer.Sound("Default_Shooting.mp3")
        if self.plays_sounds:
            default_bullet_sound.play()
            self.plays_sounds = False
        if self.direction == -1:
            self.image = DefaultBullet.bullet_image_left

        self.rect.x += self.direction * self.speed

        # check if bullet gone out of screen
        if self.rect.right < 0 or self.rect.left > 1400:
            self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(player, player_bullet_group, False):
            if player.alive:
                player.health -= self.damage
                default_bullet_sound.stop()
                self.kill()
                if player.health <= 0 and player.total_lives > 0:
                    player.total_lives -= 1
                    player.health = 100
                if player.total_lives == 0:
                    player.alive = False
                    player.health = 0

        # if pygame.sprite.spritecollide(another_player, another_player_bullet_group, False):
        if pygame.sprite.spritecollide(another_player, player_bullet_group, False):
            if another_player.alive:
                another_player.health -= self.damage
                default_bullet_sound.stop()
                self.kill()
                if another_player.health <= 0 and another_player.total_lives > 0:
                    another_player.total_lives -= 1
                    another_player.health = 100
                if another_player.total_lives == 0:
                    another_player.alive = False
                    another_player.health = 0
