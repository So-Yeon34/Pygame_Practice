import sys
import pygame
from pygame.locals import QUIT

pygame.init() # Initalize pygame
SURFACE = pygame.display.set_mode((400,300)) # Create a window (width = 400, height = 300)
pygame.display.set_caption("Game Window") # Display title "Game Window"

def main():
    """main routine"""
    while True: # Execute main() function until "QUIT" event triggered
        SURFACE.fill((255,255,255)) # Fill window with white

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update() # Update window display - changes appear

if __name__ == '__main__': # The main() function will be called only when this code is executed directly.
    main()


