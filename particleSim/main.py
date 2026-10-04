import pygame

class particle:
    def __init__(self,height,velocity,elasticity,radius,vx,px):
        self.height = height
        self.velocity = velocity
        self.elasticity = elasticity
        self.radius = radius
        self.vx = vx
        self.px = px
    def nextPos(self,fps):
        self.velocity += (gravity * (1/fps))
        self.height -= (self.velocity * (1/fps))
        self.px += (self.vx * (1/fps))
        if self.px <= self.radius:
            self.px = self.radius
            self.vx *= -1 * self.elasticity
        if self.px >= (WIDTH/SCALE-self.radius):
            self.px = (WIDTH/SCALE-self.radius)
            self.vx *= -1 * self.elasticity
        if self.height <= self.radius:
            self.height = self.radius
            self.velocity = self.velocity * -1 * self.elasticity
        WORLD_HEIGHT = GROUND / SCALE
        if self.height >= WORLD_HEIGHT - self.radius:
            self.height = WORLD_HEIGHT - self.radius
            self.velocity *= -1 * self.elasticity





pygame.init() # Initialise pygame
WIDTH = 800
HEIGHT = 600
gravity = 0 #m/s

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Creates screen
pygame.display.set_caption("Grvity") # Screen Name
clock = pygame.time.Clock() # Creats clock


SCALE = 20 #Scle to drw object height
GROUND = 550 #50 pixels from bottom
RADIUS = 20

ball = particle(20,5,1,(RADIUS/SCALE),5,(WIDTH//2)/SCALE)

pygame.draw.circle(
    screen,
    (255,0,0),
    (int(ball.px*SCALE), int((GROUND - ball.height * SCALE))), #Inititil pos
    RADIUS # Rdius
)

pygame.draw.line(
    screen,
    (255,255,255),
    (0, GROUND),
    (WIDTH, GROUND),
    3
)

running = True
while running:
    for event in pygame.event.get(): #Event hndling group
        if event.type == pygame.QUIT:
            running = False
    
    ball.nextPos(60)
    screen.fill((30,30,30))
    pygame.draw.line(
        screen,
        (255,255,255),
        (0, GROUND),
        (WIDTH, GROUND),
        3
    )
    pygame.draw.circle(
        screen,
        (255,0,0),
        (int(ball.px*SCALE), int((GROUND - ball.height * SCALE))), #Inititil pos
        RADIUS # Rdius
    )
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
