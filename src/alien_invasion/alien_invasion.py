import sys
import pygame

def run_game():
    #初始化游戏
    pygame.init()
    screen = pygame.display.set_mode(1200,800)
    pygame.display.set_caption('Aline Invasion')

    while True:

        for event in  pygame.event.get():
            if event.type == pygame.Quit:
                sys.exit()

        pygame.display.flip()

run_game()