import pygame
from pygame.locals import *

clicked = False


class Button:
    """
    the constructor of Button class get data from outside of the Button class for the other function
    to use
    """
    def __init__(self,button_col,x,y,text,text_col,screen,font,hover_col =(75, 225, 255)):
        self.button_col = button_col
        self.hover_col = hover_col#(75, 225, 255)
        self.click_col = (50, 150, 255)
        self.width = 150
        self.height = 60
        self.x = x
        self.y = y
        self.text = text
        self.text_col = text_col
        self.screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.font = font

    """
    draw_button method is the key part of this Button Class, it simply generate a button on the screen from the
     data collected from the constructor and return a signal if the button is being clicked or not to the place
     where the program calls it
    """
    def draw_button(self):
        global clicked
        status = False

        # get position
        position = pygame.mouse.get_pos()

        # create a button rectangle
        button_rect = Rect(self.x, self.y,self.width,self.height)

        # check 3 status
        # 1.mouse is clicked and released
        # 2. mouse is hover on the button
        # 3. mouse hasn't colide with the button
        if button_rect.collidepoint(position):
            # when mouse is clicked and released
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(self.screen, self.click_col, button_rect)

            # it is not clicked right now but it was clicked before
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                status = True
            # if mouse is on the button but not clicked
            else:
                pygame.draw.rect(self.screen, self.hover_col, button_rect)
        # if the mouse haven't meet the button, we draw a normal button
        else:
            pygame.draw.rect(self.screen, self.button_col, button_rect)

        # give the button a little bit 3D texture
        pygame.draw.line(self.screen, self.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(self.screen, self.white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(self.screen, self.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(self.screen, self.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = self.font.render(self.text, True, self.text_col)
        text_length = text_img.get_width()
        self.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_length / 2), self.y + 20))
        return status
