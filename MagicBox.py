import pygame
""" Magic Box is a class that is mainly responsible for dealing with magic box image and rectangle
"""


class MagicBox:
    # The constructor of Magic box simply loads image froom the folder to the program.

    def __init__(self):
        self.__weapon_box = pygame.image.load("boxes/weapon box.png")
        self.__grenade_supply = pygame.image.load("boxes/grenade supply box.png")
        self.__health_recovery = pygame.image.load("boxes/life recovery box.png")
        self.__triple_jump = pygame.image.load("boxes/triple jump box.png")
        self.__special_box = pygame.image.load("boxes/secret box.png")

    # processer function get the image from constructor and generate a rectangle area for each box
    # and return to where the program calls it.
    def processer(self):
        # the number 1,2,3,4 represents different types of weapon, return it so we can process in where we call
        # this function
        return [(self.__weapon_box, self.__weapon_box.get_rect(), 1),
                (self.__grenade_supply, self.__grenade_supply.get_rect(),2),
                (self.__health_recovery, self.__health_recovery.get_rect(),3),
                (self.__triple_jump, self.__triple_jump.get_rect(),4)
                ]
    # special box has the similar functionality of processer function, but proocesser is used for random
    # while special box is used for its specific use
    def get_special_box(self,x,y):
        special_box_rect = self.__special_box.get_rect()
        special_box_rect.x = x
        special_box_rect.y = y
        return [self.__special_box,special_box_rect]