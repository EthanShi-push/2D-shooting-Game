import pygame
from Scatter_Explosion import ScatterExplosion
from pygame import mixer


class ScatterBullet(pygame.sprite.Sprite):
    bullet_image_right = pygame.image.load("Scatter_Bullet/Scattergun_Right.png")
    bullet_image_right = pygame.transform.scale(bullet_image_right, (28, 15))

    bullet_image_left = pygame.image.load("Scatter_Bullet/Scattergun_Left.png")
    bullet_image_left = pygame.transform.scale(bullet_image_left, (28, 15))

    """ the constructor of this class set the speed and the damage of the scatter bullet,
    it also set or gain all the attributes which will be using in this class
    :parameter
    direction: indicates which direction should the bullet goes
    x:set the x value of rectangle center
    y: set the y value of the rectangle center
    """
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 25
        self.image = ScatterBullet.bullet_image_right
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.pulse_factor = 10
        self.damage = 12
        self.plays_sound = True
        self.running_time = 1
        self.direction_copy = "None"

    # update the movement of the bullet
    def update(self, player, another_player, player_bullet_group, scatter_explosion_group):
        scatter_bullet_sound = mixer.Sound("Scatter_Shooting.mp3")
        if self.plays_sound:
            scatter_bullet_sound.play()
            self.plays_sound = False

        if self.direction == -1:
            self.image = ScatterBullet.bullet_image_left

        self.rect.x += self.direction * self.speed

        # check if bullet gone out of screen
        if self.rect.right < 0 or self.rect.left > 1400:
            self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(player, player_bullet_group, False):
            if player.alive:
                player.health -= self.damage
                scatter_bullet_sound.stop()
                self.kill()
                if player.health <= 0 and player.total_lives > 0:
                    player.total_lives -= 1
                    player.health = 100
                if player.total_lives == 0:
                    player.alive = False
                    player.health = 0
                if self.running_time == 1:
                    if self.direction == 1:
                        self.direction_copy = "Right"
                    elif self.direction == -1:
                        self.direction_copy = "Left"
                    self.running_time -= 1
                if self.direction_copy == "Right":
                    if player.rect.x + self.pulse_factor >= 1320:
                        player.rect.x = 1320
                        player.rect.y -= self.pulse_factor * 3
                    else:
                        player.rect.x += self.pulse_factor
                        player.rect.y -= self.pulse_factor * 3
                elif self.direction_copy == "Left":
                    if player.rect.x - self.pulse_factor <= 8:
                        player.rect.x = 8
                        player.rect.y -= self.pulse_factor * 3
                    else:
                        player.rect.x -= self.pulse_factor
                        player.rect.y -= self.pulse_factor * 3
                scatter_explosion = ScatterExplosion(self.rect.x+15, self.rect.y+10)
                scatter_explosion_group.add(scatter_explosion)

        # if pygame.sprite.spritecollide(another_player, another_player_bullet_group, False):
        if pygame.sprite.spritecollide(another_player, player_bullet_group, False):
            if another_player.alive:
                another_player.health -= self.damage
                scatter_bullet_sound.stop()
                self.kill()
                if another_player.health <= 0 and another_player.total_lives > 0:
                    another_player.total_lives -= 1
                    another_player.health = 100
                if another_player.total_lives == 0:
                    another_player.alive = False
                    another_player.health = 0
                if self.running_time == 1:
                    if self.direction == 1:
                        self.direction_copy = "Right"
                    elif self.direction == -1:
                        self.direction_copy = "Left"
                    self.running_time -= 1
                if self.direction_copy == "Right":
                    if another_player.rect.x + self.pulse_factor >= 1320:
                        another_player.rect.x = 1320
                        another_player.rect.y -= self.pulse_factor * 3
                    else:
                        another_player.rect.x += self.pulse_factor
                        another_player.rect.y -= self.pulse_factor * 3
                if self.direction_copy == "Left":
                    if another_player.rect.x - self.pulse_factor <= 8:
                        another_player.rect.x = 8
                        another_player.rect.y -= self.pulse_factor * 3
                    else:
                        another_player.rect.x -= self.pulse_factor
                        another_player.rect.y -= self.pulse_factor * 3
                scatter_explosion = ScatterExplosion(self.rect.x+15, self.rect.y+10)
                scatter_explosion_group.add(scatter_explosion)



