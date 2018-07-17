# import pygame module
import pygame, random

# Start pygame
pygame.init()

# Create a display. (400, 300) is the size of the display and should be a tuple
screen = pygame.display.set_mode((400, 300))

# tracks whether the game is currently running
active = True

# Coordinates for rectangle
x = 10
y = 10
# Color
color = (80, 200, 255)

# Create clock
clock = pygame.time.Clock()

# This loop will run as long as active is True
while active:
    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    
    # NEW CODE
    # Check to see if a key is pressed
    pressed = pygame.key.get_pressed()
    # If a key is pressed and it's the specified key, modify coordinates
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    # What are the problems and how can we resolve them?
    # It's okay if you don't know the code to do it yet



    # NEW CODE
    # Fill the background before drawing the rectangle
    screen.fill((0, 0, 0))

    # draw a rectangle. Note that the x and y coordinates are now variables so they can change
    pygame.draw.rect(screen, color, (x, y, 20, 10))

    # update the display
    pygame.display.flip()
    clock.tick(60)