import pygame
import random

def draw(x,y,colour):
    pygame.draw.rect(screen,colour,(x*50,y*50,50,50))

def grid():
    alt = True
    for i in range(0,11):
        for j in range(0,11):
            if alt:
                alt = False
                draw(i,j,(100,100,100))
            else:
                alt = True
                draw(i,j,(100,150,100))
def apple(snake):
    x = random.randint(0,10)
    y = random.randint(0,10)
    pos = [x,y]
    while pos in snake:
        x = random.randint(0,10)
        y = random.randint(0,10)
        pos = [x,y]
    return pos

class snake:
    def __init__(self):
        self.size = 1
        self.pos = []
        self.pos.append([5,5])
        self.direction = 1
        # 1 -> Up, 2 -> Down. 3 -> Left 4 -> Right
    def draw(self):
        count = True
        for i in self.pos:
            if count:
                draw(i[0],i[1],(255,100,100))
                count = False
            else:
                draw(i[0],i[1],(255,0,0))
    def move(self, grow):
        newPos = []
        if self.direction == 1:
            newx = self.pos[0][0] 
            newy = self.pos[0][1] - 1
            newPos.append([newx,newy])
        if self.direction == 2:
            newx = self.pos[0][0] 
            newy = self.pos[0][1] + 1
            newPos.append([newx,newy])
        if self.direction == 3:
            newx = self.pos[0][0] - 1
            newy = self.pos[0][1]
            newPos.append([newx,newy])
        if self.direction == 4:
            newx = self.pos[0][0] + 1
            newy = self.pos[0][1] 
            newPos.append([newx,newy])
        if grow:
            for i in range(0,len(self.pos)):
                newx = self.pos[i][0]
                newy = self.pos[i][1]
                newPos.append([newx,newy])
        else:
            for i in range(0,len(self.pos) - 1):
                newx = self.pos[i][0]
                newy = self.pos[i][1]
                newPos.append([newx,newy])
        self.pos = newPos
    def deth(self):
        live = True
        x = self.pos[0][0]
        y = self.pos[0][1]
        if x > 10 or x < 0:
            print("s1")
            live = False
        if y > 10 or y < 0:
            live = False
            print("s2")
        first = True
        for i in self.pos:
            if first:
                first = False
            else:
                if [x,y] == i:
                    live = False
        return live
    
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
p1 = snake()
last_move = pygame.time.get_ticks()
move_delay = 175
grow = False
applepos = apple(p1.pos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and p1.direction != 2:
                p1.direction = 1

            elif event.key == pygame.K_DOWN and p1.direction != 1:
                p1.direction = 2

            elif event.key == pygame.K_LEFT and p1.direction != 4:
                p1.direction = 3

            elif event.key == pygame.K_RIGHT and p1.direction != 3:
                p1.direction = 4

    
    screen.fill("black")
    grid()
    draw(applepos[0],applepos[1],(0,255,0))
    p1.draw()
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    current_time = pygame.time.get_ticks()
    if current_time - last_move >= move_delay:
        if p1.pos[0] == applepos:
            grow = True
        else:
            grow = False
        p1.move(grow)
        if grow:
            applepos = apple(p1.pos)
        if not p1.deth():
            running = False
        last_move = current_time
    clock.tick(60) # limits FPS to 2

pygame.quit()
