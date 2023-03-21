# selection of all the maps
from settings import *
import boardGeneration
import fractals
import shape


def main():
    boards = boardGeneration.get_boards()
    shapes = fractals.create_fractal((False, shape.Star), 20, True, 19, 1.5, (255, 255, 255), 'uuu', 20)

    buttons = []
    for i in range(boardGeneration.get_boards()):
        buttons.append(menu.Button(screenWidth* i/len(boardGeneration.get_boards()) - 10, 225, 100, 50, ))
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