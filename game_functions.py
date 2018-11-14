import sys
import pygame


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            key_down(event, ship)

        elif event.type == pygame.KEYUP:
            key_up(event, ship)


def key_down(event, ship):
    if event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True


def key_up(event, ship):
    if event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(alien_settings, screen, ship):
    screen.fill(alien_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
