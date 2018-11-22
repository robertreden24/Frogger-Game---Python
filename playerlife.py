import pygame

#class for player life sprite
class Life(pygame.sprite.Sprite):

    def __init__(self, number):
        pygame.sprite.Sprite.__init__(self)

        #load sprite image
        self.image = pygame.image.load("images/life.png")
        self.rect = self.image.get_rect()

        #load the sprite at this position
        self.rect.center = (number, 620)