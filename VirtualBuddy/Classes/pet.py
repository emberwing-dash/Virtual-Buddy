import pygame
import ctypes
from animateSprites import SpriteSheetAnimation

# Initialize pygame
pygame.init()

# Window dimensions (adjust as needed)
screen_width = 128
screen_height = 128

# Create the Pygame screen (no border, no resize, transparent background)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.SRCALPHA)

# Set window title (not really needed, but helpful for debugging)
pygame.display.set_caption("Desktop Pet")

# Load static sprite image (kylo.png) for background
kylo_image = pygame.image.load("kylo.jpg")  # Ensure path is correct
kylo_image = pygame.transform.scale(kylo_image, (screen_width, screen_height))  # Resize to fit the screen

# MASCOT: Setup for sprite sheet animation
sprite_sheet_image = 'mascot.png'  # Your sprite sheet file
frame_width = 128  # Width of a single frame in the sprite sheet
frame_height = 128  # Height of a single frame in the sprite sheet
num_frames = 12  # Total number of frames in the sprite sheet
frame_rate = 3  # Frames per second for animation

# Create an instance of the SpriteSheetAnimation class
animation = SpriteSheetAnimation(sprite_sheet_image, frame_width, frame_height, num_frames, frame_rate)

# Set window to always be on top (Windows-only)
ctypes.windll.user32.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # If the "C" key is pressed
                running = False  # Exit the loop when 'C' is pressed
                print("C key pressed. Exiting...")

    # Fill screen with transparent background
    screen.fill((0, 0, 0, 0))  # Ensure the window is transparent

    #DRAW SPRITESS!!

    # Blit the static kylo image to the screen
    #screen.blit(kylo_image, (0, 0))

    # Draw the animated sprite on top of the kylo background
    animation.update()  # Update the animation (change frame)
    animation.draw(screen, 0, 0)

    # Update the display
    pygame.display.flip()

    # Control frame rate (adjust FPS if needed)
    clock.tick(60)

# Quit Pygame when the loop ends
pygame.quit()
