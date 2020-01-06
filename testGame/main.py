import pygame

pygame.init()

window = pygame.display.set_mode((1600,900))

pygame.display.set_caption("Test game")

gamer_x = 100
gamer_y = 100
gamer_weight = 30
gamer_height = 60
gamer_speed=1

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] | keys[pygame.K_a]:
        gamer_x -= gamer_speed
    if keys[pygame.K_RIGHT] | keys[pygame.K_d]:
        gamer_x += gamer_speed
    if keys[pygame.K_UP] | keys[pygame.K_w]:
        gamer_y -= gamer_speed    
    if keys[pygame.K_DOWN]| keys[pygame.K_s]:
        gamer_y += gamer_speed

    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (gamer_x,gamer_y, gamer_weight, gamer_height))
    pygame.display.update()    

pygame.quit()