import pygame, sys, random, time
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 640
WINDOWHEIGHT = 640
Window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption("game")

Stone0 = pygame.image.load('Stone0.png')
Stone1 = pygame.image.load('Stone1.png')
Stone2 = pygame.image.load('Stone2.png')
Stone3 = pygame.image.load('Stone3.png')
Stone4 = pygame.image.load('Stone4.png')
Stone5 = pygame.image.load('Stone5.png')
Stone6 = pygame.image.load('Stone6.png')
Stone7 = pygame.image.load('Stone7.png')
Stone8 = pygame.image.load('Stone8.png')
Stone9 = pygame.image.load('Stone9.png')
Stone10 = pygame.image.load('Stone10.png')
Stone11 = pygame.image.load('Stone11.png')
Stone12 = pygame.image.load('Stone12.png')
Stone13 = pygame.image.load('Stone13.png')
Stone14 = pygame.image.load('Stone14.png')
Stone15 = pygame.image.load('Stone15.png')
Wood = pygame.image.load('Wood.png')
Chain = pygame.image.load('Chain.png')
Lantern = pygame.image.load('Lantern.png')
Banner = pygame.image.load('Banner.png')
Brick = pygame.image.load('Brick.png')

Spell1 = pygame.image.load('Spell1.png')

pygame.display.set_icon(Banner)

