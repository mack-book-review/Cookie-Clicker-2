import pygame
from pygame.locals import *
from cookie import Cookie

pygame.init()
pygame.font.init()

size = (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
clicks = 0
cps = 0

font = pygame.font.SysFont("Helvetica",20)
cookies = pygame.sprite.Group()

WHITE = (255,255,255)
BLUE = (0,0,255)

def main():
    global clicks,cps
    for i in range(10):
        cookies.add(Cookie())

    text = font.render("Clicks: 0",True,BLUE)
    text_rect = text.get_rect()
    text_rect.center = (width/2,50)

    cps_text = font.render("Clicks per Second: 0",True,BLUE)
    cps_text_rect = cps_text.get_rect()
    cps_text_rect.center = (width/2,150)

    while True:
        clock.tick(60)

        elapsed_time = pygame.time.get_ticks()//1000
        if elapsed_time > 0:
            cps = round(clicks/elapsed_time,2)

        text = font.render("Clicks: {}".format(clicks), True, BLUE)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 50)

        time_text = font.render("Elapsed Time(s): {}".format(elapsed_time), True, BLUE)
        time_text_rect = time_text.get_rect()
        time_text_rect.center = (width / 2, 75)

        cps_text = font.render("Clicks per Second: {}".format(cps), True, BLUE)
        cps_text_rect = cps_text.get_rect()
        cps_text_rect.center = (width / 2, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for cookie in cookies:
                    if cookie.handle_click(x,y,cookies):
                        clicks += 1

        cookies.update()
        screen.fill(WHITE)
        screen.blit(text,text_rect)
        screen.blit(cps_text, cps_text_rect)
        screen.blit(time_text, time_text_rect)

        cookies.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
