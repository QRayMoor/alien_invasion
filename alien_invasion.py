import sys

import pygame
from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    '''初始化游戏、设置和屏幕对象'''

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        gf.check_events(ship)
        # 每次循环时都重绘屏幕 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship)


run_game()
