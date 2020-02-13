#! python3

import pygame           
import os
import random
import time


pygame.init()

WIDTH = 600    # X
HEIGHT = 600   # Y


screen = pygame.display.set_mode((WIDTH, HEIGHT))

#for k in range(10):
#    screen.fill((20 * k, 20 * k,  20 * k))
#    pygame.display.update()
#    time.sleep(1)
#    rectum = pygame.Rect(10 + 3 * k, 20, 30, 40)
#    pygame.draw.rect(screen, (20 *k, 0, 0), rectum)
#    pygame.display.update()
#    time.sleep(1)
#pygame.quit()


#size = 3

def strender(txt="", size=20, position=None, font="Arial"):
    """ """    
    ttf = pygame.font.SysFont("Arial", size=20)
    # rend = ttf.render(text=txt, antialias=1, color=(255, 100, 100), background=None)  # TypeError: render() takes no keyword arguments
    rend = ttf.render(txt, 1, (255, 100, 100), None)
    if position is None:
        x, y, w, h = rend.get_rect()
        position = ((WIDTH - w)/2, (HEIGHT - h)/2)
    return rend, position

rends={"press_space": strender("Press space to begin"),
       "logo": (pygame.image.load(os.path.join("HelicopterLogo.png")), (80, 30)),
       "menu": strender("menu")}

#%%

class Obstacle():
    
    def __init__(self, x, width):
        self._x = x
        self.width = width
        self.y_up = 0
        self.height_up = random.randint(150, 250)
        self.gap = 200
        self.y_bottom = self.height_up + self.gap
        self.height_bottom = HEIGHT - self.y_bottom
        self.color = (160, 140, 190)
        self.shape_up = pygame.Rect(self._x, self.y_up, self.width, self.height_up)
        self.shape_bottom = pygame.Rect(self._x, self.y_bottom, self.width, self.height_bottom)
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.shape_up, 0)
        pygame.draw.rect(screen, self.color, self.shape_bottom, 0)
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        self._x = new_x
        self.shape_up.x = self._x
        self.shape_bottom.x = self._x
        
    def move(self, v):
        self.x -= v

#%%

NOBST = 20
W = WIDTH/NOBST   
obstacles = [Obstacle(i * W, W) for i in range(NOBST + 1)]

SHOW = "game"

while True:
    
    #print([o.x for o in obstacles])
    
    time.sleep(.1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            break
    
    screen.fill((100, 100, 100))
    
    if SHOW=="menu":
        screen.blit(*rends["logo"])
        screen.blit(*rends["press_space"])
        
    elif SHOW=="game":
        for obst in obstacles:
            obst.move(1)
            obst.draw()
        for obst in obstacles:
            if obst.x <= -obst.width:
                obstacles.remove(obst)
                obstacles.append(Obstacle(W*20, W))
        
    pygame.display.update()


