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

    # These two lines create rectangles
    # The first argument is where you're drawing it. Use the name of your display.
    # The second argument is the color. It's given as (red, green, blue) with a range of 0-255 for each
    # The third argument is location and size
    # Version 1 uses (x, y, width, height)
    # Version 2 uses a pygame Rect object. It's there so you'll be less confused if you see it, but don't worry about it right now
    pygame.draw.rect(screen, (20, 200, 255), (10, 200, 20, 10))
    pygame.draw.rect(screen, (120, 30, 255), pygame.Rect(30, 30, 50, 80))
    
    # NEW CODE
    # Everything we've learned so far can be used here
    # for each value of x from 0 to 400, counting by 20s...
    for x in range(0, 400, 20):
        # draw a rectangle at (x, 0) with a size of (20, 100), and fill it with a random shade of purple
        pygame.draw.rect(screen, (random.randint(0, 100), 0, random.randint(100, 255)), (x, 0, 20, 100))


    # update the display
    pygame.display.flip()