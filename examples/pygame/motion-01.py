# import pygame module
import pygame, random

# Start pygame
pygame.init()

# Create a display. (400, 300) is the size of the display and should be a tuple
screen = pygame.display.set_mode((400, 300))

# tracks whether the game is currently running
active = True

# This loop will run as long as active is True
while active:
    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # Random x and y
    x = random.randint(0, 400)
    y = random.randint(0, 300)

    # Creating rectangles
    # The first argument is where you're drawing it. Use the name of your display.
    # The second argument is the color. It's given as (red, green, blue) with a range of 0-255 for each
    # The third argument is location and size
    # Version 1 uses (x, y, width, height)
    # Version 2 uses a pygame Rect object. It's there so you'll be less confused if you see it, but don't worry about it right now
    pygame.draw.rect(screen, (20, 200, 255), (x, y, 20, 10))
    
    # How can we erase the old colors
    
    # update the display
    pygame.display.flip()
