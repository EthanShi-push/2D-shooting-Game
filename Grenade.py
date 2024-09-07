import pygame
from Explosion import Explosion
from pygame import mixer


# A class for Red player to throw the grenade
class Grenade1(pygame.sprite.Sprite):
    player1_grenade = pygame.image.load("player1_grenade.png")
    another_player_grenade = pygame.image.load("player2_grenade.png")
    falling_factor = 0.65

    def __init__(self, x_pos, y_pos, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 42
        self.y_change = -11  # vertical speed
        self.speed = 11  # horizontal speed
        self.pulse_factor = 85
        self.sound_check = True

        player1_grenade = pygame.transform.scale(Grenade1.player1_grenade, (26, 30))

        self.image = player1_grenade
        self.rect = self.image.get_rect()

        self.rect.center = (x_pos, y_pos)
        self.direction = direction

    # The method to display the grenade into the screen
    def update(self, player1, player2, explosion_group, map_selection):
        grenade_bullet_sound = mixer.Sound("Grenade_Shooting.mp3")
        grenade_explosion_sound = mixer.Sound("Grenade_Explosion.mp3")
        if self.sound_check:
            grenade_bullet_sound.play()
            self.sound_check = False
        self.y_change += Grenade1.falling_factor

        x_change = self.direction * self.speed
        y_final = self.y_change

        if map_selection == "Sky":
            if self.rect.bottom + y_final > 780:
                y_final = 780 - self.rect.bottom
                x_change = 0
        else:
            # Checking collision with the floor
            if self.rect.bottom + y_final > 640:
                y_final = 640 - self.rect.bottom
                x_change = 0

        # check if grenade gone out of screen
        if self.rect.left + x_change < 0 or self.rect.right + x_change > 1400:
            self.kill()

        # Update grenade position
        self.rect.x += x_change
        self.rect.y += y_final

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            grenade_explosion_sound.play()
            grenade_explosion = Explosion(self.rect.x, self.rect.y)
            explosion_group.add(grenade_explosion)

            # do damage to anyone that is near by
            # Check for player1 and player2
            if abs(self.rect.centerx - player2.rect.centerx) < 30 * 2 and abs(
                    self.rect.centery - player2.rect.centery):
                player2.health -= 30
                player2.jump = False
                if player2.health <= 0 and player2.total_lives > 0:
                    player2.total_lives -= 1
                    player2.health = 100
                if player2.total_lives == 0:
                    player2.alive = False
                player2.rect.y -= self.pulse_factor * 2

