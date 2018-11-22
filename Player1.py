import pygame
from settings import Settings

game_settings = Settings()

#class for player1 sprite
class Player1(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #load sprite image
        self.image = pygame.image.load("images/bunnystill.png")
        self.rect = self.image.get_rect()

        #load the sprite at this position
        self.rect.center = (380, 620)

        #sprite movement dictionaries
        self.image_up = {1: "images/bunnystill.png", -1: "images/bunnyjump.png"}
        self.image_down = {1: "images/bunnystillback.png", -1: "images/bunnyjumpback.png"}
        self.image_right = {1: "images/bunnyright.png", -1: "images/bunnyjumpright.png"}
        self.image_left = {1: "images/bunnyleft.png", -1: "images/bunnyjumpleft.png"}

        #sprite movement counts
        self.up_count = 1
        self.down_count = 1
        self.right_count = 1
        self.left_count = 1

        #timer for sprite movement counts
        self.timer = 0

        # player lives
        self.lives = 3

    def update(self):
        #initialize speed of sprite movements
        self.speedx = 0
        self.speedy = 0

        #move the sprite according to keys pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -2
            self.image = pygame.image.load(self.image_left[self.left_count])
            if self.timer % 3 == 0:
                self.left_count = self.left_count * -1
        if keystate[pygame.K_RIGHT]:
            self.speedx = 2
            self.image = pygame.image.load(self.image_right[self.right_count])
            if self.timer % 3 == 0:
                self.right_count = self.right_count * -1
        if keystate[pygame.K_UP]:
            self.speedy = -2
            self.image = pygame.image.load(self.image_up[self.up_count])
            if self.timer % 2 == 0:
                self.up_count = self.up_count * -1
        if keystate[pygame.K_DOWN]:
            self.speedy = 2
            self.image = pygame.image.load(self.image_down[self.down_count])
            if self.timer % 3 == 0:
                self.down_count = self.down_count * -1

        #move the sprite according to its speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # so the sprite will not be able to pass through the edge of the screen
        if self.rect.right > game_settings.screen_width:
            self.rect.right = game_settings.screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.centery > game_settings.screen_height - 10:
            self.rect.centery = game_settings.screen_height - 10

        #increment timer
        self.timer = self.timer + 1