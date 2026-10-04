import pygame
import random

class ball:
    def __init__(self):
        self.x = 1280/2
        self.y = 720 / 2
        self.vx = random.randint(100,300)
        self.vy = random.randint(100,300)
        self.bounces = 0
    def nextPos(self,fps):
        self.x += self.vx * (1/fps)
        self.y += self.vy * (1/fps)
        if self.y < 10:
            self.y = 10
            self.vy *= -1
        if self.y > 710:
            self.y = 710
            self.vy *= -1
        if self.x < 10:
            p2.score += 1
            self.x = 1280/2
            self.y = 720/2
            self.vx = random.randint(100,300)
            self.vy = random.randint(100,300)
            self.bounces = 0
        if self.x > 1270:
            p1.score += 1
            self.x = 1280 / 2
            self.y = 720 /2
            self.vx = - random.randint(100,300)
            self.vy = random.randint(100,300)
            self.bounces = 0
        pygame.draw.circle(screen, (0, 255, 0), [self.x, self.y], 10, 0)

    def bounce(self,y1,y2):
        if self.x < 20:
            if self.y >= y1 and self.y <= (y1+100):
                self.x = 20
                self.vx *= -1.15
                self.bounces += 1
        if self.x > 1260:
            if self.y >= y2 and self.y <= (y2+100):
                self.x = 1260
                self.vx *= -1.15
                self.bounces += 1
class player:
    def __init__(self,number):
        if number == 1:
            self.number = 1
            self.x = 0
            self.score = 0
            self.y = 720 / 2
            self.colour = (255,0,0)
        elif number == 2:
            self.number = 2
            self.x = 1270
            self.score = 0
            self.y = 720 / 2
            self.colour = (0,0,255)
    def nextPos(self):
        if self.y > 620:
            self.y = 620
        if self.y < 0:
            self.y = 0
        pygame.draw.rect(screen,self.colour,(self.x,self.y,10,100))

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
ballA = ball()
p1 = player(1)
p2 = player(2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.y -= 10
    if keys[pygame.K_s]:
        p1.y += 10
    if keys[pygame.K_UP]:
        p2.y -= 10
    if keys[pygame.K_DOWN]:
        p2.y += 10

    screen.fill("black")

    ballA.nextPos(60)
    p1.nextPos()
    p2.nextPos()
    ballA.bounce(p1.y,p2.y)

    font = pygame.font.Font(None, 100)
    s1 = font.render(str(p1.score), True, p1.colour)
    s2 = font.render(str(p2.score), True, p2.colour)
    s3 = font.render(str(ballA.bounces), True, (255, 255, 255))
    screen.blit(s1, (100, 0))
    screen.blit(s2, (1150, 0))
    screen.blit(s3, (600, 0))
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60) # limits FPS to 60

pygame.quit()
