import pygame
import time
from consts import *
from bullet import *

class Player:
    def __init__(self, game):
        self.game = game

        self.x = PLAYER_X
        self.y = PLAYER_Y

        self.player_sprite = pygame.image.load('graphics/player/player_gray_150x90.png')
        self.player_sprite_copy = self.player_sprite.copy()
        self.player_hitbox = self.player_sprite.get_rect(topleft=(self.x, self.y))

        self.prev_x = self.x
        self.prev_y = self.y

        self.is_bottom = True
        self.is_left = True
        self.is_shooting = False

        self.angle = PLAYER_ANGLE
        self.rot_angle = 0

        self.start = time.time()

    def move(self):
        keys = pygame.key.get_pressed()
        if not self.game.map.moving:
            self.game.map.moving = True
            self.x = self.prev_x
            self.y = self.prev_y
        else:
            self.prev_x = self.x
            self.prev_y = self.y

            if keys[pygame.K_a]:
                self.x -= PLAYER_SPEED
            if keys[pygame.K_w]:
                self.y -= PLAYER_SPEED
            if keys[pygame.K_d]:
                self.x += PLAYER_SPEED
            if keys[pygame.K_s]:
                self.y += PLAYER_SPEED

        if pygame.mouse.get_pressed()[0]:
            self.is_shooting = True
        else:
            self.is_shooting = False

    def borders_check(self):
        # borders check:
        if self.y < 0:
            self.y = 1000
            self.player_hitbox.y = 1000
            self.is_bottom = False
            self.game.map.get_map()
            self.game.bullets = []

        if self.y > 1000:
            self.y = 0
            self.player_hitbox.y = 0
            self.is_bottom = True
            self.game.map.get_map()
            self.game.bullets = []

        if self.x > 1900:
            self.x = 0
            self.player_hitbox.x = 0
            self.is_left = False
            self.game.map.get_map()
            self.game.bullets = []

        if self.x < 0:
            self.x = 1900
            self.player_hitbox.x = 1900
            self.is_left = True
            self.game.map.get_map()
            self.game.bullets = []

    def shoot(self):
        if time.time() - self.start > BULLET_CD:
            bullet = Bullet(self.game, self.x + 150, self.y + 65, self.angle)
            self.game.bullets.append(bullet)
            self.start = time.time()

    def draw(self):
        #self.game.screen.blit(self.player_sprite, (self.x, self.y))
        pygame.draw.rect(self.game.screen, 'green', (self.x, self.y, 150, 90), 3)

    def update(self):
        self.borders_check()
        self.move()
        self.player_hitbox.x = self.x
        self.player_hitbox.y = self.y

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.player_hitbox.x
        dy = mouse_y - self.player_hitbox.y
        self.rot_angle = math.atan2(dy, dx)
        self.player_sprite = pygame.transform.rotate(self.player_sprite_copy, math.degrees(-self.rot_angle))
        self.player_hitbox = self.player_sprite.get_rect(center=(self.x, self.y))

        self.game.screen.blit(self.player_sprite, self.player_hitbox.topleft)

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_x = mouse_x - self.x - 150
            delta_y = mouse_y - self.y - 65
            self.angle = math.atan2(delta_y, delta_x)
            self.angle %= math.tau
            self.shoot()
