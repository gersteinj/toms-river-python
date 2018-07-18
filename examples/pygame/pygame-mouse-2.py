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

is_draggable = True
cat_loc = (0, 0)

# This loop will run as long as active is True
while active:
    screen.fill((0, 0, 0))
    # get mouse position
    mouse_loc = pygame.mouse.get_pos()

    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
        # Add a line of code here to print the event
        # print(event)

        # If left mouse button is clicked, toggle is_draggable
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_draggable = not is_draggable

        if event.type == pygame.QUIT:
            active = False
    
    # display mouse location in terminal
    print(mouse_loc)

    # Only change cat location if is_draggable is true
    if is_draggable:
        cat_loc = mouse_loc
    # display cat
    screen.blit(cat, cat_loc)

    # update the display
    pygame.display.flip()