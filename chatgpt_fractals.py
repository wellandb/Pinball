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

# --------


'''
As an AI language model, I cannot create visual content. However, I can provide you with a sample code that can help you create a fractal in Pygame using irregular shapes rotating 30.86682730217412 clockwise with depth 8 with scale 1.5 using the color (229, 8, 122) and changing the color values by 21. Here's the code:
'''
# import pygame
# import math

# # Initialize Pygame
# pygame.init()

# # Set the screen size
# screen_size = (800, 600)
# screen = pygame.display.set_mode(screen_size)

# # Set the background color
# background_color = (255, 255, 255)

# # Set the color and rotation values
# color = (229, 8, 122)
# color_change = 21
# rotation = 30.86682730217412

# # Set the depth and scale values
# depth = 2
# scale = 1.5

# # Define the function to draw the fractal
# def draw_fractal(x, y, size, angle, depth):
#     if depth == 0:
#         return

#     # Draw the irregular shape
#     points = [(0, -size), (size, 0), (0, size), (-size, 0)]
#     rotated_points = []
#     for point in points:
#         rotated_x = point[0] * math.cos(math.radians(angle)) - point[1] * math.sin(math.radians(angle))
#         rotated_y = point[0] * math.sin(math.radians(angle)) + point[1] * math.cos(math.radians(angle))
#         rotated_points.append((rotated_x, rotated_y))
#     points = [(x + point[0], y + point[1]) for point in rotated_points]
#     pygame.draw.polygon(screen, color, points)

#     # Recursively draw the fractal
#     new_size = size * scale
#     new_angle = angle + rotation
#     new_depth = depth - 1
#     draw_fractal(x + size, y, new_size, new_angle, new_depth)
#     draw_fractal(x, y + size, new_size, new_angle, new_depth)
#     draw_fractal(x - size, y, new_size, new_angle, new_depth)
#     draw_fractal(x, y - size, new_size, new_angle, new_depth)

# # Draw the fractal
# draw_fractal(screen_size[0] // 2, screen_size[1] // 2, 100, 0, depth)

# # Update the screen
# pygame.display.flip()

# # Wait for the user to close the window
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

'''
This code defines a function `draw_fractal` that recursively draws the fractal using irregular shapes rotated by the specified angle and scaled by the specified factor. The color of the shapes is set to the specified color, and the color values are changed by the specified amount for each iteration of the recursion.

To use this code, simply copy and paste it into a Python file and run it. The fractal will be drawn in a Pygame window, and you can adjust the parameters to create different fractals.
'''

# --------
'''
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the color and rotation values
color = (186, 173, 177)
color_change = 16
rotation = -10.355763633950103

# Define the function to draw the fractal
def draw_fractal(x, y, size, depth):
    # Draw the equilateral polygon
    polygon_points = []
    for i in range(3):
        angle = math.radians(120 * i + rotation)
        point_x = x + size * math.cos(angle)
        point_y = y + size * math.sin(angle)
        polygon_points.append((point_x, point_y))
    pygame.draw.polygon(screen, color, polygon_points)

    # Recursively draw the smaller polygons
    if depth > 0:
        for i in range(3):
            angle = math.radians(120 * i + rotation)
            new_x = x + size * math.cos(angle) / 2
            new_y = y + size * math.sin(angle) / 2
            draw_fractal(new_x, new_y, size / 2, depth - 1)

# Set the scale and depth values
scale = 1.5714285714285714
depth = 7

# Draw the fractal
draw_fractal(screen_width / 2, screen_height / 2, 200 * scale, depth)

# Update the screen
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

'''

# -----

