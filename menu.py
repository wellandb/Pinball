# Start the game have options for pinball, pinball with set start and then a fractal explorer
import pygame, sys
import Pinball, map_menu, fractal_interaction
import fractals
import shape
import time
import boardGeneration
from settings import *

# Button Class for choices in menu
class Button(pygame.sprite.Sprite):

    # Initialize the object
    def __init__(self, x, y, width, height, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.function = function
        self.colour = BLUE
        
    # draw the button onto the screen
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

    # function for the button
    def func(self):
        self.function()
        return self.function()
    
    # check the button has been clicked
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.func()
    # function to select the button and return the function
    def select(self):
        return self.func()
    
    # function to show it is selected, colour = Red
    def is_selected(self):
        self.colour = RED
    
    # function to show it is not selected, colour = Blue
    def not_selected(self):
        self.colour = BLUE

# pinball button function
def pinball():
    return "pinball"
# map menu button function
def map_Menu():
    return "map_menu"
# fractal interaction function
def fractal_inter():
    return "fractal interaction"

# main that is run when the file is run
def main():
    # background
    # bkg = pygame.image.load("img/neon_L.jpg")
    # bkg_fit = pygame.transform.scale(bkg, (screenWidth,screenHeight))
    # background fractal
    shapes = fractals.create_fractal((False, shape.Star, 4), 20, True, 19, 1.5, (255, 255, 255), 'uuu', 20)
    # button list
    buttons = []
    buttons.append(Button(screenWidth* 1/4 - 10, 225, 100, 50, pinball))
    buttons.append(Button(screenWidth* 2/4 - 10, 225, 100, 50, map_Menu))
    buttons.append(Button(screenWidth* 3/4 - 10, 225, 100, 50, fractal_inter))
    buttons[0].is_selected()
    selection = 0
    # key sleep is to stop over commitment of inputs as a press could last several frames
    key_sleep = False
    # count stores number of frames that the keyboard is asleep for
    count = 0
    # game loop
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
            
        # get current state of the keyboard
        keys = pygame.key.get_pressed()
        if not key_sleep:
            # if left pressed then select the button to the left
            if keys[pygame.K_LEFT]:
                selection = (selection - 1) % len(buttons)
                key_sleep = True
            # if right pressed then select the button on the right
            if keys[pygame.K_RIGHT]:
                selection = (selection + 1) % len(buttons)
                key_sleep = True
            # call the function for the selected button when space is pressed
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
                

        # show selected buttons
        for i in buttons:
            if i == buttons[selection]:
                i.is_selected()
            else:
                i.not_selected()

        # fill the background with black
        win.fill(BLACK)
        # win.blit(bkg_fit,(0,0))
        # sort the shapes from large to small so the smaller shapes can be seen
        shapes.sort(reverse= True, key=lambda x: x.get_area())
        for i in shapes: # draw the shapes
            i.draw(win)
        for s in shapes:# rotate and update colour of shapes
            s.rotate_poly(1, s.get_clockwise())
            s.update_colour(3)
        for i in buttons: # draw the buttons
            i.draw(win)

        # win.blit(pygame.image.load('bcg.img'), (screenWidth/2 - 225, 100))
        # draw the text that explains the menu
        win.blit(myfont.render('FracBall', True, WHITE), (screenWidth/2 - 50, 100))
        win.blit(smallfont.render('Pinball', True, WHITE), (screenWidth* 1/4, 250))
        win.blit(smallfont.render('Map', True, WHITE), (screenWidth* 2/4, 250))
        win.blit(smallfont.render('fractal', True, WHITE), (screenWidth* 3/4, 250))

        # update the screen
        pygame.display.update()
    # calls the choice of the button press
    # pinball starts the pinball simulation
    if choice == "pinball":
        Pinball.main(boardGeneration.board1)
    # map menu opens the map menu
    elif choice == "map_menu":
        board = map_menu.main()
        Pinball.main(board) # run pinball simulation on the board selection
    # fractals will start the fractal interaction
    elif choice == "fractal interaction":
        fractal_interaction.main(False, 1, 20, True, 19, 1.5, (255, 255, 255), 'uuu', 20)
# call the main function
main()
# quit pygame after a run through
pygame.quit()