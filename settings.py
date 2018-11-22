import pygame

#class for game settings
class Settings():

    def __init__(self):

        #initialize screen settings(width, height, background image, and fps)
        self.screen_width = 640
        self.screen_height = 640
        self.bg_image = pygame.image.load("images/background.png")
        self.bg_image_rect = self.bg_image.get_rect()
        self.fps = 30

        #initialize speed of floats sprite
        self.float_speed = 3

        #initialize background music volume
        self.bg_music_vol = 0.5