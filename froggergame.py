import pygame
from settings import Settings
from Player1 import Player1
from Player2 import Player2
from mobs import Mobs
from floats import Floats
from playerlife import Life

#initialize pygame and create window
pygame.init()
game_settings = Settings()
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
pygame.display.set_caption("My Game")

#initialize mixer module
pygame.mixer.init()

#create object to help track time
clock = pygame.time.Clock()

#load background music
#credits to http://opengameart.org
pygame.mixer.music.load("music/random silly chip song.ogg")
pygame.mixer.music.set_volume(game_settings.bg_music_vol)


font_name = pygame.font.match_font('arial')
# function to draw text to screen
def draw_text(surf, text, size, x, y):

    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# function to generate car mob
def generate_car():

    # mobs sprite
    car1 = Mobs("images/car1.png", 545, 2.4, 1)
    car2 = Mobs("images/car2.png", 495, 3.3, 2)
    car3 = Mobs("images/car3.png", 451, 3.6, 3)
    car4 = Mobs("images/car4.png", 403, 2.9, 4)
    car5 = Mobs("images/car5.png", 352, 3.4, 5)

    # add mob sprite to group
    all_sprites.add(car1, car2, car3, car4, car5)
    all_mobs.add(car1, car2, car3, car4, car5)


#function to show game start screen
def show_go_screen():

    #show background image as background in game start and game over screen
    screen.blit(game_settings.bg_image, game_settings.bg_image_rect)

    # render text
    draw_text(screen, "Frogger", 70, game_settings.screen_width / 2, game_settings.screen_height / 4)
    draw_text(screen, "Press space key to begin", 24, game_settings.screen_width / 2, game_settings.screen_height * 3 / 4)
    draw_text(screen, "Press escape key to exit", 24, game_settings.screen_width / 2, game_settings.screen_height * 4 / 5 )

    #flip display after drawing text to screen
    pygame.display.flip()

    #variable to initiate infinite loop
    waiting = True

    #loop to show game start or game over screen
    while waiting:

        #control speed of the loop
        clock.tick(game_settings.fps)

        #assign keys to start and exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                waiting = False
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                pygame.quit()

#set player1 and player2 score
player1_score = 0
player2_score = 0

#function  to draw score to screen
def show_score():

    draw_text(screen, "Player1: ", 20, 580, 10)
    draw_text(screen, "Player2: ", 20, 40, 10)
    draw_text(screen, str(player1_score), 20, 610, 10)
    draw_text(screen, str(player2_score), 20, 70, 10)

    #flip display after score is drawn to screen
    pygame.display.flip()


#variable to initiate game over loop
game_over = True
#variable to initiate game loop
running = True

#counter for generating mobs
counter = 0

#loop background music
pygame.mixer.music.play(loops=-1)

