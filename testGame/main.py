import pygame

pygame.init()
window_w = 1600
window_h = 900
window = pygame.display.set_mode((window_w,window_h))

pygame.display.set_caption("Test game")

gamer_x = 100
gamer_y = 100
gamer_weight = 30
gamer_height = 60
gamer_speed=10

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and gamer_x > 50:
        gamer_x -= gamer_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and gamer_x<window_w-gamer_weight-50:
        gamer_x += gamer_speed
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and gamer_y>50:
        gamer_y -= gamer_speed    
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and gamer_y<window_h-gamer_height-50:
        gamer_y += gamer_speed

    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (gamer_x,gamer_y, gamer_weight, gamer_height))
    pygame.display.update()    

pygame.quit()