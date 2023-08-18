import pygame
import pytmx
import sys

from bullet import *
from player import *
from map import *
from enemy import *
from consts import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        self.clock = pygame.time.Clock()
        self.delta_time = 1

        self.bullets = []
        self.start = 0
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.map = Map(self, self.player)
        self.enemy = Enemy(self)

    def draw(self):

        self.player.draw()

        for bullet in self.bullets:
            bullet.draw()

        self.screen.blit(self.debug(), (20, 1000))

    def update(self):

        self.player.update()

        pygame.display.flip()
        self.map.get_map()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.player.update()
            for bullet in self.bullets:
                bullet.update()
    def debug(self):
        font = pygame.font.SysFont(None, 24)
        text = (
                'P_X: ', self.player.x,
                'P_Y: ', self.player.y,
                #self.map.curr_map[int(self.player.y / 32)][int(abs(self.player.x) / 32)],
                #'T_X: ', round(self.player.x / 32),
                #'T_Y: ', round(self.player.y / 32),s
                )

        img = font.render(str(text), True, 'white')
        return img

if __name__ == '__main__':
    game = Game()
    game.run()
