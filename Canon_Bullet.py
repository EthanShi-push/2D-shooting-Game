import pygame
from Canon_Explosion import CanonExplosion
from pygame import mixer


class CanonBullet(pygame.sprite.Sprite):
    bullet_image_right = pygame.image.load("Canon_Bullet/Canon_Bullet_Right.png")
    bullet_image_right = pygame.transform.scale(bullet_image_right, (45, 25))

    bullet_image_left = pygame.image.load("Canon_Bullet/Canon_Bullet_Left.png")
    bullet_image_left = pygame.transform.scale(bullet_image_left, (45, 25))

    """ the constructor of this class set the speed and the damage of the cannon bullet,
    it also set or gain all the attributes which will be using in this class
    :parameter
    direction: indicates which direction should the bullet goes
    x:set the x value of rectangle center
    y: set the y value of the rectangle center
    """
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = CanonBullet.bullet_image_right
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.pulse_factor = 80
        self.damage = 60
        self.plays_sounds = True
        self.running_time = 1
        self.direction_copy = "None"

    # update the movement of cannon bullet
    def update(self, player, another_player, player_bullet_group, canon_explosion_group):
        canon_bullet_sound = mixer.Sound("Canon_Shooting.mp3")
        if self.plays_sounds:
            canon_bullet_sound.play()
            self.plays_sounds = False
        if self.direction == -1:
            self.image = CanonBullet.bullet_image_left

        self.rect.x += self.direction * self.speed

        # check if bullet gone out of screen
        if self.rect.right < 0 or self.rect.left > 1400:
            self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(player, player_bullet_group, False):
            if player.alive:
                player.health -= self.damage
                canon_bullet_sound.stop()
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
                    else:
                        player.rect.x += self.pulse_factor
                elif self.direction_copy == "Left":
                    if player.rect.x - self.pulse_factor <= 8:
                        player.rect.x = 8
                    else:
                        player.rect.x -= self.pulse_factor
                canon_explosion = CanonExplosion(player.rect.x, self.rect.y-20)
                canon_explosion_group.add(canon_explosion)

        if pygame.sprite.spritecollide(another_player, player_bullet_group, False):
            if another_player.alive:
                another_player.health -= self.damage
                canon_bullet_sound.stop()
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
                    else:
                        another_player.rect.x += self.pulse_factor
                if self.direction_copy == "Left":
                    if another_player.rect.x - self.pulse_factor <= 8:
                        another_player.rect.x = 8
                    else:
                        another_player.rect.x -= self.pulse_factor
                canon_explosion = CanonExplosion(another_player.rect.x, self.rect.y-20)
                canon_explosion_group.add(canon_explosion)




