import random
import sys
import pygame
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
IMAGEWIDTH = 300
IMAGEHEIGHT = 200
FPS = 200


def random_pos(win_width, win_height, image_width, image_height):
    r_x = random.randint(0, (win_width - image_width))
    r_y = random.randint(0, (win_height - image_height))

    return r_x, r_y


class Mos(pygame.sprite.Sprite):
    def __init__(self, width, height, r_x, r_y, win_width, win_height):
        super().__init__()
        # 載入圖片
        self.raw_image = pygame.image.load('./蚊子.png').convert_alpha()
        # 縮放圖片
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        # 回傳位置
        self.rect = self.image.get_rect()
        # 定位
        self.rect.topleft = (r_x, r_y)
        self.width = width
        self.height = height
        self.win_width = win_width
        self.win_height = win_height


def main():
    pygame.init()

    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    global IMAGEWIDTH
    global IMAGEHEIGHT
    global WHITE
    global FPS

    # 載入介面
    win_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    r_x, r_y = random_pos(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
    mos = Mos(IMAGEWIDTH, IMAGEHEIGHT, r_x, r_y, WINDOW_WIDTH, WINDOW_HEIGHT)
    reload_mos_event = USEREVENT + 1
    pygame.time.set_timer(reload_mos_event, 300)
    scores = 0
    font = pygame.font.SysFont(None, 30)
    hit_font = pygame.font.SysFont(None, 40)
    hit_text_surface = None
    main_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == reload_mos_event:
                mos.kill()
                r_x, r_y = random_pos(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                mos = Mos(IMAGEWIDTH, IMAGEHEIGHT, r_x, r_y, WINDOW_WIDTH, WINDOW_HEIGHT)
            elif event.type == MOUSEBUTTONDOWN:
                if r_x < pygame.mouse.get_pos()[0] < r_x + IMAGEWIDTH and \
                        r_y < pygame.mouse.get_pos()[1] < r_y + IMAGEHEIGHT:
                    mos.kill()
                    r_x, r_y = random_pos(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                    mos = Mos(IMAGEWIDTH, IMAGEHEIGHT, r_x, r_y, WINDOW_WIDTH, WINDOW_HEIGHT)
                    scores += 5

        # 清除畫面
        win_surface.fill(WHITE)

        text_surface = font.render('Scores: {}'.format(scores), True, (0, 0, 0))

        # 渲染物件
        win_surface.blit(mos.image, mos.rect)
        win_surface.blit(text_surface, (10, 0))

        if hit_text_surface:
            win_surface.blit(hit_text_surface, (10, 10))
            hit_text_surface = None

        pygame.display.update()
        main_clock.tick(FPS)


if __name__ == '__main__':
    main()
