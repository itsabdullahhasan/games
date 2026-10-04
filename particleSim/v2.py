import pygame, random, math
class particle:
    def __init__(self,height,velocity,elasticity,radius,vx,px,):
        self.height = height
        self.velocity = velocity
        self.elasticity = elasticity
        self.radius = radius
        self.vx = vx
        self.px = px
        self.check = False
        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def nextPos(self,fps):
        if self.check:
            self.vx *= friction
            self.velocity += (gravity * (1/fps))
            self.velocity *= friction
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
friction = 1
fps = 30

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Creates screen
pygame.display.set_caption("Grvity") # Screen Name
clock = pygame.time.Clock() # Creats clock


SCALE = 20 #Scle to drw object height
GROUND = 550 #50 pixels from bottom
RADIUS = 20

pygame.draw.line(
    screen,
    (255,255,255),
    (0, GROUND),
    (WIDTH, GROUND),
    3
)

running = True
plcement = True
direction = True
items = []
while running:
    for event in pygame.event.get(): #Event hndling group
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if plcement == True and direction == True:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                world_x = mouse_x / SCALE
                world_height = (GROUND - mouse_y) / SCALE

                ball = particle(world_height, 0, 1, RADIUS/SCALE, 0, world_x)
                items.append(ball)
                plcement = False
            elif plcement == False:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x = mouse_x / SCALE
                world_height = (GROUND - mouse_y) / SCALE
                items[-1].vx = (world_x - items[-1].px)
                items[-1].velocity = -((world_height - items[-1].height))
                items[-1].check = True
                plcement = True

    for i in items:
        i.nextPos(fps)

    #Collision Prt
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            b1 = items[i]
            b2 = items[j]
            #Check if collide
            distnce = math.sqrt((b2.height - b1.height)**2 + (b2.px - b1.px)**2)
            if distnce <= (b1.radius+b2.radius):
                overlap = b1.radius + b2.radius - distnce
                dx = (b2.px -b1.px) / distnce
                dy = (b2.height - b1.height) / distnce
                items[i].px -= dx * overlap / 2
                items[i].height -= dy * overlap / 2
                items[j].px += dx * overlap / 2
                items[j].height += dy * overlap / 2
                v1 = items[i].velocity
                v2 = items[i].vx
                items[i].velocity = b2.velocity
                items[i].vx = b2.vx
                items[j].velocity = v1
                items[j].vx = v2

    #Drwing prt     
    screen.fill((30,30,30))
    for i in items:
        pygame.draw.circle(
        screen,
        i.colour,
        (int(i.px*SCALE), int((GROUND - i.height * SCALE))), #Inititil pos
        RADIUS # Rdius
        )
    pygame.draw.line(
        screen,
        (255,255,255),
        (0, GROUND),
        (WIDTH, GROUND),
        3
    )
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
