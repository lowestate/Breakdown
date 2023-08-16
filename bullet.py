import pygame
import math
from consts import *

class Bullet:
    def __init__(self, game, x, y, angle):
        self.game = game
        self.x = x
        self.y = y

        self.angle = angle
        self.speed = BULLET_SPEED
        self.cd = BULLET_CD

    def update(self):
        dx = self.speed * math.cos(self.angle) * self.game.delta_time
        dy = self.speed * math.sin(self.angle) * self.game.delta_time
        self.x += dx
        self.y += dy

        if self.check_collision():
            self.game.bullets.remove(self)

    def check_collision(self):
        map_x, map_y = int(self.x / 32), int(self.y / 32)
        #print(map_x, map_y)
        if self.game.map.curr_map[map_y][map_x] != '-1':
            return True
        return False

    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', (int(self.x), int(self.y)), 4)
