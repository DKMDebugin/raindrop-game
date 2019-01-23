import sys
import pygame


from raindrop import Raindrop

def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the quit event is triggered
            sys.exit() # exit game

def update_screen(ai_settings, screen, raindrops):
    """Update images on the screen and flip to the new screen."""

    screen.fill(ai_settings.bg_color) #Redraw the screen during each pass through the loop.

    raindrops.draw(screen) #Redraw each Raindrop in the group to the screen
    pygame.display.flip() # Make the most recently drawn screen visible.

def get_number_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row """
    available_space_x = ai_settings.screen_width - 2 * raindrop_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def create_raindrop(ai_settings, screen, raindrops, raindrop_number):
    """Create a raindrop and place it in the row"""
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrops.add(raindrop)

def create_fleet(ai_settings, screen, raindrops):
    """Create a full fleet of Raindrops."""
    # Create an Raindrop and find the number of Raindrops in a row.
    # Spacing between each Raindrop is equal to one Raindrop width.
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)

    # Create the first row of Raindrops.
    for raindrop_number in range(number_raindrops_x):
        # Create an Raindrop and place it in the row.
        create_raindrop(ai_settings, screen, raindrops, raindrop_number)

def check_fleet_bottom(ai_settings, screen, raindrops):
    """Respond appropriately if any raindrops have reached the bottom."""
    for raindrop in raindrops.sprites():
        if raindrop.check_bottom(ai_settings):
            raindrop.del_raindrop(raindrops)
            create_fleet(ai_settings, screen, raindrops)
            break

def update_raindrops(ai_settings, screen, raindrops):
    """
    Check if the fleet is at an edge,
    and then update the postions of all raindrops in the fleet.
    """
    check_fleet_bottom(ai_settings, screen, raindrops)
    raindrops.update()
