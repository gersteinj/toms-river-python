# import pygame module
import pygame

# Start pygame
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

cat = pygame.image.load('cat.png')
cat = pygame.transform.scale(cat, (120, 140))

# tracks whether the game is currently running
active = True

# This loop will run as long as active is True
while active:
    # get mouse position
    mouse_loc = pygame.mouse.get_pos()

    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
        # Add a line of code here to print the event
        # print(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked!")
            if event.button == 1:
                print("and it's the left button")

        if event.type == pygame.QUIT:
            active = False
    
    # display mouse location in terminal
    print(mouse_loc)
    # display cat
    screen.blit(cat, mouse_loc)

    # update the display
    pygame.display.flip()