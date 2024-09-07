import pygame
import random
from MagicBox import MagicBox
from pygame import mixer



class ArcticMap(object):
    # the constructor of arctic map loads images from folder
    def __init__(self):
        self.island = pygame.image.load("Arctic Map/Ice Image - Island.png")
        self.deco = pygame.image.load("Arctic Map/deco.png")
        self.centre_island_upper_part = pygame.image.load("Arctic Map/Ice Centre Island upper part.png")
        self.centre_island_bottom_part = pygame.image.load("Arctic Map/Ice Centre Island bottom part.png")
        self.background = pygame.image.load("Arctic Map/Ice Image 3.jpg")
        self.draw_list = []
        self.box_areas = []
        self.box_first_round = MagicBox()
        self.box_first_round2 = MagicBox()
        self.first_round_box_image = self.box_first_round.processer()[0][0]
        self.first_round_box_rect = self.box_first_round.processer()[0][1]
        self.first_round_box2_image = self.box_first_round2.processer()[0][0]
        self.first_round_box2_rect = self.box_first_round2.processer()[0][1]
        self.first_round_box_rect.x = 110
        self.first_round_box_rect.y = 100
        self.first_round_box2_rect.x = 1203
        self.first_round_box2_rect.y = 100
        self.music = mixer.Sound("stick fight 1.mp3")
        self.name = "Arctic"

        # the following for loop is to set the position for each islands in the map
        # and get the box areas and the islands rectangle for checking the collisions
        for i in range(0, 1):
            img = self.centre_island_bottom_part
            img_rect = img.get_rect()
            img_rect.x = 555
            img_rect.y = 121
            current = (img, img_rect)

            self.draw_list.append(current)

        distance = 40
        for i in range(0,2):
            img = self.island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 130
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 1090
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y -30))
        distance = 250
        for i in range(0, 2):
            img = self.island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 240
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 700
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y -30))

        distance = 90
        for i in range(0, 3):
            img = self.island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 360
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 420
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y-30 ))

        distance = 150
        for i in range(0, 2):
            img = self.island
            img_rect = img.get_rect()
            img_rect.x = 0 + distance
            img_rect.y = 510
            current = (img, img_rect)
            self.draw_list.append(current)
            distance += 420
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y-30 ))
        for i in range(0, 1):
            img = self.island
            img_rect = img.get_rect()
            img_rect.x = 1200
            img_rect.y = 510
            current = (img, img_rect)
            self.draw_list.append(current)
            self.box_areas.append((img_rect.x,
                                   img_rect.width + img_rect.x - 40,
                                   img_rect.y -30))

    # draw method blit all the image on to the screen
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        img = self.centre_island_upper_part
        img_rect = img.get_rect()
        img_rect.x = 555
        img_rect.y = 20
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
    def generate_boxes(self, screen, first_round=False, special_box=False):

        if first_round:
            screen.blit(self.first_round_box_image, self.first_round_box_rect)
            screen.blit(self.first_round_box2_image, self.first_round_box2_rect)

            return [(self.first_round_box_image, self.first_round_box_rect),
                    (self.first_round_box2_image, self.first_round_box2_rect)
                    ]
        if not first_round and not special_box:
            # for random boxes
            boxes_random = MagicBox()
            random_box = random.choice(boxes_random.processer())
            # big area, island area
            random_area = random.choice((self.box_areas))
            random_box[1].y = random_area[2]
            random_box[1].x = random.randrange(random_area[0], random_area[1])
            return (random_box[0], random_box[1],random_box[2])

        if special_box:
            return self.box_first_round.get_special_box(650, 80)

    # this method is just used to erase two first round boxes
    def erase_box(self, box, screen):
        replaceBg = self.background.subsurface(box[1])
        screen.blit(replaceBg, box[1])
        pygame.display.update(box[1])
        box[1].x = 2000
        box[1].y = 2000
        print("re")

    # get_draw_list() is used for the class outside map classes to get the surface of the islands and
    # check for collision
    def get_draw_list(self):
        return self.draw_list