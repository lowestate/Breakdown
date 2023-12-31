import pygame
import time
from consts import *

class Enemy:
    def __init__(self, game):
        self.game = game

        self.is_shooting = False

        self.angle = PLAYER_ANGLE

        self.start = time.time()

    def move(self):
        keys = pygame.key.get_pressed()

        if self.game.map.curr_map[int(self.y / 32)][int(self.x / 32)] == -1:
            if keys[pygame.K_a]:
                self.prev_x = self.x
                self.x -= PLAYER_SPEED
            if keys[pygame.K_w]:
                self.prev_y = self.y
                self.y -= PLAYER_SPEED
            if keys[pygame.K_d]:
                self.prev_x = self.x
                self.x += PLAYER_SPEED
            if keys[pygame.K_s]:
                self.prev_y = self.y
                self.y += PLAYER_SPEED
        else:
            self.x = self.prev_x
            self.y = self.prev_y

        if pygame.mouse.get_pressed()[0]:
            self.is_shooting = True
        else:
            self.is_shooting = False

    def borders_check(self):
        # borders check:
        if self.y < 0:
            self.y = 1070
            self.is_bottom = False
            self.game.map.get_map()
            self.game.bullets = []

        if self.y > 1070:
            self.y = 0
            self.is_bottom = True
            self.game.map.get_map()
            self.game.bullets = []

        if self.x > 1910:
            self.x = 0
            self.is_left = False
            self.game.map.get_map()
            self.game.bullets = []

        if self.x < 0:
            self.x = 1910
            self.is_left = True
            self.game.map.get_map()
            self.game.bullets = []

    def shoot(self):
        if time.time() - self.start > BULLET_CD:
            bullet = Bullet(self.game, self.x, self.y, self.angle)
            self.game.bullets.append(bullet)
            self.start = time.time()

    def draw(self):

        pygame.draw.circle(self.game.screen, 'green', (self.x, self.y), 15)

    def update(self):
        self.borders_check()
        self.move()

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_x = mouse_x - self.x
            delta_y = mouse_y - self.y
            self.angle = math.atan2(delta_y, delta_x)
            self.angle %= math.tau
            self.shoot()
