# import pygame module
import pygame, random

# Start pygame
pygame.init()

# Create a display. (400, 300) is the size of the display and should be a tuple
screen = pygame.display.set_mode((400, 300))

# tracks whether the game is currently running
active = True

# NEW CODE
# used to determine color of rectangle
is_red = True

# This loop will run as long as active is True
while active:
    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
        # NEW CODE
        # Watch for key presses, and react to pushing any key
        if event.type == pygame.KEYDOWN:
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:    # This version only reacts if space is pressed
            # Assign is_red the opposite of its value
            is_red = not is_red
        if event.type == pygame.QUIT:
            active = False

    # NEW CODE
    # If is_red is True, create the color variable and assign it a tuple representing red
    if is_red:
        color = (255, 0, 0)
    # If not, create variable and assign it a tuple representing blue
    else:
        color = (0, 0, 255)

    # MODIFIED CODE
    # draw a rectangle. Note that I've replaced the color with the variable named color
    pygame.draw.rect(screen, color, (10, 200, 20, 10))

    # update the display
    pygame.display.flip()