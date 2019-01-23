import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    """A class to represent a single Raindrop in the fleet."""
    def __init__(self, ai_settings, screen):
       """Initialize the raindrop and set its starting position."""
       super().__init__()
       self.screen = screen
       self.ai_settings = ai_settings
       # Load the raindrop image and set its rect attribute.
       self.image = pygame.image.load('images/raindrop.bmp')
       self.rect = self.image.get_rect()
       # Start each new raindrop near the top left of the screen.
       self.rect.x = self.rect.width
       self.rect.y = self.rect.height
       # Store the Raindrop's exact position.
       self.y = float(self.rect.y)

    def blitme(self):
       """Draw the raindrop at its current location."""
       self.screen.blit(self.image, self.rect)

    def check_bottom(self, ai_settings):
        """Return True if raindrop is at edge of screen."""
        if self.rect.top >= ai_settings.screen_height:
            return True

    def update(self):
        """Move the raindrop down."""
        self.y += randint(1,self.ai_settings.raindrop_speed_factor)
        self.rect.y = self.y

    def del_raindrop(self, raindrops):
        """Delete raindrop"""
        for raindrop in raindrops.copy():
            raindrops.remove(raindrop)