#game loop
while running:

    show_score()

    #game over loop
    if game_over:
        show_go_screen()
        game_over = False

        # sprite group
        all_sprites = pygame.sprite.Group()

        # mobs group
        all_mobs = pygame.sprite.Group()

        # player sprites
        bunny = Player1()
        turtle = Player2()

        # life sprites
        life_1_P1 = Life(580)
        life_2_P1 = Life(600)
        life_3_P1 = Life(620)
        life_1_P2 = Life(60)
        life_2_P2 = Life(40)
        life_3_P2 = Life(20)

        # floats sprite
        log1 = Floats("images/log.png", 250, 1)
        plank1 = Floats("images/plank.png", 200, 2)
        log2 = Floats("images/log.png", 150, 3)
        plank2 = Floats("images/plank.png", 100, 4)
        log3 = Floats("images/log.png", 50, 5)

        # add sprites to group
        all_sprites.add(log1, plank1, log2, plank2, log3)
        all_sprites.add(bunny, turtle)
        all_sprites.add(life_1_P1, life_2_P1, life_3_P1, life_1_P2, life_2_P2, life_3_P2)

        player1_score = 0
        player2_score = 0

    #keep loop running at same speed
    clock.tick(game_settings.fps)

    #generate mob periodically
    if counter % 100 == 0:
        generate_car()

    #increment counter
    counter += 1

    #process input(events)
    for event in pygame.event.get():

        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #remove life for every player1 death
    if bunny.lives == 2:
        all_sprites.remove(life_1_P1)
    elif bunny.lives == 1:
        all_sprites.remove(life_2_P1)
    elif bunny.lives == 0:
        all_sprites.remove(life_3_P1)
        all_sprites.remove(bunny)

    # remove life for every player2 death
    if turtle.lives == 2:
        all_sprites.remove(life_1_P2)
    elif turtle.lives == 1:
        all_sprites.remove(life_2_P2)
    elif turtle.lives == 0:
        all_sprites.remove(life_3_P2)
        all_sprites.remove(turtle)

    # show game over when both players run out of lives
    if bunny.lives == 0 and turtle.lives == 0:
        game_over = True

    #update the sprites
    all_sprites.update()

    #check to see if a mob hits a player1 or player1 drowns
    colPlayer1 = pygame.sprite.spritecollide(bunny, all_mobs, False)

    #check to see if player1 makes contact with floats
    player1_log1 = pygame.sprite.collide_rect(log1, bunny)
    player1_plank1 = pygame.sprite.collide_rect(plank1, bunny)
    player1_log2 = pygame.sprite.collide_rect(log2, bunny)
    player1_plank2 = pygame.sprite.collide_rect(plank2, bunny)
    player1_log3 = pygame.sprite.collide_rect(log3, bunny)

    #define danger area for player1
    danger_area_player1 = bunny.rect.top < 275 and bunny.rect.bottom > 50

    # minus 1 life of player1 if collision happens or if player1 drops into river and reset its position
    if colPlayer1 or (danger_area_player1 and not (player1_log1 or player1_plank1 or player1_log2 or player1_plank2 or player1_log3)):
        bunny.lives = bunny.lives - 1
        bunny.rect.center = (380, 620)

    #move the sprite in cohesion with float sprite when player1 sprite makes contact with float sprite
    if player1_log1 or player1_log2 or player1_log3:
            bunny.rect = bunny.rect.move(game_settings.float_speed * 1, 0)
    elif player1_plank1 or player1_plank2:
        bunny.rect = bunny.rect.move(game_settings.float_speed * -1, 0)

    #add a point when sprite reaches goal and reset position
    if bunny.rect.top < 50:
        player1_score += 1
        bunny.rect.center = (380, 620)


    #check to see if a mob hits player2 or player2 drowns
    colPlayer2 = pygame.sprite.spritecollide(turtle, all_mobs, False)

    # check to see if player2 makes contact with floats
    player2_log1 = pygame.sprite.collide_rect(log1, turtle)
    player2_plank1 = pygame.sprite.collide_rect(plank1, turtle)
    player2_log2 = pygame.sprite.collide_rect(log2, turtle)
    player2_plank2 = pygame.sprite.collide_rect(plank2, turtle)
    player2_log3 = pygame.sprite.collide_rect(log3, turtle)

    #define danger area for player2
    danger_area_player2 = turtle.rect.top < 275 and turtle.rect.bottom > 50

    # minus 1 life of player2 if collision happens or if player2 drops into river and reset its position
    if colPlayer2 or (danger_area_player2 and not (player2_log1 or player2_plank1 or player2_log2 or player2_plank2 or player2_log3)):
        turtle.lives = turtle.lives - 1
        turtle.rect.center = (260, 620)

    #move the sprite in cohesion with float sprite when player2 sprite makes contact with float sprite
    if player2_log1 or player2_log2 or player2_log3:
        turtle.rect = turtle.rect.move(game_settings.float_speed * 1, 0)
    elif player2_plank1 or player2_plank2:
        turtle.rect = turtle.rect.move(game_settings.float_speed * -1, 0)

    # add a point when sprite reaches goal and reset position
    if turtle.rect.top < 50:
        player2_score += 1
        turtle.rect.center = (260, 620)


    #fill the screen with an image as its background
    screen.blit(game_settings.bg_image, (0, 0))

    #draw the sprites to the screen
    all_sprites.draw(screen)

    #flip display after drawing everything to screen
    pygame.display.flip()

#close pygame window
pygame.quit()

#credits to ashivers
