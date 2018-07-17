# import pygame module
import pygame

# Start pygame
pygame.init()

# Create a display. (400, 300) is the size of the display and should be a tuple
screen = pygame.display.set_mode((800, 600))

# NEW CODE
# load font
font = pygame.font.SysFont('garamond', 72)
# create text
text = font.render("Good morning!", True, (0, 255, 180))

# tracks whether the game is currently running
active = True

# This loop will run as long as active is True
while active:
    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            active = False
    
    screen.fill( (0, 0, 0) )
    screen.blit(text, (0, 0))

    # update the display
    pygame.display.flip()