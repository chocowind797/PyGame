import pygame
import sys
from pygame.locals import *

pygame.init()

# 給定視窗大小
win = pygame.display.set_mode((800, 600))

# 更新視窗
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
