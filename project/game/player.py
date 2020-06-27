import pygame
from .config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        # self.rect.x = 100
        # self.rect.y = 100

        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

        self.can_jump = False

    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)

    def validate_platform(self, platform):
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True

            #self.image = self.images[0]

    def jump(self):
        if self.can_jump:
            self.vel_y = -23
            self.can_jump = False

            #self.image = self.images[1]

    def update_pos(self):
        self.vel_y += PLAYER_GRAV
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV

    def update(self):
        self.update_pos()

        self.rect.bottom = self.pos_y