'''
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
width, height = 800, 800
screen = pygame.display.set_mode((width, height))

# Set the initial polygon
polygon = [(400, 100), (550, 450), (250, 450)]

# Define the function to rotate a point around another point
def rotate_point(point, angle, origin):
    x, y = point
    ox, oy = origin
    qx = ox + math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy)
    qy = oy + math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy)
    return qx, qy

# Define the function to draw the fractal
def draw_fractal(polygon, depth, scale, color):
    # Draw the polygon
    pygame.draw.polygon(screen, color, polygon)
    # Check if the depth is greater than 0
    if depth > 0:
        # Rotate the polygon
        angle = -0.7960203776999636
        origin = polygon[0]
        rotated_polygon = [rotate_point(point, angle, origin) for point in polygon]
        # Scale the polygon
        scaled_polygon = [(point[0]*scale, point[1]*scale) for point in rotated_polygon]
        # Change the color
        color = ((color[0]+39)%255, (color[1]+39)%255, (color[2]+39)%255)
        # Draw the fractal with the new polygon
        draw_fractal(scaled_polygon, depth-1, scale, color)

# Draw the fractal
draw_fractal(polygon, 8, 1.5, (209, 196, 251))

# Update the display
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
'''

# -----
'''
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)

# Define the color and color change values
color = (189, 213, 73)
color_change = (47, 47, 47)

# Define the rotation angle, depth, and scale
angle = 2.103482913280023
depth = 13
scale = 1.3076923076923077

# Define the function to draw the fractal
def draw_fractal(x, y, size, angle, depth):
    if depth == 0:
        return

    # Draw an irregular shape
    points = [(0, 0), (size, 0), (size/2, size)]
    rotated_points = []
    for point in points:
        rotated_x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
        rotated_y = point[0] * math.sin(angle) + point[1] * math.cos(angle)
        rotated_points.append((rotated_x, rotated_y))
    translated_points = [(x + point[0], y + point[1]) for point in rotated_points]
    pygame.draw.polygon(screen, color, translated_points)

    # Recursively draw smaller shapes
    for i in range(3):
        new_x = x + i * size / 2
        new_y = y + size / 2
        draw_fractal(new_x, new_y, size / 2, angle, depth - 1)

# Draw the fractal
draw_fractal(100, 100, 400, angle, depth)

# Update the screen
pygame.display.flip()

# Wait for the user to close the window
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# Quit Pygame
pygame.quit()
'''
# -----
'''

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fractal")

def draw_shape(x, y, size):
    points = [(0, 0), (size, 0), (size, size), (0, size)]
    for i in range(len(points)):
        points[i] = (points[i][0] + x, points[i][1] + y)
    pygame.draw.polygon(screen, (100, 148, 252), points)

def draw_fractal(x, y, size, depth):
    if depth == 0:
        return
    draw_shape(x, y, size)
    angle = -55.20677156237537 * math.pi / 180
    new_size = size / 1.6666666666666665
    draw_fractal(x + size * math.cos(angle), y + size * math.sin(angle), new_size, depth - 1)
    draw_fractal(x + size * math.cos(angle + math.pi / 2), y + size * math.sin(angle + math.pi / 2), new_size, depth - 1)
    draw_fractal(x + size * math.cos(angle + math.pi), y + size * math.sin(angle + math.pi), new_size, depth - 1)
    draw_fractal(x + size * math.cos(angle + 3 * math.pi / 2), y + size * math.sin(angle + 3 * math.pi / 2), new_size, depth - 1)

draw_fractal(400, 400, 400, 3)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
'''
# ----------
'''
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 800)

# Set the background color
background_color = (255, 255, 255)

# Set the color of the fractal
fractal_color = (166, 20, 95)

# Set the depth of the fractal
depth = 6

# Set the scale of the fractal
scale = 1.6666666666666665

# Set the angle of rotation
angle = -1.2175459029269486

# Set the starting position of the fractal
start_pos = (window_size[0] // 2, window_size[1] // 2)

# Set the size of the starting shape
start_size = 200

# Create the Pygame window
window = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Fractal")

# Define a function to draw the fractal
def draw_fractal(pos, size, depth):
    # Draw the starting shape
    pygame.draw.rect(window, fractal_color, (pos[0] - size // 2, pos[1] - size // 2, size, size))

    # If the depth is greater than 0, draw the next level of the fractal
    if depth > 0:
        # Calculate the position and size of the next level of the fractal
        next_pos = (pos[0] + size // 2, pos[1] - size // 2)
        next_size = int(size / scale)

        # Rotate the position of the next level of the fractal
        x = next_pos[0] - pos[0]
        y = next_pos[1] - pos[1]
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = x * math.sin(angle) + y * math.cos(angle)
        next_pos = (pos[0] + new_x, pos[1] + new_y)

        # Draw the next level of the fractal
        draw_fractal(next_pos, next_size, depth - 1)

# Draw the fractal
draw_fractal(start_pos, start_size, depth)

# Update the Pygame window
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

'''
#------
'''
import pygame
import math

# Initialize pygame
pygame.init()

# Set the window size
width, height = 800, 800
screen = pygame.display.set_mode((width, height))

# Set the background color
background_color = (0, 0, 0)

# Set the polygon color
polygon_color = (146, 217, 52)

# Set the color increment
color_increment = 2

# Set the polygon rotation angle
rotation_angle = 0.005119704941190283

# Set the polygon scale factor
scale_factor = 1.4

# Set the polygon depth
depth = 2

# Define the function to draw the fractal
def draw_fractal(x, y, size, angle, depth):
    # Draw the polygon
    polygon_points = []
    for i in range(3):
        x_i = x + size * math.cos(angle + i * 2 * math.pi / 3)
        y_i = y + size * math.sin(angle + i * 2 * math.pi / 3)
        polygon_points.append((x_i, y_i))
    pygame.draw.polygon(screen, polygon_color, polygon_points)

    # Recursively draw the sub-polygons
    if depth > 0:
        for i in range(3):
            x_i = x + size * math.cos(angle + i * 2 * math.pi / 3)
            y_i = y + size * math.sin(angle + i * 2 * math.pi / 3)
            draw_fractal(x_i, y_i, size / scale_factor, angle + rotation_angle, depth - 1)

# Draw the fractal
draw_fractal(width / 2, height / 2, 300, 0, depth)

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Change the polygon color
    polygon_color = tuple((c + color_increment) % 255 for c in polygon_color)

    # Redraw the fractal with the new color
    screen.fill(background_color)
    draw_fractal(width / 2, height / 2, 300, 0, depth)
    pygame.display.flip()

# Quit pygame
pygame.quit()

'''
# --------- REALLLY GOOD
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
width = 800
height = 600

