import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    alien_settings = Settings()
    screen = pygame.display.set_mode((alien_settings.screen_height, alien_settings.screen_width))
    pygame.display.set_caption("David se la come")
    ship1 = Ship(alien_settings, screen)

    while True:
        gf.check_event(ship1)
        ship1.update()
        gf.update_screen(alien_settings, screen, ship1)


run_game()
