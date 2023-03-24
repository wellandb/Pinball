install the relevant python modules:
pygame, random, sys, math, cmath, numpy, time, openai, chat_api, pygame_widgets

In order to run:
run menu.py

The controls are then the arrow keys to get to the button that you want to choose and space button to choose the option.
Pinball will open up the first board and you then have to choose the parameters by either clicking the position with your mouse or pressing k to type the parameters into the terminal. (previous paramets are stored in the paramete_log.txt file)
This is then repeated for working out the velocity of the ball.
The pinball will then travel through the simulation and once it exits the map through the bottom of the screen the fractal will be shown on screen.
The fractal can be zoomed in or out using the up and down arrow keys.
If chat gpt has been enabled the chat gpt fractal will be shown once the fractal is closed

The map menu option on the menu will give a choice of map which when the space is pressed will generate the map chosen.

The fractals option will open an interactive fractal menu where the sliders can be changed in order to change the fractal shown. To show the new fractal press the space button.

To get the chat gpt fractals you must go to chat gpt and generate your API key.
This key can then be placed into the API variable of the chat_api.py file.
There is also a different variable called chat_query which stores a boolean value where True = run the chat gpt query and False doesn't run the query.

Background image sources:
neon_L:
https://pngtree.com/freebackground/modern-double-color-futuristic-neon-background_1181573.html

galaxy background:
dall-E

pixel sky:
https://caniaeast.itch.io/simple-sky-pixel-backgrounds/download/eyJleHBpcmVzIjoxNjc5NDg0NzUxLCJpZCI6NzY1NzU4fQ%3d%3d%2eRKZoltcn3PNY%2b3oyKgoCPof5XSs%3d