Level = [[6,6,6,6,0,0,6,6,6,6,0,0,6,6,6,6,0,0,6,6,6,6],
         [6,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,6],
         [6,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,6],
         [6,1,1,1,0,0,0,5,0,1,0,0,1,0,5,0,0,0,1,1,1,6],
         [6,1,1,1,0,0,0,0,0,3,0,0,3,0,0,0,0,0,1,1,1,6],
         [6,1,0,2,0,0,0,7,0,4,0,0,3,0,0,0,0,0,2,0,1,6],
         [6,1,0,2,0,0,0,0,0,0,0,0,4,0,0,0,0,0,2,0,1,6],
         [6,1,0,2,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2,0,1,6],
         [0,0,0,2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,2,0,0,0],
         [0,0,0,2,0,0,0,1,1,0,0,0,0,1,1,0,0,0,2,0,0,0],
         [0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
         [6,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,6],
         [6,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,1,6],
         [6,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1,6],
         [6,1,0,3,0,1,1,1,0,0,0,0,0,0,1,1,1,0,4,0,1,6],
         [6,1,0,4,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,1,6],
         [6,1,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,1,6],
         [6,1,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,1,6],
         [6,1,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,1,6],
         [6,1,1,1,0,0,2,0,0,1,0,0,1,0,0,2,0,0,1,1,1,6],
         [6,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,6],
         [6,6,6,6,0,0,6,6,6,6,0,0,6,6,6,6,0,0,6,6,6,6]]
         

Tiles = []
Attacks = []
Particles = []
NoMoveTiles = [1,6]

class TILE(object):
    def __init__(self,x,y,i,q,tile):
        self.x = x 
        self.y = y
        self.X = i
        self.Y = q
        self.R = pygame.Rect(self.x,self.y,32,32)
        self.T = tile
        if self.T == 1:
            if Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone0
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone5
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone4
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone3
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone2
            
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone6
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone7
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone8
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone9
            
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone10
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone11
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone12
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone13
            
            elif Level[self.X][self.Y-1] != 1 and Level[self.X][self.Y+1] != 1 and Level[self.X-1][self.Y] == 1 and Level[self.X+1][self.Y] == 1 and self.T == 1:
                self.I = Stone14
            elif Level[self.X][self.Y-1] == 1 and Level[self.X][self.Y+1] == 1 and Level[self.X-1][self.Y] != 1 and Level[self.X+1][self.Y] != 1 and self.T == 1:
                self.I = Stone15
   
            else:
                self.I = Stone1
        elif self.T == 0:
            self.I = Stone0
        elif self.T == 2:
            self.I = Wood
        elif self.T == 3:
            self.I = Chain
        elif self.T == 4:
            self.I = Lantern
        elif self.T == 5:
            self.I = Banner
        elif self.T == 6:
            self.I = Stone1
        elif self.T == 7:
            self.I = Brick
        self.SI = pygame.transform.scale(self.I,(32,32))
    def draw(self,Window):
        if self.T != 0:
            Window.blit(self.SI,self.R)
            

class ATTACK(object):
    def __init__(self,x,y,Atype,Dir):
        self.x = x 
        self.y = y
        self.T = Atype
        if self.T == 0:
            self.I = Spell1
            self.Time = random.randint(-3,0)
            self.R = pygame.Rect(self.x,self.y,16,16)
            self.SI = pygame.transform.scale(self.I,(random.randint(13,20),random.randint(13,20)))
            self.MS = random.randint(4,6)
            self.D = Dir
    def draw(self,Window):
        Window.blit(self.SI,self.R)
        
class PARTICLE(object):
        def __init__(self,x,y):
            self.x = x + random.randint(-5, 5)
            self.y = y + random.randint(-10, 10)
            self.T = 8
            self.S = random.randint(3, 8)
            self.C = ((0,0,random.randint(140,160)))
            self.R = pygame.Rect(self.x, self.y, self.S, self.S)
            
        def draw(self,Window):
            for Particle in Particles:
                pygame.draw.rect(Window, self.C, self.R)
            

for i in range(0,len(Level)):
    for q in range(0,len(Level[i])):
        x = q * 32 - 32
        y = i * 32 - 32
        tile = Level[i][q]
        Tiles.append(TILE(x,y,i,q,tile))
g = 0


player = pygame.Rect(300,300,22,40)
playerI = pygame.image.load('Fighter1right.png')
playerSI = pygame.transform.scale(playerI,(58,58))
AttackleftI = pygame.image.load('Fighter1attackleft.png')
AttackrightI = pygame.image.load('Fighter1attackright.png')
AttackleftSI = pygame.transform.scale(AttackleftI,(58,58))
AttackrightSI = pygame.transform.scale(AttackrightI,(58,58))
attack = False
Dir = 0

Fighter1R = pygame.image.load('Fighter1right.png')
Fighter1L = pygame.image.load('Fighter1left.png')


Fighter1I = [Fighter1R,Fighter1L]



YSPEED = 0
XSPEED = 0

MOVELEFT = False
MOVERIGHT = False
Dash = False
DashTime = 20
DashX = 0
DashY = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit  
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit
            if event.key == K_a:
                MOVELEFT = True
                MOVERIGHT = False
                Dir = 1
            if event.key == K_d:
                MOVERIGHT = True
                MOVELEFT = False
                Dir = 0
            if event.key == K_LSHIFT and DashTime == 20:
                if DashX or DashY != 0:
                    Dash = True
            if event.key == K_s:
                attack = True
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
                x = player.centerx
                y = player.top + random.randint(0,15)
                Atype = 0
                Attacks.append(ATTACK(x,y,Atype,Dir))
            if event.key == K_w:
                PU = False
                player.top += 8
                for Tile in Tiles:
                    if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                        PU = True
                if PU == True:
                    player.top -= 8
                    YSPEED = -5
                else:
                    player.top -= 8
        if event.type == KEYUP:
            if event.key == K_a:
                MOVELEFT = False
            if event.key == K_d:
                MOVERIGHT = False
            if event.key == K_LSHIFT:
                Dash = False
                
    if MOVELEFT == True:
        XSPEED += -1
    if MOVERIGHT == True:
        XSPEED += 1
        
    
    Window.fill((0,0,0))
    
    

    
    
    
    
    
    playerI = Fighter1I[Dir]
    
    playerSI = pygame.transform.scale(playerI,(58,58))
    
    if YSPEED > 0:
        PD = False
        player.top += YSPEED
        for Tile in Tiles:
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                PD = True
                player.bottom = Tile.R.top
                DashTime = 20
        if PD == True:
            YSPEED = 0
    elif YSPEED < 0:
        PU = False
        player.top -= 10
        for Tile in Tiles:
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                PU = True     
        if PU == True:
            player.top += 10
            YSPEED = 0
        else:
            player.top += 10
            player.top += YSPEED
            
    if XSPEED < 0 and player.left > 0:
        PL = False
        player.right += XSPEED
        for Tile in Tiles:
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                PL = True
                player.left = Tile.R.right
                
        if PL == True:
            XSPEED = 0
    if XSPEED > 0 and player.right < WINDOWWIDTH:
        PR = False
        player.right += XSPEED
        for Tile in Tiles:
            if Tile.R.colliderect(player) and Tile.T in NoMoveTiles:
                PR = True
                player.right = Tile.R.left
                
                
        if PR == True:
            XSPEED = 0
        
                    
    
    for Tile in Tiles:
        Tile.draw(Window)
    
    for Attack in Attacks:
        if Attack.T == 0:
            Attack.Time += 1
            if Attack.D == 1:
                Attack.R.x -= Attack.MS - XSPEED
            elif Attack.D == 0:
                Attack.R.x += Attack.MS + XSPEED
            Attack.draw(Window)
            if Attack.Time > 10:
                Attacks.pop(Attacks.index(Attack))
                
        
    #pygame.draw.rect(Window,(255,0,0),player)
                
    x = player.centerx
    y = player.centery
    if XSPEED != 0 or YSPEED > 1 or YSPEED < -1:
        Particles.append(PARTICLE(x,y))
        Particles.append(PARTICLE(x,y))
                
    for Particle in Particles:
        Particle.draw(Window)
        Particle.T -= 1
        if Particle.T < 0:
            Particles.pop(Particles.index(Particle))
    
    Window.blit(playerSI,(player.x,player.y))
    if attack == True:
        if Dir == 1:
            Window.blit(AttackleftSI,(player.x-2,player.y))
        elif Dir == 0:
            Window.blit(AttackrightSI,(player.x-2,player.y))
            
    
    if YSPEED < 7.5:   
        YSPEED += .15
    
    if XSPEED != 0:
        if XSPEED > .5:
            if XSPEED > 3 and Dash == False:
                XSPEED = 3
            XSPEED -= .1
        elif XSPEED < -.5:
            if XSPEED < -3  and Dash == False:
                XSPEED = -3
            XSPEED += .1
        else:
            XSPEED = 0
    
    if player.y > 640:
        player.bottom = 0
        
    if len(Attacks) == 0:
        attack = False
    
    
    pygame.display.update()
    mainClock.tick(60)




