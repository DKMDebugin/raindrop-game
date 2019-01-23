import pygame
from pygame.sprite import Group

from settings import Settings
import game_function as gf
from raindrop import Raindrop

def run_game():
    '''
    Initialize pygame ,
    create a screen object
    (window screen size & window caption) & settings
    '''
    pygame.init()
    ai_settings = Settings() #Object of Settings() class
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height)) #set screen size by passing in Settings width & height attributes
    pygame.display.set_caption("Raindrop")

    #Make  a group of Raindrops
    raindrops = Group()
    # Create the fleet of Raindrops.
    gf.create_fleet(ai_settings, screen, raindrops)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen)
        gf.update_raindrops(ai_settings, screen, raindrops)
        gf.update_screen(ai_settings, screen, raindrops)

run_game()
