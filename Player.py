# Create the Parent Player Class
import pygame
import time
import re
from abc import ABC
from Player_Explosion import PlayerExplosion
from pygame import mixer


# The parent, abstract class for the player
class Player(pygame.sprite.Sprite, ABC):

    # Constant to be the jumping factor
    JUMPING_HEIGHT = 0.65

    # Constructor for the Player parent class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.weapon_index = 0
        self.alive = True
        self.current_jump_times = 2
        self.maximum_jump_times = 2
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.action_code = 0
        self.jump = False
        self.jumping_factor = 0
        self.speed = 10
        self.flip = False
        self.moving_left = False
        self.moving_right = False
        self.maximum_living_time = 0.0
        self.total_lives = 6
        self.shoot_cool_down = 0
        self.health = 100
        self.shoot_cool_down = 0
        self.bullet_limit = 1000000
        self.is_shooting = False
        self.is_grenade = False
        self.grenade_thrown = False
        self.grenade_total = 2
        self.canon_limit = 3
        self.sniper_limit = 3
        self.riffle_limit = 20
        self.scatter_limit = 7
        self.jump_looping_time = self.maximum_jump_times
        self.player_explosion_time = 1
        self.is_tracking_time = True
        self.start_time = 0.0
        self.total_lives_copy = 6
        self.play_sounds_check = True
        self.is_on_block = False
        self.is_explode = False

    # A method to update the moving sprites
    def update_action(self, new_action):
        # Check if the new action is different to the new one
        if self.alive:
            if new_action != self.action_code:
                self.action_code = new_action
                # update animation setting
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
        else:
            self.moving_left = False
            self.moving_right = False

    # Update all the features of the player
    def update_all(self, players_explosion_group):
        self.animation_update()
        self.check_alive(players_explosion_group)
        # Update cooldown
        if self.shoot_cool_down > 0:
            self.shoot_cool_down -= 1

    # Checking the living condition of the player
    def check_alive(self, players_explosion_group):
        if self.health <= 0 and self.total_lives == 0:
            self.health = 0
            self.speed = 0
            self.alive = False
        if not self.alive:
            if self.player_explosion_time == 1:
                explosion_music = mixer.Sound("man dead.mp3")
                explosion_music.play()
                player_explosion = PlayerExplosion(self.rect.x, self.rect.y)
                players_explosion_group.add(player_explosion)
                self.player_explosion_time -= 1
            self.is_explode = True

    # Reset all the weapon bullets numbers before updating an weapon
    def update_weapon_bullets(self):
        self.canon_limit = 3
        self.sniper_limit = 3
        self.riffle_limit = 20
        self.scatter_limit = 7

    # Am method to track the living time maximum for the player
    def track_living_time(self):
        if self.is_tracking_time:
            start_time = time.time()
            self.start_time = start_time
            self.is_tracking_time = False
        if self.total_lives < self.total_lives_copy:
            end_time = time.time()
            current_living_time = end_time - self.start_time
            if current_living_time > self.maximum_living_time:
                self.maximum_living_time = self.__time_format(current_living_time)
            self.is_tracking_time = True
            self.total_lives_copy -= 1

    # A method to format the time
    def __time_format(self, num):
        return float(re.sub(r'^(\d+\.\d{,2})\d*$', r'\1', str(num)))

    # A method to display the jumping limit into the screen
    def display_jumping_times(self):
        pass

    # A method to display the total lives into the screen
    def display_total_lives(self, screen):
        pass

    # A method to update the animation
    def animation_update(self):
        pass

    # A method to move the player
    def moving(self,island_list,y_land):
        pass

    # A method to show the player into the screen
    def show_player(self):
        pass

    # A method to display total bullet numbers into the screen
    def display_bullet_numbers(self, screen):
        pass

    # A method to display the grenade numbers
    def display_grenade_numbers(self):
        pass





