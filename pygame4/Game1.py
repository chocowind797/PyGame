import sys
import time
import pygame
import threading
from pygame.locals import *

spaces = []
isDown = True
size = [0, 550, 50, 50]
finish = None


def checkDown():
    global isDown

    while rect[1] < 500 + size[3]:
        canMove = True

        time.sleep(0.5)

        pygame.draw.rect(win, (255, 255, 255), rect)
        drawLines()
        pygame.display.update()

        if rect[1] < 500 + size[3]:
            for space in spaces:
                if rect[1] + 50 == space.top and rect[0] == space.left:
                    canMove = False
            if canMove:
                rect.move_ip(0, 50)
        pygame.draw.rect(win, (100, 100, 100), rect)

        drawLines()
        pygame.display.update()
        isDown = True
        time.sleep(0.75)


def drawFinish(a, b):
    global finish
    finish = pygame.Rect(a, b, 50, 50)
    pygame.draw.rect(win, (0, 0, 255), finish)


def space():
    rows = open('space.txt').read().split('\n')
    i = 0
    for row in rows:
        if row.__contains__('='):
            pass
        if row.__contains__('finish:'):
            row = row.split(":")[1].split(",")
            drawFinish(int(row[0]), int(row[1]))
            break
        row = row.split(",")
        if len(row) == 1:
            continue
        rect_local = pygame.Rect(int(row[0]), int(row[1]), 50, 50)
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
        canMove = True
        if event.key == K_RIGHT:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[0] < 700 + size[2]:
                for space in spaces:
                    if rect[0] + 50 == space.left and rect[1] == space.top:
                        canMove = False
                        break
                if canMove:
                    rect.move_ip(50, 0)
        elif event.key == K_LEFT:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[0] > 0:
                for space in spaces:
                    if rect[0] - 50 == space.left and rect[1] == space.top:
                        canMove = False
                        break
                if canMove:
                    rect.move_ip(-50, 0)
        elif event.key == K_UP and isDown:
            pygame.draw.rect(win, (255, 255, 255), rect)
            if rect[1] > 0:
                for space in spaces:
                    if rect[1] - 50 == space.top and rect[0] == space.left:
                        canMove = False
                        break
                if canMove:
                    rect.move_ip(0, -50)
        pygame.draw.rect(win, (100, 100, 100), rect)
        drawLines()
        pygame.display.update()

        # print(rect[1] + 50, spaces[0].top)
        # print('--------------')
        # print(rect[0], spaces[0].left)
        # print("==============")
        if rect[1] < 500 + size[3]:
            threading.Thread(target=checkDown).start()
            isDown = False

        if rect[0] == finish.left and rect[1] == finish.top:
            finish_raw_pic = pygame.image.load('./遊戲結束.jpg').convert()
            finish_pic = pygame.transform.scale(finish_raw_pic, win.get_size())
            win.blit(finish_pic, win.get_rect())
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    elif event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    pygame.init()

    win = pygame.display.set_mode((800, 600))

    win.fill((255, 255, 255))

    space()
    drawLines()

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
