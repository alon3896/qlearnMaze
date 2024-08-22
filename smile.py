import pygame
class Smile:
    def __init__(self,x,y):
        self.xpos = x
        self.ypos = y
        self.img_path = "./smile.png"
        self.img = pygame.image.load(self.img_path)


    def add(self,screen):
        img = pygame.transform.scale(self.img,(100, 100))
        screen.blit(img, (self.xpos, self.ypos))