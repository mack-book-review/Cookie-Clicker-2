import pygame,random, math
from pygame.locals import *


class Cookie(pygame.sprite.Sprite):

    def __init__(self,pos = None):
        super().__init__()
        self.image = pygame.image.load("Cookie.png")
        self.image = pygame.transform.smoothscale(self.image,(120,100))
        self.rect = self.image.get_rect()

        self.speed = [random.randint(-1,1),random.randint(-1,1)]
        if not pos:
            self.rect.center = (random.randint(0,500),random.randint(0,500))
        else:
            self.rect.center = pos

    def randomize_position(self):
        newX = random.randint(0,500)
        newY = random.randint(0,500)
        self.rect.center = (newX,newY)

    def handle_click(self,x,y,cookies):
        if self.rect.collidepoint(x,y):

            hit_list = pygame.sprite.spritecollide(self,cookies,False)

            if len(hit_list) > 1:
                top_cookie = hit_list[-1]

                if self is top_cookie:
                    self.randomize_position()
                    return True

            else:
                self.randomize_position()
                return True

        return False


    def update(self):

        self.rect.move_ip(self.speed)

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed[1] *= -1

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed[0] *= -1

        if self.rect.bottom > 500:
            self.rect.bottom = 500
            self.speed[1] *= -1

        if self.rect.right > 500:
            self.rect.right = 500
            self.speed[0] *= -1

    def draw(self,screen):
        screen.blit(self.image,self.rect)

