import pygame
import time
from Forest import Forest
from Button import Button
from Sky import Sky
from Arctic import ArcticMap
from pygame import mixer
import re
from Player1 import Player1
from Player2 import Player2
from Grenade import Grenade1
from Grenade2 import Grenade2
from HealthBar import HealthBar
import random

pygame.init()
screen_width = 1400
screen_height = 800
playerBoundary_y = screen_height - 650

font = pygame.font.Font("font/CartooNature.ttf", 27)

# Initialize some colour variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (170, 0, 0)
light_red = (255, 0, 0)
green = (0, 155, 0)
light_green = (0, 255, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
blue = (105, 89, 246)
light_blue = (35, 13, 233)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Twins Fight")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

# Creating Map objects
sky = Sky()
forest = Forest()
arctic = ArcticMap()
map_list = [forest, sky, arctic]

general_clock = pygame.time.Clock()
FPS = 60

# Loading Music
intro_music = mixer.Sound("Intro_Music.mp3")
intro_music.play(-1)
explosion_music = mixer.Sound("man dead.mp3")

# Loading fonts
intro_title_font = pygame.font.Font("font/BuffaloInline2Grunge.otf", 75)
map_selection_title_font = pygame.font.Font("font/Carnevalee Freakshow.ttf", 75)
pause_font = pygame.font.Font("font/Royale Kingdom DEMO.otf", 55)

game_rule_title_font = pygame.font.Font("font/Jersey 716.ttf", 75)
game_rule_word_font = pygame.font.Font("font/Jersey 716.ttf", 35)

game_over_title_font = pygame.font.Font("font/Carnevalee Freakshow.ttf", 75)
game_over_word_font = pygame.font.Font("font/Carnevalee Freakshow.ttf", 30)


# This function uses to reduce the decimal places of gaming time while report them
def time_format(num):
    return float(re.sub(r'^(\d+\.\d{,2})\d*$', r'\1', str(num)))


# The function to introduce the game rule
def game_rule_display(screen):
    rule_status = True

    # Loading images and fonts
    rule_pic = pygame.image.load("Rule1.png").convert()
    rule_pic = pygame.transform.scale(rule_pic, (1400, 800))
    game_rule_title = game_rule_title_font.render("GAMING RULE", True, (255, 255, 255))

    message_1 = game_rule_word_font.render("Jump Between Islands To Shoot Your Enemy", True, (255, 255, 255))
    message_2 = game_rule_word_font.render("Open Boxes to gain a powerful weapon", True, (255, 255, 255))
    message_3 = game_rule_word_font.render("protect yourself, and kills the enemy", True, (255, 255, 255))
    next_page = Button((96, 255, 255), 270, 600, "Next Page", black, screen, font)
    quit_b = Button(red, 960, 600, "Quit", black, screen, font, (255, 96, 96))
    while rule_status:

        # Bliting images and messages
        screen.blit(rule_pic, (0, 0))
        screen.blit(game_rule_title, (420, 30))
        screen.blit(message_1, (260, 260))
        screen.blit(message_2, (270, 360))
        screen.blit(message_3, (290, 460))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rule_status = False
                pygame.quit()
        if next_page.draw_button():
            game_rule_display_page_2(screen)
            rule_status = False
        if quit_b.draw_button():
            pygame.quit()

        pygame.display.update()
    # end of while
# end of function


# The second page of game rule to show keyboards displaying rules
def game_rule_display_page_2(screen):
    rule_status = True

    # Loading images and fonts
    rule_pic = pygame.image.load("Rule1.png").convert()
    rule_pic = pygame.transform.scale(rule_pic, (1400, 800))
    game_rule_title = game_rule_title_font.render("GAMING RULE", True, (255, 255, 255))
    play = Button((96, 255, 255), 270, 700, "Play", black, screen, font)
    quit_b = Button(red, 960, 700, "Quit", black, screen, font, (255, 96, 96))

    red_player = pygame.image.load("Red.png")
    red_player = pygame.transform.scale(red_player, (130, 163))

    yellow_player = pygame.image.load("Yellow.png")
    yellow_player = pygame.transform.scale(yellow_player, (130, 163))

    red_player_moving_keys = pygame.image.load("arrow keys.png")
    red_player_moving_keys = pygame.transform.scale(red_player_moving_keys, (316, 300))

    yellow_player_moving_keys = pygame.image.load("rule_wasd.png")
    yellow_player_moving_keys = pygame.transform.scale(yellow_player_moving_keys, (316, 300))

    red_shoot = pygame.image.load("M.png")
    red_shoot = pygame.transform.scale(red_shoot, (70, 70))
    red_grenade = pygame.image.load("N.png")
    red_grenade = pygame.transform.scale(red_grenade, (70, 70))

    yellow_shoot = pygame.image.load("Q.png")
    yellow_shoot = pygame.transform.scale(yellow_shoot, (70, 70))
    yellow_grenade = pygame.image.load("E.png")
    yellow_grenade = pygame.transform.scale(yellow_grenade, (70, 70))

    shooting_words = game_rule_word_font.render(" : Shoot", True, (255, 255, 255))
    grenade_words = game_rule_word_font.render(" : Grenade", True, (255, 255, 255))

    message_1 = game_rule_word_font.render("Each Weapon Has their own traits", True, (255, 255, 255))
    message_2 = game_rule_word_font.render("Try to discover yourself! ! !", True, (255, 255, 255))


    while rule_status:
        # Bliting images and messages to the screen
        screen.blit(rule_pic, (0, 0))
        screen.blit(game_rule_title, (420, 30))

        screen.blit(red_player, (100, 70))
        screen.blit(yellow_player, (1200, 70))

        screen.blit(red_player_moving_keys, (30, 210))
        screen.blit(yellow_player_moving_keys, (1070, 210))

        screen.blit(red_shoot, (60, 490))
        screen.blit(shooting_words, (140, 510))
        screen.blit(red_grenade, (60, 590))
        screen.blit(grenade_words, (140, 610))

        screen.blit(yellow_shoot, (1050, 490))
        screen.blit(shooting_words, (1130, 510))
        screen.blit(yellow_grenade, (1050, 590))
        screen.blit(grenade_words, (1130, 610))

        screen.blit(message_1, (340, 320))
        screen.blit(message_2, (380, 470))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rule_status = False
                pygame.quit()

        if play.draw_button():
            map_selection()
            rule_status = False
        if quit_b.draw_button():
            pygame.quit()
        pygame.display.update()
    # end of while
# end of function
    

# A function to pause the game at any time
def paused(current_world, intro_music):
    pausing = True

    # Loading images and fonts
    pausing_pic = pygame.image.load("Pause6.png").convert()
    pausing_pic = pygame.transform.scale(pausing_pic, (600, 340))
    first_message = pause_font.render("PAUSED", True, (255, 255, 255))
    pausing_pic.set_alpha(248)
    screen.blit(pausing_pic, (400, 250))
    screen.blit(first_message, (605, 320))
    while pausing:

        # Creating buttons on the paused function page
        button_continue = Button((255, 255, 96), 425, 480, "Continue", blue, screen, font,(255,255,160))
        button_replay = Button((96, 255, 255), 625, 480, "Replay", blue, screen, font)
        button_quit = Button(red, 825, 480, "Quit", blue, screen, font,(255,96,96))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if button_replay.draw_button():
            current_world.music.stop()
            intro_music.play(-1)
            begin()

        if button_quit.draw_button():
            pygame.quit()

        if button_continue.draw_button():
            pausing = False

        pygame.display.update()
    # end of while
# end of function


def begin():
    intro = True
    message = intro_title_font.render("Twins Fight", True, (255, 255, 255))
    while intro:

        # Bliting images and buttons
        photo = pygame.image.load("intro cover.png")
        background_pics = pygame.transform.scale(photo, (1400, 800))
        screen.blit(background_pics, (0, 0))
        screen.blit(message, (500, 190))
        play = Button((96, 255, 255), 620, 600, "Play",black, screen, font)
        game_rule = Button((255, 255, 96), 200, 600, "Game Rule", black, screen, font,(255,255,160))
        quit_b = Button(red, 1010, 600, "Quit", black, screen, font,(255,96,96))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()

        if play.draw_button():
            map_selection()
            intro = False

        if game_rule.draw_button():
            game_rule_display(screen)
            intro = False

        if quit_b.draw_button():
            intro = False
            pygame.quit()

        pygame.display.update()
    # end of while
# end of function


# A function to report the winner as well as the statics of the game
def game_over(gaming_time, winner, red_damage_per_second, red_maximum_living_time, yellow_damage_per_second, yellow_maximum_living_time, current_world):
    is_game_over = True
    game_over_pics = pygame.image.load("Over Photo.png")
    game_over_music = mixer.Sound("game over.mp3")
    music_time = 1

    message_1 = game_over_title_font.render("Game Over", True, (255, 0, 0))
    message_2 = game_rule_word_font.render("The Winner Is", True, (255, 0, 0))

    # Bliting the image based on the winner
    if winner == "Red":
        message_3 = game_rule_word_font.render(f"{winner} Player !", True, (255, 0, 0))
    else:
        message_3 = game_rule_word_font.render(f"{winner} Player !", True, (255, 255, 32))

    red_player = pygame.image.load("Red.png")
    red_player = pygame.transform.scale(red_player, (200, 255))

    yellow_player = pygame.image.load("Yellow.png")
    yellow_player = pygame.transform.scale(yellow_player, (200, 250))

    message_4 = game_over_word_font.render(f"Gaming Time: {gaming_time} s", True, (255, 0, 0))
    message_5 = game_over_word_font.render(f"Red Player: {red_damage_per_second} damage per sec", True, (255, 0, 0))
    message_6 = game_over_word_font.render(f"Red Maximum Living Time {red_maximum_living_time} s", True, (255, 0, 0))
    message_7 = game_over_word_font.render(f"Yellow Player: {yellow_damage_per_second} damage per sec", True,  (255, 255, 32))
    message_8 = game_over_word_font.render(f"Yellow Maximum Living Time {yellow_maximum_living_time} s", True,  (255, 255, 32))

    # Use time count to delay bliting the image and the message
    run_time_count = 0
    display_photo_count = 0

    while is_game_over:
        current_world.music.stop()
        if music_time == 1:
            game_over_music.play()
            music_time -= 1
        screen.blit(game_over_pics, (0, 0))
        screen.blit(message_1, (550, 20))
        screen.blit(message_2, (420, 200))

        screen.blit(message_4, (580, 120))

        play = Button((96, 255, 255), 300, 600, "Replay", black, screen, font)
        quit_b = Button(red, 1010, 600, "Quit", black, screen, font, (255, 96, 96))

        # Use this to delay the execution
        if run_time_count >= 120:
            screen.blit(message_3, (740, 200))
            if display_photo_count >= 20:
                if winner == "Red":
                    screen.blit(red_player, (600, 250))
                else:
                    screen.blit(yellow_player, (600, 250))
                screen.blit(message_5, (200, 270))
                screen.blit(message_6, (200, 370))
                screen.blit(message_7, (830, 270))
                screen.blit(message_8, (830, 370))
            display_photo_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if play.draw_button():
            current_world.music.stop()
            intro_music.play(-1)
            begin()
        if quit_b.draw_button():
            is_game_over = False
            pygame.quit()
            quit()

        run_time_count += 1
        pygame.display.update()
    # end of while
# end of function


# A function to show map selection page
def map_selection():
    map_selection_status = True

    # Loading images and fonts
    photo = pygame.image.load("Map Selection Background.jpeg")
    arctic_photo = pygame.image.load("Arctic Map.jpg")
    forest_photo = pygame.image.load("Forest.jpg")
    sky_photo = pygame.image.load("Sky_Island.jpg")

    map_selection_photo = pygame.transform.scale(photo, (1400, 800))
    arctic_photo = pygame.transform.scale(arctic_photo, (400, 280))
    forest_photo = pygame.transform.scale(forest_photo, (400, 280))
    sky_photo = pygame.transform.scale(sky_photo, (400, 280))

    red_player = pygame.image.load("Red.png")
    red_player = pygame.transform.scale(red_player, (80, 100))

    yellow_player = pygame.image.load("Yellow.png")
    yellow_player = pygame.transform.scale(yellow_player, (80, 100))

    map_deco = pygame.image.load("Map Deco.png")
    map_deco = pygame.transform.scale(map_deco, (512, 412))

    map_selection_message = map_selection_title_font.render("MAP SELECTION", True, (255, 128, 0))

    while map_selection_status:

        # Displaying images and fonts
        screen.blit(map_selection_photo, (0, 0))
        screen.blit(arctic_photo, (950, 240))
        screen.blit(forest_photo, (50, 240))
        screen.blit(sky_photo, (500, 240))
        screen.blit(red_player, (10, 20))
        screen.blit(yellow_player, (1300, 20))
        screen.blit(map_deco, (450, -150))
        screen.blit(map_selection_message, (480, 100))
        select1 = Button((96, 255, 255), 175, 600, "Forest", black, screen, font)
        select2 = Button((96, 255, 255), 625, 600, "Sky", black, screen, font)
        select3 = Button((96, 255, 255), 1055, 600, "Arctic", black, screen, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_selection_status = False
                pygame.quit()

        # Different condition while pressing a button
        if select1.draw_button():
            game_loop(1)
            map_selection_status = False

        if select2.draw_button():
            game_loop(2)
            map_selection_status = False

        if select3.draw_button():
            game_loop(3)
            map_selection_status = False

        pygame.display.update()
    # end of while
# end of function


# The main game loop to start the game
def game_loop(map_selection):

    # Initializing variables for the game
    status = True
    current_world = None
    islands = None
    y_stand = 0
    land_y = 0

    # Call the current world user choose
    if map_selection == 1:
        current_world = map_list[0]
        islands = current_world.get_draw_list()
        y_stand = 25
        land_y = 640
    if map_selection == 2:
        current_world = map_list[1]
        islands = current_world.get_draw_list()
        y_stand = 25
        land_y = 780
    if map_selection == 3:
        current_world = map_list[2]
        islands = current_world.get_draw_list()
        y_stand = 40
        land_y = 640
    generate_time = 0
    special_box_gt = 0
    clock = pygame.time.Clock()
    clock2 = pygame.time.Clock()

    random_box = None
    special_box = None

    music_play = 1
    is_tracking_game_time = True
    starting_time = time.time()

    player1_x = 40
    player1_y = -50
    player = Player1(player1_x, player1_y)

    player2_x = 1360
    player2_y = -50
    another_player = Player2(player2_x, player2_y)

    # Creating bullet sprite group
    default_bullet_group = pygame.sprite.Group()
    canon_bullet_group = pygame.sprite.Group()
    sniper_bullet_group = pygame.sprite.Group()
    riffle_bullet_group = pygame.sprite.Group()
    scatter_bullet_group = pygame.sprite.Group()

    # Creating explosion sprite group for each bullet
    explosion_group = pygame.sprite.Group()
    canon_explosion_group = pygame.sprite.Group()
    riffle_explosion_group = pygame.sprite.Group()
    scatter_explosion_group = pygame.sprite.Group()
    sniper_explosion_group = pygame.sprite.Group()
    players_explosion_group = pygame.sprite.Group()

    player_grenade_group = pygame.sprite.Group()
    another_player_grenade_group = pygame.sprite.Group()

    player_health_bar = HealthBar(80, 45, player.health, player.health)
    another_player_health_bar = HealthBar(1170, 45, player.health, player.health)

    # Initializing final static report variables
    gaming_time = 0.0
    red_damage_per_second = 0.0
    yellow_damage_per_second = 0.0
    exploding_count = 0

    while status:
        intro_music.stop()
        current_world.draw(screen)

        # Use to handle multiple gaming sound
        if music_play == 1:
            current_world.music.play(-1)
            music_play -= 1

        general_clock.tick(FPS)
        first_round_box = current_world.generate_boxes(screen, first_round=True)

        # Update the sprites groups for players and bullets
        player.update_all(players_explosion_group)
        another_player.update_all(players_explosion_group)
        default_bullet_group.update(player, another_player, default_bullet_group)
        canon_bullet_group.update(player, another_player, canon_bullet_group, canon_explosion_group)
        sniper_bullet_group.update(player, another_player, sniper_bullet_group, sniper_explosion_group)
        riffle_bullet_group.update(player, another_player, riffle_bullet_group, riffle_explosion_group)
        scatter_bullet_group.update(player, another_player, scatter_bullet_group, scatter_explosion_group)

        player_grenade_group.update(player, another_player, explosion_group, current_world.name)
        another_player_grenade_group.update(player, another_player, explosion_group, current_world.name)

        # Update the explosion groups
        explosion_group.update()
        canon_explosion_group.update()
        riffle_explosion_group.update()
        scatter_explosion_group.update()
        sniper_explosion_group.update()
        players_explosion_group.update()

        # Draw the bullet groups
        default_bullet_group.draw(screen)
        canon_bullet_group.draw(screen)
        sniper_bullet_group.draw(screen)
        riffle_bullet_group.draw(screen)
        scatter_bullet_group.draw(screen)

        # Draw the explosion groups
        player.show_player(screen)
        another_player.show_player(screen)
        player_grenade_group.draw(screen)
        another_player_grenade_group.draw(screen)
        explosion_group.draw(screen)
        canon_explosion_group.draw(screen)
        riffle_explosion_group.draw(screen)
        scatter_explosion_group.draw(screen)
        sniper_explosion_group.draw(screen)
        players_explosion_group.draw(screen)

        # Display the health bar
        player_health_bar.draw(player.health, screen)
        another_player_health_bar.draw(another_player.health, screen)

        # Track living Times for two players
        player.track_living_time()
        another_player.track_living_time()

        # if 2 boxes are gone, generate new random
        if first_round_box[1][1].x == 2000 and first_round_box[0][1].x == 2000:
            dt = clock.tick()
            generate_time += dt
            if generate_time > 5000:  # 10000
                random_box = current_world.generate_boxes(screen, first_round=False)
                generate_time = 0

            if random_box is not None:
                screen.blit(random_box[0], random_box[1])

        special_box_dt = clock2.tick()
        special_box_gt += special_box_dt

        if special_box_gt > 10000:  # 25000
            special_box = current_world.generate_boxes(screen, first_round=False, special_box=True)
            special_box_gt = 0

        if special_box is not None:
            screen.blit(special_box[0], special_box[1])

        # draw_grid()
        player.moving(islands,y_stand,land_y)
        another_player.moving(islands,y_stand,land_y)

        # Show total lives
        player.display_total_lives(screen)
        another_player.display_total_lives(screen)

        # Show Bullets Numbers
        player.display_bullet_numbers(screen)
        another_player.display_bullet_numbers(screen)

        # Show grenade numbers
        player.display_grenade_numbers(screen)
        another_player.display_grenade_numbers(screen)

        # Show jumping times
        player.display_jumping_times(screen)
        another_player.display_jumping_times(screen)

        # Setting the weapon back to default if running out of bullet
        if player.riffle_limit == 0:
            player.update_weapon(0)
        elif player.sniper_limit == 0:
            player.update_weapon(0)
        elif player.canon_limit == 0:
            player.update_weapon(0)
        elif player.scatter_limit == 0:
            player.update_weapon(0)

        if another_player.riffle_limit == 0:
            another_player.update_weapon(0)
        elif another_player.sniper_limit == 0:
            another_player.update_weapon(0)
        elif another_player.canon_limit == 0:
            another_player.update_weapon(0)
        elif another_player.scatter_limit == 0:
            another_player.update_weapon(0)

        # Handling weapon changing for players
        if player.alive:
            # shoot bullets
            if player.is_shooting and player.weapon_index == 0:
                # Shoot default bullet
                player.shooting_default_bullet(default_bullet_group)

            elif player.is_shooting and player.weapon_index == 1:
                # Shoot riffle bullet
                player.shooting_riffle_bullet(riffle_bullet_group)

            elif player.is_shooting and player.weapon_index == 2:
                # Shoot sniper bullet
                player.shooting_sniper_bullet(sniper_bullet_group)

            elif player.is_shooting and player.weapon_index == 3:
                # Shoot canon bullet
                player.shooting_canon_bullet(canon_bullet_group)

            elif player.is_shooting and player.weapon_index == 4:
                # Shoot scatter bullet
                player.shooting_scatter_bullet(scatter_bullet_group)

            # Throwing grenade
            elif player.is_grenade and player.grenade_thrown == False and player.grenade_total > 0:
                grenade = Grenade1(player.rect.centerx + (0.7 * player.rect.size[0] * player.direction),
                                   player.rect.top, player.direction)
                player_grenade_group.add(grenade)
                player.grenade_thrown = True
                player.grenade_total -= 1

        # Apply the same change for another player
        if another_player.alive:
            # shoot bullets
            if another_player.is_shooting and another_player.weapon_index == 0:
                # Shoot default bullet
                another_player.shooting_default_bullet(default_bullet_group)

            elif another_player.is_shooting and another_player.weapon_index == 1:
                # Shoot riffle bullet
                another_player.shooting_riffle_bullet(riffle_bullet_group)

            elif another_player.is_shooting and another_player.weapon_index == 2:
                # Shoot sniper bullet
                another_player.shooting_sniper_bullet(sniper_bullet_group)

            elif another_player.is_shooting and another_player.weapon_index == 3:
                # Shoot canon bullet
                another_player.shooting_canon_bullet(canon_bullet_group)

            elif another_player.is_shooting and another_player.weapon_index == 4:
                # Shoot scatter bullet
                another_player.shooting_scatter_bullet(scatter_bullet_group)

            # Handle if another player is throwing the grenade
            elif another_player.is_grenade and another_player.grenade_thrown == False and another_player.grenade_total > 0:
                grenade = Grenade2(
                    another_player.rect.centerx + (0.7 * another_player.rect.size[0] * another_player.direction),
                    another_player.rect.top, another_player.direction)
                another_player_grenade_group.add(grenade)
                another_player.grenade_thrown = True
                another_player.grenade_total -= 1

        # Update the moving sprites of player
        if player.current_jump_times < player.maximum_jump_times:
            player.update_action(2)  # 2: jump
        elif player.moving_left or player.moving_right:
            player.update_action(1)  # 1: run
        else:
            player.update_action(0)  # 0: idle

        # Update the moving sprites of another player
        if another_player.current_jump_times < another_player.maximum_jump_times:
            another_player.update_action(2)  # 2: jump
        elif another_player.moving_left or another_player.moving_right:
            another_player.update_action(1)  # 1: run
        else:
            another_player.update_action(0)  # 0: idle

        # Calculate the variables to call the game over function
        if not player.alive or not another_player.alive:
            if is_tracking_game_time:
                ending_time = time.time()
                gaming_time = time_format(ending_time - starting_time)
                is_tracking_game_time = False

                if not another_player.alive:
                    yellow_damage_per_second = time_format(600.0 / gaming_time)
                else:
                    yellow_damage_per_second = time_format(
                        (100 * (6 - another_player.total_lives) + (100 - another_player.health)) / gaming_time)
                if not player.alive:
                    red_damage_per_second = time_format(600.0 / gaming_time)
                else:
                    red_damage_per_second = time_format(
                        (100 * (6 - player.total_lives) + (100 - player.health)) / gaming_time)
            exploding_count += 1

            if another_player.is_explode and exploding_count == 155:
                time.sleep(1)
                winner = "Red"
                game_over(gaming_time, winner, red_damage_per_second, player.maximum_living_time, yellow_damage_per_second,
                          another_player.maximum_living_time, current_world)
            elif player.is_explode and exploding_count == 155:
                time.sleep(1)
                winner = "Yellow"
                game_over(gaming_time, winner, red_damage_per_second, player.maximum_living_time, yellow_damage_per_second,
                          another_player.maximum_living_time, current_world)

        # player collides with magic boxes
        if player.rect.colliderect(first_round_box[0][1]):
            current_world.erase_box(first_round_box[0], screen)
            weapon_type = random.choice([1,2,3,4])
            player.update_weapon_bullets()
            player.update_weapon(weapon_type)
            player.animation_update()

        if player.rect.colliderect(first_round_box[1][1]):
            current_world.erase_box(first_round_box[1], screen)
            player.update_weapon_bullets()
            weapon_type = random.choice([1, 2, 3, 4])
            player.update_weapon(weapon_type)
            player.animation_update()

        # Handling the choices for different types of random boxes
        if random_box is not None:
            if player.rect.colliderect(random_box[1]):
                if random_box[2] == 1:
                    weapon_type = random.choice([1, 2, 3, 4])
                    player.update_weapon_bullets()
                    player.update_weapon(weapon_type)
                    player.animation_update()
                if random_box[2] == 2:
                    player.grenade_total += 2
                if random_box[2] == 3:
                    if player.health + 40 < 100:
                        player.health += 40
                    else:
                        player.health = 100
                if random_box[2] == 4:
                    player.maximum_jump_times = 3

                random_box = None


        if special_box is not None:
            if player.rect.colliderect(special_box[1]):
                current_status = random.choice([1,2,3,4])
                if current_status == 1:
                    weapon_type = random.choice([1, 2, 3])
                    player.update_weapon_bullets()
                    player.update_weapon(weapon_type)
                    player.animation_update()
                if current_status == 2:
                    player.grenade_total += 2
                if current_status == 3:
                    if player.health + 40 < 100:
                        player.health += 40
                    else:
                        player.health = 100


                random_box = None
                special_box = None

        # Check if another player is colliding with the box
        if another_player.rect.colliderect(first_round_box[0][1]):
            current_world.erase_box(first_round_box[0], screen)
            weapon_type = random.choice([1,2,3,4])
            another_player.update_weapon_bullets()
            another_player.update_weapon(weapon_type)
            another_player.animation_update()
                
        if another_player.rect.colliderect(first_round_box[1][1]):
            current_world.erase_box(first_round_box[1], screen)
            another_player.update_weapon_bullets()
            weapon_type = random.choice([1,2,3,4])
            another_player.update_weapon(weapon_type)
            another_player.animation_update()

        if random_box is not None:
            if another_player.rect.colliderect(random_box[1]):
                if random_box[2] == 1:
                    weapon_type = random.choice([1,2,3,4])
                    another_player.update_weapon_bullets()
                    another_player.update_weapon(weapon_type)
                    another_player.animation_update()
                if random_box[2] == 2:
                    another_player.grenade_total += 2
                if random_box[2] == 3:
                    if another_player.health + 40 < 100:
                        another_player.health += 40
                    else:
                        another_player.health = 100
                if random_box[2] == 4:
                    another_player.maximum_jump_times = 3

                random_box = None
        if special_box is not None:
            if another_player.rect.colliderect(special_box[1]):
                current_status = random.choice([1,2,3])
                if current_status == 1:
                    weapon_type = random.choice([1,2,3,4])
                    another_player.update_weapon_bullets()
                    another_player.update_weapon(weapon_type)
                    another_player.animation_update()
                if current_status == 2:
                    another_player.grenade_total += 2
                if current_status == 3:
                    if another_player.health + 40 < 100:
                        another_player.health += 40
                    else:
                        another_player.health = 100

                special_box = None

        # Handling keyboard pressings
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.moving_left = True
                if event.key == pygame.K_RIGHT:
                    player.moving_right = True
                if event.key == pygame.K_UP and player.alive:
                    player.jump = True
                    player.current_jump_times -= 1
                    if player.current_jump_times < 0:
                        player.jump = False

                if event.key == pygame.K_a:
                    another_player.moving_left = True
                if event.key == pygame.K_d:
                    another_player.moving_right = True
                if event.key == pygame.K_w and another_player.alive:
                    another_player.jump = True
                    another_player.current_jump_times -= 1
                    if another_player.current_jump_times < 0:
                        another_player.jump = False

                if event.key == pygame.K_m:
                    player.is_shooting = True
                if event.key == pygame.K_q:
                    another_player.is_shooting = True

                if event.key == pygame.K_n:
                    player.is_grenade = True
                if event.key == pygame.K_e:
                    another_player.is_grenade = True
                if event.key == pygame.K_SPACE:
                    paused(current_world, intro_music)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.moving_left = False
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False
                if event.key == pygame.K_UP:
                    player.jump = False

                if event.key == pygame.K_a:
                    another_player.moving_left = False
                if event.key == pygame.K_d:
                    another_player.moving_right = False
                if event.key == pygame.K_w:
                    another_player.jump = False

                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_m:
                    player.is_shooting = False
                if event.key == pygame.K_q:
                    another_player.is_shooting = False

                if event.key == pygame.K_n:
                    player.is_grenade = False
                    player.grenade_thrown = False
                if event.key == pygame.K_e:
                    another_player.is_grenade = False
                    another_player.grenade_thrown = False

        pygame.display.update()

    pygame.quit()
    quit()
# end of function


begin()

