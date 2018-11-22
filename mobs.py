import pygame
from settings import Settings

game_settings = Settings()

#class for mobs sprite
class Mobs(pygame.sprite.Sprite):

    def __init__(self, image, position, speed, number):
        pygame.sprite.Sprite.__init__(self)

        #load sprite image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        #initalize sprite speed, position, and number
        self.pos = position
        self.speed = speed
        self.number = number

        #decide from which side the sprite is loaded to the screen according to its number(lane)
        if self.number % 2 == 0:
            self.rect = self.rect.move(670, self.pos)
        else:
            self.rect = self.rect.move(-40, self.pos)

    def update(self):

        #decide the direction the sprite moves according to its number(lane)
        if self.number % 2 == 0:
            self.rect = self.rect.move(-1 * self.speed, 0)

        else:
            self.rect = self.rect.move(self.speed, 0)