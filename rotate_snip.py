import pygame
from pygame.math import Vector2

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotate Ship")

# Load the ship image
orig_ship_image = pygame.image.load("path_to_ship_image.png").convert_alpha()
ship_rect = orig_ship_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

angle = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate the ship (You can change how you modify the angle)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += 1  # Rotate counter-clockwise
    if keys[pygame.K_RIGHT]:
        angle -= 1  # Rotate clockwise

    # Use the rotozoom function to rotate and scale (1 for original size here)
    rotated_ship = pygame.transform.rotozoom(orig_ship_image, angle, 1)
    new_rect = rotated_ship.get_rect(center=ship_rect.center)

    screen.blit(rotated_ship, new_rect.topleft)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
