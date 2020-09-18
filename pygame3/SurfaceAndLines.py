import sys
import time
import pygame
import threading
from pygame.locals import *

spaces = []
isDown = True


def space():
    rect_local = pygame.Rect(400, 550, 50, 50)
    pygame.draw.rect(win, (255, 0, 0), rect_local)
    spaces.append(rect_local)
    pygame.display.update()


def drawLines():
    for i in range(size[2], 800, size[2]):
        pygame.draw.aaline(win, (0, 0, 0), (i, 0), (i, 600), 2)

    for i in range(size[3], 600, size[3]):
        pygame.draw.aaline(win, (0, 0, 0), (0, i), (800, i), 2)


keys = [K_RIGHT, K_LEFT, K_UP, K_DOWN]


def checkKey(event):
    if keys.__contains__(event.key):
        global isDown
        if event.key == K_RIGHT:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[0] < 700 + size[2]:
                if not (rect[0] + 50 == spaces[0].left and rect[1] == spaces[0].top):
                    rect.move_ip(50, 0)
        elif event.key == K_LEFT:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[0] > 0:
                if not (rect[0] - 50 == spaces[0].left and rect[1] == spaces[0].top):
                    rect.move_ip(-50, 0)
        elif event.key == K_UP and isDown:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[1] > 0:
                if not (rect[1] - 50 == spaces[0].top and rect[0] == spaces[0].left):
                    rect.move_ip(0, -50)
        elif event.key == K_DOWN and isDown:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[1] < 500 + size[3]:
                if not (rect[1] + 50 == spaces[0].top and rect[0] == spaces[0].left):
                    rect.move_ip(0, 50)
        pygame.draw.rect(win, (100, 100, 100), rect)
        drawLines()
        pygame.display.update()

        # print(rect[1] + 50, spaces[0].top)
        # print('--------------')
        # print(rect[0], spaces[0].left)
        # print("==============")
        if rect[1] < 500 + size[3] and (rect[1] + 50 != spaces[0].top or rect[0] != spaces[0].left):
            def wait():
                global isDown
                time.sleep(1)

                pygame.draw.rect(win, (255, 255, 255), rect)
                drawLines()
                pygame.display.update()

                if rect[1] < 550 and not (rect[1] + 50 == spaces[0].top and rect[0] == spaces[0].left):
                    rect.move_ip(0, 50)
                pygame.draw.rect(win, (100, 100, 100), rect)

                drawLines()
                pygame.display.update()
                isDown = True
            threading.Thread(target=wait).start()
            isDown = False

    elif event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()


size = [0, 550, 50, 50]

if __name__ == '__main__':
    pygame.init()

    win = pygame.display.set_mode((800, 600))

    win.fill((255, 255, 255))

    drawLines()
    space()

    rect = pygame.Rect(size[0], size[1], size[2], size[3])
    pygame.draw.rect(win, (100, 100, 100), rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                checkKey(event)
