# selection of all the maps
# Import necessary modules
from settings import *
import boardGeneration
import fractals
import shape

# Button class
class Button(pygame.sprite.Sprite):

    # Intialize object
    def __init__(self, x, y, width, height, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.function = function # function to be run when selected
        self.colour = BLUE
        
    # draw the button on the window
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

    # return stored function
    def func(self):
        return self.function
    
    # chcek the that the button has been clicked
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.func()

    # select the button
    def select(self):
        return self.func()
    
    # if currently selected show in red else, blue
    def is_selected(self):
        self.colour = RED
    
    # if not selected show in blue
    def not_selected(self):
        self.colour = BLUE

# main function to be run
def main():
    # get the possible boards
    boards = boardGeneration.get_boards()
    # draw the fractal to be shown intially
    shapes = fractals.create_fractal((False, shape.Star, 4), 20, True, 19, 1.5, (255, 255, 255), 'uuu', 20)

    # list of buttons
    buttons = []
    # create button for each possible board
    for i in range(len(boards)):
        buttons.append(Button(screenWidth* (i+1)/4 - 10, 225, 100, 50, boards[i]))
    buttons[0].is_selected() # set the first button as the selected button intially
    selection = 0
    # don't take the key presses straight away so that the option of selection is open rather than accidentally selecting twice with one space press
    key_sleep = True
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
        # get state of keyboard
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
        for s in shapes: # rotate and update colour of shapes
            s.rotate_poly(1, s.get_clockwise())
            s.update_colour(3)
        for i in buttons: # draw the buttons
            i.draw(win)
        # win.blit(pygame.image.load('bcg.img'), (screenWidth/2 - 225, 100))
        # draw the text that explains the menu
        win.blit(myfont.render('Map Choice', True, WHITE), (screenWidth/2 - 50, 100))
        win.blit(smallfont.render('Board 1', True, WHITE), (screenWidth* 1/4, 250))
        win.blit(smallfont.render('Board 2', True, WHITE), (screenWidth* 2/4, 250))
        win.blit(smallfont.render('Board 3', True, WHITE), (screenWidth* 3/4, 250))
        # update the screen
        pygame.display.update()
    return choice