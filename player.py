import pygame
from consts import *

class Player:
    def __init__(self, game):
        self.game = game

        self.x = PLAYER_X
        self.y = PLAYER_Y
        self.prev_x = self.x
        self.prev_y = self.y

        self.is_bottom = True
        self.is_left = True

    def move(self):
        keys = pygame.key.get_pressed()

        #self.prev_x = self.x
        #self.prev_y = self.y

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
        
        '''
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED
        '''
    def borders_check(self):
        # borders check:
        if self.y < 0:
            self.y = 1080
            self.is_bottom = False

        if self.y > 1080:
            self.y = 0
            self.is_bottom = True

        if self.x > 1920:
            self.x = 0
            self.is_left = False

        if self.x < 0:
            self.x = 1920
            self.is_left = True

    def draw(self):
        pygame.draw.circle(self.game.screen, 'green', (self.x, self.y), 15)

    def update(self):
        self.move()
        self.borders_check()
