import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_IMAGE_SIZE = 100  # The background image is 100x100 pixels

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background image
bg_image = pygame.image.load("b.png")
bg_image = pygame.transform.scale(bg_image, (BG_IMAGE_SIZE, BG_IMAGE_SIZE))

# Initialize variables
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
scroll_offset = [0, 0]
player_speed = 5

# Main loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        scroll_offset[0] += player_speed
    if keys[pygame.K_RIGHT]:
        scroll_offset[0] -= player_speed
    if keys[pygame.K_UP]:
        scroll_offset[1] += player_speed
    if keys[pygame.K_DOWN]:
        scroll_offset[1] -= player_speed

    # Draw background
    for x in range(-scroll_offset[0] % BG_IMAGE_SIZE, SCREEN_WIDTH, BG_IMAGE_SIZE):
        for y in range(-scroll_offset[1] % BG_IMAGE_SIZE, SCREEN_HEIGHT, BG_IMAGE_SIZE):
            screen.blit(bg_image, (x, y))

    # Draw player (as a red rectangle for demonstration)
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], 20, 20))

    # Update the screen
    pygame.display.update()
    clock.tick(60)
