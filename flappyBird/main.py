import pygame
import random
hitbox = False
class player:
    def __init__(self):
        self.position = 360
        self.velocity = 0
    def nextPos(self,fps):
        self.velocity += (gravity / fps)
        self.position += (self.velocity / fps)
        if hitbox:
            pygame.draw.rect(screen,(255,0,0),(200,self.position,40,40))
        screen.blit(Bird, (190,self.position - 10,))

class pipe:
    def __init__(self):
        self.velocity = VELOCITY
        self.position = 1280
        self.gap = random.randint(180,420)
    def nextPos(self,fps):
        self.position -= (VELOCITY / fps)
        if hitbox:
            pygame.draw.rect(screen,(0,255,0),(self.position,0,80,self.gap))
            pygame.draw.rect(screen,(0,255,0),(self.position,(self.gap + 200),80,720))
        screen.blit(pipebot, (self.position,(self.gap + 200)))
        screen.blit(pipetop, (self.position,(self.gap - 640)))

class bckground:
    def __init__(self):
        self.position1 = 0
        self.position2 = 1280
        self.velocity = 50
    def nextPos(self,fps):
        self.position1 -= (self.velocity/fps)
        self.position2 -= (self.velocity/fps)
        if self.position1 <= -1280:
            self.position1 = 1280
            self.position2 = 0
        if self.position2 <= -1280:
            self.position2 = 1280
            self.position1 = 0
        screen.blit(background, (self.position1,0))
        screen.blit(background, (self.position2,0))
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
scale = 20
gravity = 9.8 * scale
VELOCITY = 200
running = True
bird = player()
pipes = []
p1 = pipe()
pipes.append(p1)
check = True
score = 0
scoreCheck = True
font = pygame.font.Font("freesansbold.ttf", 64)
pipebot = pygame.image.load("pipebottom.png").convert_alpha()
pipetop = pygame.image.load("pipetop.png").convert_alpha()
Bird = pygame.image.load("bird.png").convert_alpha()
background = pygame.image.load("bckground.png").convert_alpha()
b1 = bckground()

Game = True
while running:
    VELOCITY = 300 + (score * 10)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
               bird.velocity = -10*scale
    
    # fill the screen with a color to wipe away anything from last frame
    if Game:
        screen.fill("blue")
        b1.nextPos(60)
        bird.nextPos(60)
        for i in pipes:
            i.nextPos(60)
        if pipes[0].position <= (-80):
            pipes.pop(0)
            check = True
            scoreCheck = True
        if pipes[0].position <= 640 and pipes[0].position:
            if check:
                pipes.append(pipe())
                check = False

        if (pipes[0].position <= 240) and (pipes[0].position >= 160):
            if bird.position <= pipes[0].gap:
                Game = False
            if (bird.position + 40) >= (pipes[0].gap + 200):
                Game = False
        if pipes[0].position <= 160 and scoreCheck:
            score += 1
            print(score)
            scoreCheck = False
        
        # RENDER YOUR GAME HERE
        text = font.render(str(score), True, (255, 255, 255))
        screen.blit(text, (0, 0))
    else:
        screen.fill("black")
        text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(text, (360, 0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
