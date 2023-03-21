# THIS IS A SERIES OF FRACTALS CREATED BY CHAT-GPT



# Q:don't use turtle (turtle wasn't working on my computer)
# import numpy as np
# import matplotlib.pyplot as plt

# def fractal(n):
#     x = np.linspace(-2, 2, n)
#     y = np.linspace(-2, 2, n)
#     c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
#     z = np.zeros_like(c)
#     for i in range(100):
#         z = z**2 + c
#     return np.abs(z) < 2

# plt.imshow(fractal(1000), cmap=plt.cm.Blues)
# plt.axis('off')
# plt.show()

# --------------

# Q: create a fractal made out of star shapes

# Q:don't use turtle (turtle wasn't working on my computer)

# import pygame
# import math

# # Set up the window
# pygame.init()
# window_width, window_height = 800, 800
# screen = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Fractal Star")

# # Define the star shape
# def draw_star(x, y, size):
#     points = [(x, y-size), (x+size/4, y-size/4),
#               (x+size, y-size), (x+size/4, y),
#               (x+size, y+size/4), (x, y+size),
#               (x-size/4, y+size/4), (x-size, y+size),
#               (x-size/4, y), (x-size, y-size/4)]
#     pygame.draw.polygon(screen, (255, 255, 255), points, 1)

# # Recursive function to draw the fractal
# def fractal_star(x, y, size, level):
#     draw_star(x, y, size)
#     if level > 0:
#         new_size = size / math.sqrt(2)
#         fractal_star(x-size/2, y-size/2, new_size, level-1)
#         fractal_star(x+size/2, y-size/2, new_size, level-1)
#         fractal_star(x-size/2, y+size/2, new_size, level-1)
#         fractal_star(x+size/2, y+size/2, new_size, level-1)

# # Main game loop
# running = True
# level = 5
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))
#     fractal_star(window_width/2, window_height/2, 200, level)
#     pygame.display.flip()

# # Clean up the pygame module
# pygame.quit()

# --------------

# use pygame to create a fractal that repeats a polygon of various colours
# import pygame
# import random
# import math

# # Set up the window
# pygame.init()
# window_width, window_height = 800, 800
# screen = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Fractal Polygon")

# # Define the polygon shape
# def draw_polygon(x, y, size, sides, color):
#     points = []
#     for i in range(sides):
#         angle = i * 2 * math.pi / sides
#         point = (x + size * math.cos(angle), y + size * math.sin(angle))
#         points.append(point)
#     pygame.draw.polygon(screen, color, points, 0)

# # Recursive function to draw the fractal
# def fractal_polygon(x, y, size, sides, color, level):
#     draw_polygon(x, y, size, sides, color)
#     if level > 0:
#         new_size = size / 2
#         new_sides = sides #+ random.choice([-1, 1])
#         new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         fractal_polygon(x - size/2, y - size/2, new_size, new_sides, new_color, level-1)
#         fractal_polygon(x + size/2, y - size/2, new_size, new_sides, new_color, level-1)
#         fractal_polygon(x - size/2, y + size/2, new_size, new_sides, new_color, level-1)
#         fractal_polygon(x + size/2, y + size/2, new_size, new_sides, new_color, level-1)

# # Main game loop
# running = True
# level = 6
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))
#     fractal_polygon(window_width/2, window_height/2, 200, 5, (255, 255, 255), level)
#     pygame.display.flip()

# # Clean up the pygame module
# pygame.quit()

# -----

#As an AI language model, I cannot create visual content. However, I can provide you with the code to create a fractal in Pygame using equilateral polygons with sides greater than 2 rotating 2.7315064928574366 clockwise with depth 19 with scale 1.2 using the colour (6, 141, 75) and changing the colour values by 56. Here's the code:
# import pygame
# import math

# # Initialize Pygame
# pygame.init()

# # Set the window size
# WINDOW_SIZE = (800, 800)

# # Set the background color
# BACKGROUND_COLOR = (255, 255, 255)