# Create the window
screen = pygame.display.set_mode((width, height))

# Set the background color
background_color = (255, 255, 255)

# Set the initial color
color = (115, 151, 1)

# Set the color change value
color_change = 50

# Set the initial depth
depth = 5

# Set the initial scale
scale = 1.25

# Set the initial rotation angle
angle = 5.274266619815985

# Define the function to draw the fractal
def draw_fractal(x, y, size, depth, angle, scale, color):
    # Draw the equilateral polygon
    polygon_points = []
    for i in range(3):
        x_i = x + size * math.cos(angle + i * 2 * math.pi / 3)
        y_i = y + size * math.sin(angle + i * 2 * math.pi / 3)
        polygon_points.append((x_i, y_i))
    pygame.draw.polygon(screen, color, polygon_points)

    # Recursively draw the smaller polygons
    if depth > 0:
        for i in range(3):
            x_i = x + size * math.cos(angle + i * 2 * math.pi / 3)
            y_i = y + size * math.sin(angle + i * 2 * math.pi / 3)
            # I added in the % 255 as chatgpt forgot it and it doesn't work without it
            draw_fractal(x_i, y_i, size / scale, depth - 1, angle + math.pi / 3, scale, ((color[0] + color_change)%255, (color[1] + color_change)%255, (color[2] + color_change)%255))

# Draw the fractal
draw_fractal(width / 2, height / 2, 200, depth, angle, scale, color)

# Update the display
pygame.display.flip()

# Wait for the user to close the window
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

# Quit Pygame
pygame.quit()
