import pygame

pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen = pygame.display.set_mode((500, 500))

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Workspace begin
    '''
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LCTRL] == 1:
        if keystate[pygame.K_UP] == 1:
            target1 = pygame.draw.circle(screen, (255, 0, 0), (255, 255), 100)
            target2 = pygame.draw.circle(screen, (0, 0, 0), (255, 255), 70)
            target3 = pygame.draw.circle(screen, (255, 0, 0), (255, 255),50)
            target4 = pygame.draw.circle(screen, (0, 0, 0), (255, 255), 30)
            target5 = pygame.draw.circle(screen, (255, 0, 0), (255, 255), 10)
        if keystate[pygame.K_DOWN] == 1:
            clear = pygame.draw.circle(screen, (0, 0, 0), (255, 255), 100)
    if keystate[pygame.K_] == 1:
            pygame.quit()
    '''
    
    keystate = pygame.key.get_pressed()
    #if up arrow, then draw a red box
    if keystate[pygame.K_UP]:
        rectangle = pygame.draw.rect(screen, (255, 0, 0), (390, 10, 100, 50))
    #if down arrow, then draw a green box
    elif keystate[pygame.K_DOWN]:
        rectangle = pygame.draw.rect(screen, (0, 255, 0), (100, 10, 50, 50))
    #if left arrow, then draw a blue box
    elif keystate[pygame.K_LEFT]:
        rectangle = pygame.draw.rect(screen, (0, 0, 255), (300, 200, 70, 50))
    #if right arrow, then draw a white box
    elif keystate[pygame.K_RIGHT]:
        rectangle = pygame.draw.rect(screen, (255, 255, 255), (250, 40, 45, 50))
    
    keystate = pygame.key.get_pressed()
    #if up arrow, then draw a red box
    if keystate[pygame.K_w]:
        red = pygame.draw.circle(screen, (255, 0, 0), (120, 100), 20)
    #if down arrow, then draw a green box
    elif keystate[pygame.K_s]:
        green = pygame.draw.circle(screen, (0, 255, 0), (480, 100), 30)
    #if left arrow, then draw a blue box
    elif keystate[pygame.K_a]:
        blue = pygame.draw.circle(screen, (0, 0, 255), (480, 400), 40)
    #if right arrow, then draw a white box
    elif keystate[pygame.K_d]:
        white = pygame.draw.circle(screen, (255, 255, 255), (120, 400), 50)

    # Workspace end

    pygame.display.update()
    clock.tick(60)
