import pygame
from random import randint, randrange

class snake(object):
    def __init__(self, segments,speed_x,speed_y):
        self.head = head
        self.segments = segments
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, wind):
        self.update()
        self.head.draw(wind)
        for segmen in self.segments:
            segmen.draw(wind)
    def checking(self):
        answer = True
        for i in range(2,len(self.segments)-1):
            if not self.segments[0].check_contakt(self.segments[i]):
                return False
        return answer

    def update(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].x = self.segments[i-1].x
            self.segments[i].y = self.segments[i-1].y
        self.segments[0].x += self.speed_x
        self.segments[0].y += self.speed_y
    def add(self):
        temp = self.segments[-1]
        self.segments.append(segment(temp.x,temp.y,temp.color))
class segment(object):
    def __init__(self, x,y,colour):
        self.x=x
        self.y=y
        self.color = colour

    

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 10)

    def check_contakt(self, other):
        answer = True
        if (self.x == other.x and self.y == other.y):
            answer = False
        return answer

#Умираем если трогаем границу
def chek_dead(snake_head, win_w, win_h):
    if snake_head.x-10<0:
        return False
    elif snake_head.x+10>win_w: return False
    elif snake_head.y-10<0: return False
    elif snake_head.x+10>win_h: return False 
    else: return True

#Если дотрагиваемся до границы, телепортируемся
def teleport(snake_head, win_w, win_h, spd_x,spd_y):
    if snake_head.x-10<0:
        snake_head.x = win_w-10
    elif snake_head.x>win_w: 
        snake_head.x = 0+10
    elif snake_head.y-10<0: 
        snake_head.y = win_h-10
    elif snake_head.y+10>win_h: 
        snake_head.y = 0+10
    return snake_head


def check_food_spawn(x,y,snk):
    for snake_seg in snk.segments:
        if (x==snake_seg.x and y == snake_seg.y):
            return False
    return True

def generate_food(snk):
    x = randrange(1,window_w//20,2)*10
    y = randrange(1,window_h//20,2)*10
    while not check_food_spawn(x,y,snk):
        x = randrange(1,window_w//20,2)*10
        y = randrange(1,window_h//20,2)*10
    return segment(x,y,(0,0,255))
#Настройки окна
window_w = 500
window_h = 500
window = pygame.display.set_mode((window_w,window_h))
clock = pygame.time.Clock()
run = True
tick = 1
game_speed=1

#Длинна и полжение змеи вначале
head = segment(70,50, (255,0,0))
seg = segment(50,50, (255,255,255))
seg2 = segment(50,30, (255,255,0))
seg3 = segment(50,10, (255,255,0))
sn = snake([head,seg,seg2, seg3],20,0)

#Начальная генерация еды
food = generate_food(sn)

#Основной цикл игры
while run:
    clock.tick(30)
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    if tick == 31: tick = 1 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #sn.segments[0]=teleport(sn.segments[0], window_w, window_h, sn.speed_x, sn.speed_y)
    if tick%3 == 0 :
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and sn.speed_y==0:
            sn.speed_x=0
            sn.speed_y=20
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and sn.speed_y==0:
            sn.speed_x=0
            sn.speed_y=-20
        if (keys[pygame.K_LEFT] or keys[pygame.K_a])and sn.speed_x==0:
            sn.speed_x=-20
            sn.speed_y=0
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d])and sn.speed_x==0:
            sn.speed_x=20
            sn.speed_y=0
        if (keys[pygame.K_g]):
            sn.add()
        window.fill((0,0,0))
        sn.draw(window)
        food.draw(window)
        run = sn.checking()
        run = chek_dead(sn.segments[0],window_w, window_h)
        if not(sn.segments[0].check_contakt(food)):
            food = generate_food(sn)
            sn.add()
    pygame.display.update()
    tick+=1