import pygame
import random
from MagicBox import MagicBox
from pygame import mixer


class Sky:
    # the constructor of Sky loads images from folder
    def __init__(self):
        self.bg = pygame.image.load("Sky Map/Sky Map Background.jpg")
        self.big_island_upper_part = pygame.image.load("Sky Map/Sky Centre Island upper part.png")
        self.big_island_bottom_part = pygame.image.load("Sky Map/Sky Centre Island bottom part.png")
        self.small_island = pygame.image.load("Sky Map/small_island.png")
        self.second_small_island = pygame.image.load("Sky Map/small island2.png")
        self.box_areas = []
        self.draw_list = []
        self.box_first_round = MagicBox()
        self.box_first_round2 = MagicBox()
        # get two default weapon boxes rectangle and image
        self.first_round_box_image = self.box_first_round.processer()[0][0]
        self.first_round_box_rect = self.box_first_round.processer()[0][1]
        self.first_round_box2_image = self.box_first_round2.processer()[0][0]
        self.first_round_box2_rect = self.box_first_round2.processer()[0][1]
        # set 2 default x and y values
        self.first_round_box_rect.x = 120
        self.first_round_box_rect.y = 90
        self.first_round_box2_rect.x = 1220
        self.first_round_box2_rect.y = 90
        # get the music
        self.music = mixer.Sound("Sky_Music.mp3")
        self.name = "Sky"


        # the following for loop is to set the position for each islands in the map
        # and get the box areas and the islands rectangle for checking the collisions
        for i in range(0, 1):
            img = self.big_island_bottom_part
            img_rect = img.get_rect()
            img_rect.x = 515
            img_rect.y = 367
            current = (img, img_rect)
            self.draw_list.append(current)


        distance = 250
        for i in range(0, 2):
            img = self.small_island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 210
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 750
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y - 30))

        distance = 250
        for i in range(0, 2):
            img = self.small_island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 380
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 750
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y - 30))

        distance = 70
        for i in range(0, 2):
            img = self.second_small_island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 120
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 1100
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y - 30))
        distance = 70
        for i in range(0, 2):
            img = self.second_small_island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 280
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 1100
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y - 30))

        distance = 70
        for i in range(0, 2):
            img = self.second_small_island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 440
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 1100
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y - 30))

        distance = 70
        for i in range(0, 2):
            img = self.second_small_island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 600
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 1100
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y - 30))



    # draw method blit all the image on to the screen
    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        img = self.big_island_upper_part
        img_rect = img.get_rect()
        img_rect.x = 515
        img_rect.y = 250
        screen.blit(img,img_rect)
        for item in self.draw_list:
            screen.blit(item[0], item[1])

    """ generate_boxes method generate the random boxes, first_round boxes and special boxes.
     -- param
     screen: screen
     first_round: boolean
     special_box: boolean
     Two boolean is like two switches, makes one of either switch True will execute different actions
    """
    def generate_boxes(self,screen,first_round=False, special_box =False):

        if first_round:
            screen.blit(self.first_round_box_image, self.first_round_box_rect)
            screen.blit(self.first_round_box2_image,self.first_round_box2_rect)

            return [(self.first_round_box_image, self.first_round_box_rect),
                    (self.first_round_box2_image, self.first_round_box2_rect)
                    ]
        if not first_round and not special_box:
            # for random boxes
            boxes_random = MagicBox()
            random_box = random.choice(boxes_random.processer())
            # big area, island area
            random_area = random.choice((self.box_areas))
            random_box[1].y =random_area[2]
            random_box[1].x = random.randrange(random_area[0],random_area[1])
            return (random_box[0],random_box[1],random_box[2])

        if special_box:
            return self.box_first_round.get_special_box(660,330)


    # this method is just used to erase two first round boxes
    def erase_box(self, box,screen):
        replaceBg = self.bg.subsurface(box[1])
        screen.blit(replaceBg,box[1])
        pygame.display.update(box[1])
        box[1].x = 2000
        box[1].y = 2000
        print("re")
    # get_draw_list() is used for the class outside map classes to get the surface of the islands and
    # check for collision
    def get_draw_list(self):
        return self.draw_list


