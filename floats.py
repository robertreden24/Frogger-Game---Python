import pygame
from settings import Settings

game_settings = Settings()

#class for floats sprite
class Floats(pygame.sprite.Sprite):

    def __init__(self, image, position, number):
        pygame.sprite.Sprite.__init__(self)

        #load sprite image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        #initalize sprite speed, position, and number
        self.speed = game_settings.float_speed
        self.pos = position
        self.number = number

        #decide from which side the sprite is loaded to the screen according to its number(lane)
        if self.number % 2 == 0:
            self.rect = self.rect.move(700, self.pos)
        else:
            self.rect = self.rect.move(-60, self.pos)

    def update(self):

        #decide the direction the sprite moves according to its number(lane)
        if self.number % 2 == 0:
            self.rect = self.rect.move(-1 * self.speed, 0)
            if self.rect.right < 0:
                self.rect.left = 640
        else:
            self.rect = self.rect.move(self.speed, 0)
            if self.rect.left > 640:
                self.rect.right = 0