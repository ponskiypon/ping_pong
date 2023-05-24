import pygame
import random
pygame.init()
class GameSprite():
    def __init__(self,image,x,y,shir,vis):
        self.x = x
        self.y = y
        self.shir = shir
        self.vis = vis
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect((self.x,self.y,self.shir,self.vis))

    def draw(self):
        self.kartinka = pygame.transform.scale(self.image,(self.shir,self.vis))
        mw.blit(self.kartinka,(self.x,self.y))


class Player(GameSprite):
    def move(self,speed):
        
        self.speed = speed
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        if key[pygame.K_DOWN] and self.rect.y < mw_y - self.vis:
            self.rect.y += self.speed
    
        
            
        
    def move2(self,speed):
        
        self.speed = speed
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        if key[pygame.K_s] and self.rect.y < mw_y - self.vis:
            self.rect.y += self.speed


class Balls(GameSprite):
    def __init__(self,image,x,y,shir,vis,speed_x,speed_y):
        self.x = x
        self.y = y
        self.shir = shir
        self.vis = vis
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect((self.x,self.y,self.shir,self.vis))
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect) == True:
            self.speed_x *= -1
        if self.rect.colliderect(top.rect) or self.rect.colliderect(bottom.rect) == True:
            self.speed_y *= -1

        if self.rect.x > mw_x:
            self.rect.x = mw_x/2
            self.rect.y = mw_y/2
            rand = random.randint(1,2)
            if rand == 1:
                self.speed = -3
            else:
                self.speed = 3
            score[0] += 1

        
        if self.rect.x < 0:
            self.rect.x = mw_x/2
            self.rect.y = mw_y/2
            rand = random.randint(1,2)
            if rand == 1:
                self.speed = -3
            else:
                self.speed = 3
            score[1] += 1


mw_x = 700
mw_y = 500
mw_size = (700,500)

mw = pygame.display.set_mode(mw_size)

clock = pygame.time.Clock()
fps = 60

game = True

score = [0,0]

font = pygame.font.Font(None,100)

                        
player1 = Player('f.png',20,80,30,100)
player2 = Player('f.png',mw_x-(20+player1.shir),mw_y-player1.vis,30,100)
ball = Balls('f.png',mw_x/2,mw_y/2,50,50,3,3)
bg = GameSprite('f.png',0,0,mw_x,mw_y)
bottom = GameSprite('f.png',0,mw_y,mw_x,200)
top = GameSprite('f.png',0,-200,mw_x,200)
while game:
    player1.x = player1.rect.x
    player1.y = player1.rect.y
    player2.x = player2.rect.x
    player2.y = player2.rect.y
    ball.x = ball.rect.x
    ball.y = ball.rect.y
    
    text1 = font.render(str(score[0]),30,(255,255,255))
    text2 = font.render(str(score[1]),30,(255,255,255))
    
    bg.draw()
    top.draw()
    bottom.draw()
    mw.blit(text1,(0,0))
    mw.blit(text2,(mw_x-50,0))
    
    player1.draw()
    player1.move2(10)
    player2.draw()
    player2.move(10)
    ball.draw()
    ball.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(60)







pygame.quit()
