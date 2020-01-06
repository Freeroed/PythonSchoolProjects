import pygame, random

#Инициализация PyGame
pygame.init()

#Настройки окна
window_w = 1600
window_h = 900
window = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption("Pong by Freereod")
clock = pygame.time.Clock()

#Настройки шарика
class ball:
    def __init__(self, x, y, radius, colour, speed_x, speed_y, change):
        self.x = x #Координата Х
        self.y = y #Координата У
        self.radius = radius # Радиус
        self.colour = colour #Цвет в модели RGB
        self.speed_x = float(speed_x) #Скорость по Х
        self.speed_y = float(speed_y) #Скорость по У
        self.change = change # Коэффициент ускорения
    
    #Проверка вылета за границу
    def check_range(self):
        if self.x + self.speed_x>window_w-self.radius-5:
            self.speed_x*=-1 * self.change 
        if self.x + self.speed_x<0+self.radius+5:
            self.speed_x*=-1 * self.change 
        if self.y + self.speed_y<0+self.radius+5:
            self.speed_y *=-1 * self.change
        if self.y + self.speed_y>window_h-self.radius-5:
            self.speed_y*=-1 * self.change
    #Отрисовка шарика
    def drawBall(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)
        self.x =round(self.x + self.speed_x)
        self.y =round(self.y + self.speed_y)
        self.check_range()
    
    def spawnBall(self, w, h):
        self.x = w//2
        self.y = h//2
        self.speed_x = random.randint(-20,20)
        self.speed_y = random.randint(-20,20)

run = True

bl = ball(window_w//2, window_h//2, 10, (255,0,0), random.randint(-20,20),random.randint(-20,20), 1)
#Основной цикл программы
while run:
    clock.tick(30)
    #Проверяем нажатые клавиши
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        bl.spawnBall(window_w,window_h)
    window.fill((0,0,0))
    pygame.draw.rect(window, (100,0,255), (0,0, 5, window_h))
    pygame.draw.rect(window, (100,0,255), (0,0, window_w, 5))
    pygame.draw.rect(window, (100,0,255), (window_w, window_h, -5, -window_h))
    pygame.draw.rect(window, (100,0,255), (window_w, window_h, -window_w, -5))
    bl.drawBall(window)
    pygame.display.update()