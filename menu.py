# Start the game have options for pinball, pinball with set start and then a fractal explorer
import pygame, sys
import Pinball, map_menu, fractal_interaction
import fractals
import shape
import time

pygame.init()

from settings import *

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.function = function
        self.colour = BLUE
        
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

    def func(self):
        self.function()
        return self.function()
    
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.func()

    def select(self):
        return self.func()
    
    def is_selected(self):
        self.colour = RED
    
    def not_selected(self):
        self.colour = BLUE

def pinball():
    return "pinball"
def map_Menu():
    return "map_menu"
def fractal_inter():
    return "fractal interaction"


def main():
    # background
    # bkg = pygame.image.load("img/neon_L.jpg")
    # bkg_fit = pygame.transform.scale(bkg, (screenWidth,screenHeight))
    shapes = fractals.create_fractal((False, shape.Star), 20, True, 19, 1.5, (255, 255, 255), 'uuu', 20)

    buttons = []
    buttons.append(Button(screenWidth* 1/4 - 10, 225, 100, 50, pinball))
    buttons.append(Button(screenWidth* 2/4 - 10, 225, 100, 50, map_Menu))
    buttons.append(Button(screenWidth* 3/4 - 10, 225, 100, 50, fractal_inter))
    buttons[0].is_selected()
    selection = 0
    key_sleep = False
    count = 0
    menu = True
    while menu:
        # set clock
        clock.tick(30)

        #event loop
        for event in pygame.event.get():
            # bomb out of loop if quit
            if event.type == pygame.QUIT:
                menu = False
            
        # if pygame.mouse.get_pressed():
        #     for b in buttons:
        #         b.check_click(pygame.mouse.get_pos())
            
        keys = pygame.key.get_pressed()
        if not key_sleep:
            if keys[pygame.K_LEFT]:
                selection = (selection - 1) % len(buttons)
                key_sleep = True
            if keys[pygame.K_RIGHT]:
                selection = (selection + 1) % len(buttons)
                key_sleep = True
            if keys[pygame.K_SPACE]:
                choice = buttons[selection].select()
                menu = False
                key_sleep = True
        else:
            if count == 3:
                count = 0
                key_sleep = False
            else:
                count += 1
                

        for i in buttons:
            if i == buttons[selection]:
                i.is_selected()
            else:
                i.not_selected()

        win.fill(BLACK)
        # win.blit(bkg_fit,(0,0))
        shapes.sort(reverse= True, key=lambda x: x.get_area())
        for i in shapes:
            i.draw(win)
        for s in shapes:
            s.rotate_poly(1, s.get_clockwise())
            s.update_colour(3)
        for i in buttons:
            i.draw(win)
        # win.blit(pygame.image.load('bcg.img'), (screenWidth/2 - 225, 100))
        win.blit(myfont.render('FracBall', True, WHITE), (screenWidth/2 - 50, 100))
        win.blit(smallfont.render('Pinball', True, WHITE), (screenWidth* 1/4, 250))
        win.blit(smallfont.render('Map', True, WHITE), (screenWidth* 2/4, 250))
        win.blit(smallfont.render('fractal', True, WHITE), (screenWidth* 3/4, 250))

        pygame.display.update()
    return choice

choice = main()
print(choice)
if choice == "pinball":
    Pinball.main()
elif choice == "map_menu":
    map_menu.main()
elif choice == "fractal interaction":
    fractal_interaction.main()