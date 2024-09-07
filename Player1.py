from Player import Player
from Canon_Bullet import CanonBullet
from Riffle_Bullet import RiffleBullet
from Sniper_Bullet import SniperBullet
from Bullet import DefaultBullet
from Scattergun_Bullet import ScatterBullet
import pygame


# The red player character
class Player1(Player):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.all_weapon_types_sprites = []
        default_animations_list = []
        riffle_animation_list = []
        sniper_animation_list = []
        canon_animation_list = []
        scatter_animation_list = []

        # Default Weapon
        default_idle_list = []
        for i in range(5):
            img = pygame.image.load(f"Gunner_Red_Sprites/Gunner_Red_Idle/Gunner_Red_Idle{i}.png")
            img = pygame.transform.scale(img, (70, 85))
            default_idle_list.append(img)
        default_animations_list.append(default_idle_list)

        # Default Weapon
        default_run_list = []
        for i in range(6):
            img = pygame.image.load(f"Gunner_Red_Sprites/Gunner_Red_Run/Gunner_Red_Run{i}.png")
            img = pygame.transform.scale(img, (70, 85))
            default_run_list.append(img)
        default_animations_list.append(default_run_list)

        # Default Weapon
        default_jump_list = []
        for i in range(2):
            img = pygame.image.load(f"Gunner_Red_Sprites/Gunner_Red_Jump/Gunner_Red_Jump{i}.png")
            img = pygame.transform.scale(img, (70, 85))
            default_jump_list.append(img)
        default_animations_list.append(default_jump_list)

        self.all_weapon_types_sprites.append(default_animations_list)


        # Riffle Gun
        riffle_idle_list = []
        for i in range(5):
            img = pygame.image.load(f"Riffle_Red_Sprites/Riffle_Red_Idle/Riffle_Red_Idle{i}.png")
            img = pygame.transform.scale(img, (84, 85))
            riffle_idle_list.append(img)
        riffle_animation_list.append(riffle_idle_list)

        # Riffle Gun
        riffle_run_list = []
        for i in range(6):
            img = pygame.image.load(f"Riffle_Red_Sprites/Riffle_Red_Run/Riffle_Red_Run{i}.png")
            img = pygame.transform.scale(img, (84, 85))
            riffle_run_list.append(img)
        riffle_animation_list.append(riffle_run_list)

        # Riffle Gun
        riffle_jump_list = []
        for i in range(2):
            img = pygame.image.load(f"Riffle_Red_Sprites/Riffle_Red_Jump/Riffle_Red_Jump{i}.png")
            img = pygame.transform.scale(img, (84, 85))
            riffle_jump_list.append(img)
        riffle_animation_list.append(riffle_jump_list)

        self.all_weapon_types_sprites.append(riffle_animation_list)

        # Sniper Gun
        sniper_idle_list = []
        for i in range(5):
            img = pygame.image.load(f"Sniper_Red_Sprites/Sniper_Red_Idle/Sniper_Red_Idle{i}.png")
            img = pygame.transform.scale(img, (118, 85))
            sniper_idle_list.append(img)
        sniper_animation_list.append(sniper_idle_list)

        # Sniper Gun
        sniper_run_list = []
        for i in range(6):
            img = pygame.image.load(f"Sniper_Red_Sprites/Sniper_Red_Run/Sniper_Red_Run{i}.png")
            img = pygame.transform.scale(img, (118, 85))
            sniper_run_list.append(img)
        sniper_animation_list.append(sniper_run_list)

        # Sniper Gun
        sniper_jump_list = []
        for i in range(2):
            img = pygame.image.load(f"Sniper_Red_Sprites/Sniper_Red_Jump/Sniper_Red_Jump{i}.png")
            img = pygame.transform.scale(img, (118, 85))
            sniper_jump_list.append(img)
        sniper_animation_list.append(sniper_jump_list)

        self.all_weapon_types_sprites.append(sniper_animation_list)

        # Canon Gun
        canon_idle_list = []
        for i in range(5):
            img = pygame.image.load(f"Canon_Red_Sprites/Canon_Red_Idle/Canon_Red_Idle{i}.png")
            img = pygame.transform.scale(img, (106, 85))
            canon_idle_list.append(img)
        canon_animation_list.append(canon_idle_list)

        # Canon Gun
        canon_run_list = []
        for i in range(6):
            img = pygame.image.load(f"Canon_Red_Sprites/Canon_Red_Run/Canon_Red_Run{i}.png")
            img = pygame.transform.scale(img, (106, 85))
            canon_run_list.append(img)
        canon_animation_list.append(canon_run_list)

        # Canon Gun
        canon_jump_list = []
        for i in range(2):
            img = pygame.image.load(f"Canon_Red_Sprites/Canon_Red_Jump/Canon_Red_Jump{i}.png")
            img = pygame.transform.scale(img, (106, 85))
            canon_jump_list.append(img)
        canon_animation_list.append(canon_jump_list)

        self.all_weapon_types_sprites.append(canon_animation_list)

        # Scatter Gun
        scatter_idle_list = []
        for i in range(5):
            img = pygame.image.load(f"Scatter_Red_Sprites/Scatter_Red_Idle/Scatter_Red_Idle{i}.png")
            img = pygame.transform.scale(img, (86, 85))
            scatter_idle_list.append(img)
        scatter_animation_list.append(scatter_idle_list)

        # Scatter Gun
        scatter_run_list = []
        for i in range(6):
            img = pygame.image.load(f"Scatter_Red_Sprites/Scatter_Red_Run/Scatter_Red_Run{i}.png")
            img = pygame.transform.scale(img, (86, 85))
            scatter_run_list.append(img)
        scatter_animation_list.append(scatter_run_list)

        # Scatter Gun
        scatter_jump_list = []
        for i in range(2):
            img = pygame.image.load(f"Scatter_Red_Sprites/Scatter_Red_Jump/Scatter_Red_Jump{i}.png")
            img = pygame.transform.scale(img, (86, 85))
            scatter_jump_list.append(img)
        scatter_animation_list.append(scatter_jump_list)

        self.all_weapon_types_sprites.append(scatter_animation_list)

        # Set a variable to hold the current weapon sprites
        self.sprites = self.all_weapon_types_sprites[self.weapon_index]

        self.img = self.sprites[self.action_code][self.frame_index]

        self.rect = self.img.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.direction = 1

    # A method to move the player
    def moving(self,island_list,y_stand,y_land):
        x_change = 0
        y_change = 0

        if self.moving_left:
            x_change -= self.speed
            self.flip = True
            self.direction = -1
            if self.rect.x < 8:
                self.rect.x = 8
                x_change = 0
        if self.moving_right:
            x_change += self.speed
            self.flip = False
            self.direction = 1
            if self.rect.x > 1320:
                self.rect.x = 1320
                x_change = 0

        # Jump
        if self.jump_looping_time > 0:
            if self.jump == True and self.current_jump_times <= self.maximum_jump_times:
                self.jumping_factor = -10.5
                self.jump_looping_time -= 1
                if self.jump_looping_time <= 0:
                    self.jump = False
                    self.jump_looping_time = self.maximum_jump_times

        # Apply gravity
        self.jumping_factor += self.JUMPING_HEIGHT
        if self.jumping_factor > 10:
            self.jumping_factor = 10
        y_change += self.jumping_factor

        # check for collision with islands
        for island in island_list:

            # check for collision in x direction
            if island[1].colliderect(self.rect.x + x_change, self.rect.y + 25, 30, 40):
                x_change = 0
            # check for collision in y direction
            if island[1].colliderect(self.rect.x, self.rect.y + y_stand + y_change, 30, 40):
                # check if below the ground i.e. jumping
                if self.jumping_factor < 0:
                    y_change = island[1].bottom - self.rect.top
                    self.jumping_factor = 0

                # check if above the ground i.e. falling
                elif self.jumping_factor > 0:
                    y_change = island[1].top - self.rect.bottom
                    self.jumping_factor = 0
                    self.jump = False
                    self.current_jump_times = self.maximum_jump_times

            # Check collision with floor
            if self.rect.bottom + y_change > y_land:
                y_change = y_land - self.rect.bottom
                self.jump = False
                self.current_jump_times = self.maximum_jump_times

        self.rect.x += x_change
        if self.jumping_factor != 0:
            self.rect.y += y_change

    # Display the player into the screen
    def show_player(self, screen):
        if self.alive:
            screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)

    # Update the animation of the player
    def animation_update(self):
        cooldown = 100
        if self.alive:
            self.img = self.sprites[self.action_code][self.frame_index]
            # check if enough time has passed
            if pygame.time.get_ticks() - self.update_time > cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
                # if the animation runs out, reset it to start
                if self.frame_index == len(self.sprites[self.action_code]):
                    self.frame_index = 0

    # A method to shoot default bullet
    def shooting_default_bullet(self, default_bullet_group):
        if self.shoot_cool_down == 0 and self.bullet_limit > 0:
            self.shoot_cool_down = 20
            bullet = DefaultBullet(self.rect.centerx + (0.7 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            default_bullet_group.add(bullet)
            # reduce ammo
            self.bullet_limit -= 1

    # A method to shoot canon bullet
    def shooting_canon_bullet(self, canon_bullet_group):
        if self.shoot_cool_down == 0 and self.canon_limit > 0:
            self.shoot_cool_down = 120
            bullet = CanonBullet(self.rect.centerx + (0.7 * self.rect.size[0] * self.direction), self.rect.centery-7,
                                   self.direction)
            canon_bullet_group.add(bullet)
            # reduce ammo
            self.canon_limit -= 1

    # A method to shoot riffle bullet
    def shooting_riffle_bullet(self, riffle_bullet_group):
        if self.shoot_cool_down == 0 and self.riffle_limit > 0:
            self.shoot_cool_down = 25
            bullet = RiffleBullet(self.rect.centerx + (0.7 * self.rect.size[0] * self.direction), self.rect.centery-7,
                                   self.direction)
            riffle_bullet_group.add(bullet)
            # reduce ammo
            self.riffle_limit -= 1

    # A method to shoot scatter bullet
    def shooting_scatter_bullet(self, scatter_bullet_group):
        if self.shoot_cool_down == 0 and self.riffle_limit > 0:
            self.shoot_cool_down = 45
            bullet = ScatterBullet(self.rect.centerx + (0.7 * self.rect.size[0] * self.direction), self.rect.centery-7,
                                   self.direction)
            scatter_bullet_group.add(bullet)
            # reduce ammo
            self.scatter_limit -= 1

    # A method to shoot sniper bullet
    def shooting_sniper_bullet(self, sniper_bullet_group):
        if self.shoot_cool_down == 0 and self.sniper_limit > 0:
            self.shoot_cool_down = 55
            bullet = SniperBullet(self.rect.centerx + (0.7 * self.rect.size[0] * self.direction), self.rect.centery-16,
                                   self.direction)
            sniper_bullet_group.add(bullet)
            # reduce ammo
            self.sniper_limit -= 1

    # Update the weapon of the player
    def update_weapon(self, new_weapon_index):
        if self.alive:
            self.weapon_index = new_weapon_index
            self.sprites = self.all_weapon_types_sprites[self.weapon_index]

    # A method to display the total loves of the player
    def display_total_lives(self, screen):
        img = pygame.image.load("Player_total_lives.png")
        lives_img = pygame.transform.scale(img, (20, 20))
        for i in range(1, self.total_lives+1):
            screen.blit(lives_img, (30*i+40, 20))

    # A method to display the total bullet number into the screen
    def display_bullet_numbers(self, screen):
        font = pygame.font.SysFont(None, 25)
        img = pygame.image.load("Bullet_Total_Numbees.png")
        bullets_img = pygame.transform.scale(img, (20, 25))
        if self.weapon_index == 0:
            screen.blit(bullets_img, (80, 70))
            default_message = font.render("UNLIMITED", True, (232, 64, 225))
            screen.blit(default_message, (100, 75))
        elif self.weapon_index == 1:
            screen.blit(bullets_img, (80, 70))
            riffle_message = font.render(f"x{self.riffle_limit}", True, (232, 64, 225))
            screen.blit(riffle_message, (95, 75))
        elif self.weapon_index == 2:
            screen.blit(bullets_img, (80, 70))
            sniper_message = font.render(f"x{self.sniper_limit}", True, (232, 64, 225))
            screen.blit(sniper_message, (95, 75))
        elif self.weapon_index == 3:
            screen.blit(bullets_img, (80, 70))
            canon_message = font.render(f"x{self.canon_limit}", True, (232, 64, 225))
            screen.blit(canon_message, (95, 75))
        elif self.weapon_index == 4:
            screen.blit(bullets_img, (80, 70))
            scatter_message = font.render(f"x{self.scatter_limit}", True, (232, 64, 225))
            screen.blit(scatter_message, (95, 75))

    # Display the total grenade number into the screen
    def display_grenade_numbers(self, screen):
        img = pygame.image.load("Grenade_Count.png")
        grenade_img = pygame.transform.scale(img, (20, 25))
        for i in range(1, self.grenade_total+1):
            screen.blit(grenade_img, (20 * i + 180, 70))

    # Display the maximum jumping times allowed into the screen
    def display_jumping_times(self, screen):
        font = pygame.font.SysFont(None, 25)
        jump_message = font.render(f"{self.maximum_jump_times} x", True, (224, 0, 224))
        screen.blit(jump_message, (30, 10))