# # Set the polygon color
# POLYGON_COLOR = (6, 141, 75)

# # Set the color change value
# COLOR_CHANGE = 56

# # Set the polygon sides
# SIDES = 3

# # Set the polygon rotation
# ROTATION = 2.7315064928574366

# # Set the polygon depth
# DEPTH = 19

# # Set the polygon scale
# SCALE = 1.2

# # Create the window
# screen = pygame.display.set_mode(WINDOW_SIZE)

# # Set the window title
# pygame.display.set_caption("Fractal")

# # Define the function to draw the fractal
# def draw_fractal(x, y, size, rotation, depth):
#     # Draw the polygon
#     polygon_points = []
#     for i in range(SIDES):
#         angle = math.radians(360 / SIDES * i + rotation)
#         x_pos = x + size * math.cos(angle)
#         y_pos = y + size * math.sin(angle)
#         polygon_points.append((x_pos, y_pos))
#     pygame.draw.polygon(screen, POLYGON_COLOR, polygon_points)

#     # Recursively draw the fractal
#     if depth > 0:
#         new_size = size * SCALE
#         new_depth = depth - 1
#         draw_fractal(x, y, new_size, rotation + ROTATION, new_depth)
#         draw_fractal(x + size * math.cos(math.radians(ROTATION)), y + size * math.sin(math.radians(ROTATION)), new_size, rotation - ROTATION, new_depth)

# # Define the function to change the polygon color
# def change_color(color):
#     new_color = []
#     for value in color:
#         new_value = value + COLOR_CHANGE
#         if new_value > 255:
#             new_value = 255
#         new_color.append(new_value)
#     return tuple(new_color)

# # Draw the fractal
# draw_fractal(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2, 200, 0, DEPTH)

# # Update the display
# pygame.display.flip()

# # Run the game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Change the polygon color
#     POLYGON_COLOR = change_color(POLYGON_COLOR)

#     # Redraw the fractal
#     screen.fill(BACKGROUND_COLOR)
#     draw_fractal(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2, 200, 0, DEPTH)
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()


# -----

# import pygame
# import math

# # Initialize pygame
# pygame.init()

# # Set the screen size
# screen_size = (800, 800)
# screen = pygame.display.set_mode(screen_size)

# # Set the background color
# background_color = (255, 255, 255)

# # Set the polygon color
# polygon_color = (40, 127, 209)

# # Set the color change value
# color_change = 10

# # Set the polygon sides and rotation angle
# sides = 3
# angle = -27.154603294513702

# # Set the fractal depth and scale
# depth = 2
# scale = 1.2

# # Define the function to draw the fractal
# def draw_fractal(x, y, size, depth):
#     # Draw the polygon
#     polygon_points = []
#     for i in range(sides):
#         angle_rad = math.radians(angle + i * 360 / sides)
#         x_i = x + size * math.cos(angle_rad)
#         y_i = y + size * math.sin(angle_rad)
#         polygon_points.append((x_i, y_i))
#     pygame.draw.polygon(screen, polygon_color, polygon_points)

#     # Recursively draw the fractal
#     if depth > 0:
#         for i in range(sides):
#             angle_rad = math.radians(angle + i * 360 / sides)
#             x_i = x + size * math.cos(angle_rad)
#             y_i = y + size * math.sin(angle_rad)
#             draw_fractal(x_i, y_i, size * scale, depth - 1)

# # Set the initial size and position of the fractal
# size = 300
# x = screen_size[0] / 2
# y = screen_size[1] / 2

# # Draw the fractal
# draw_fractal(x, y, size, depth)

# # Update the screen
# pygame.display.flip()

# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Change the polygon color
#     polygon_color = tuple((c + color_change) % 256 for c in polygon_color)

#     # Clear the screen
#     screen.fill(background_color)

#     # Draw the fractal
#     draw_fractal(x, y, size, depth)

#     # Update the screen
#     pygame.display.flip()

# # Quit pygame
# pygame.quit()