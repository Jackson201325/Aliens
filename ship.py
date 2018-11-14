from setting import Settings

import pygame


class Ship():
    def __init__(self, alien_settings, screen):
        self.screen = screen
        self.alien_settings = alien_settings

        # Get rectangle of image and screen
        self.image = pygame.image.load('n/ship.bmp')
        self.ship_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the left center of the screen
        self.ship_rect.centery = self.screen_rect.centery
        self.ship_rect.left = self.screen_rect.left

        # Movement flag
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        # Store a decimal value in ship's centery
        self.center1 = float(self.ship_rect.centery)
        self.center2 = float(self.ship_rect.centerx)

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.ship_rect)

    def update(self):
        # Update ship's position bsd on the movente flag
        if self.move_up and self.ship_rect.top > 0:
            self.center1 -= self.alien_settings.move_speed
        if self.move_down and self.ship_rect.bottom < self.alien_settings.screen_width:
            self.center1 += self.alien_settings.move_speed
        if self.move_right and self.ship_rect.right < self.alien_settings.screen_height:
            self.center2 += self.alien_settings.move_speed
        if self.move_left and self.ship_rect.left > 0:
            self.center2 -= self.alien_settings.move_speed

        self.ship_rect.centery = self.center1
        self.ship_rect.centerx = self.center2
