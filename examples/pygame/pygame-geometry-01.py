import pygame

# VARIABLES

active = True

# Now we can refer to the width and height easily
screen_width = 800
screen_height = 600

# Create display
screen = pygame.display.set_mode( (screen_width, screen_height) )

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    
    # DRAW THINGS
    for y in range(0, screen_height, 3):
        # Lines
        pygame.draw.line(screen, (200, 0, 255), (0, y), (10, y))

    # polygon
    pygame.draw.polygon(screen, (255, 0, 0), [(25, 5), (75, 5), (95, 40), (45, 40)])

    # circle
    pygame.draw.circle(screen, (100, 200, 255), (int(screen_width/2), int(screen_height/2)), 100)

    # ellipse
    pygame.draw.ellipse(screen, (50, 50, 50), (screen_width * .3, screen_height * .4, 50, 100))

    # Updae) the display
    pygame.display.flip()