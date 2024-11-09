import pygame

pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw any color rectangle at position (250, 20) with a width of 25 and height of 75. surface, color, dimensions	

    rectangle = pygame.draw.rect(screen, (0, 133, 255), (250, 20, 25, 75))

    # Draw any color circle at position (275, 40) with a radius of 10. surface, color, center point, radius

    circle = pygame.draw.circle(screen, (0, 133, 255), (275, 40), 10)

    # Draw any color line at starting position (325, 32) end position (375, 32) and a width of 5. surface, color, start point, end point, width

    line = pygame.draw.line(screen, (0, 133, 255), (325, 32), (375, 32), 5)

    # Draw any color polygon surface, color, list of points

    yellow_triangle = pygame.draw.polygon(screen, (0, 133, 255), [(10, 300), (40, 200), (70, 300) ])

    # Draw a target

    #target1 = pygame.draw.circle(screen, (255, 0, 0), (255, 255), 100)
    #target2 = pygame.draw.circle(screen, (0, 0, 0), (255, 255), 70)
    #target3 = pygame.draw.circle(screen, (255, 0, 0), (255, 255),50)
    #target4 = pygame.draw.circle(screen, (0, 0, 0), (255, 255), 30)
    #target5 = pygame.draw.circle(screen, (255, 0, 0), (255, 255), 10)

    pygame.display.update()
    clock.tick(60)