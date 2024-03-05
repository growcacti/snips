import pygame as pg
import sys

pg.init()
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Platformer Game")
import pygame as pg
import sys

pg.init()
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Platformer Game")


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = screen_width // 2, screen_height // 2
        self.vel_y = 0
        self.vel_x = 0  # Horizontal velocity

    def update(self):
        self.vel_y += 1  # Gravity
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x  # Horizontal movement
        self.rect.y = min(
            self.rect.y, screen_height - self.rect.height
        )  # Prevent falling through floor

    def jump(self):
        self.vel_y = -15  # Jump strength

    def move_left(self):
        self.vel_x = -5  # Left movement speed

    def move_right(self):
        self.vel_x = 5  # Right movement speed

    def stop_horizontal_movement(self):
        self.vel_x = 0  # Stop horizontal movement


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


player = Player()
platforms = pg.sprite.Group()
platforms.add(Platform(300, 500, 200, 10))  # Example platform
platforms.add(Platform(400, 600, 200, 10))
platforms.add(Platform(200, 100, 200, 10))
platforms.add(Platform(300, 800, 200, 10))
platforms.add(Platform(500, 800, 200, 10))
platforms.add(Platform(400, 900, 200, 10))
platforms.add(Platform(300, 750, 200, 10))
platforms.add(Platform(350, 550, 200, 10))
platforms.add(Platform(700, 600, 200, 10))
platforms.add(Platform(100, 500, 200, 10))


def camera_translate(camera, target_rect):
    l, t, _, _ = target_rect  # local left, top
    _, _, w, h = camera  # camera width, height
    return pg.Rect(-l + w // 2, -t + h // 2, w, h)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
            elif event.key == pg.K_LEFT:
                player.move_left()
            elif event.key == pg.K_RIGHT:
                player.move_right()
        elif event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_RIGHT):
                player.stop_horizontal_movement()

    player.update()

    camera_rect = camera_translate(
        pg.Rect(0, 0, screen_width, screen_height), player.rect
    )

    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if player.vel_y > 0:  # Colliding from above
                player.rect.y = platform.rect.y - player.rect.height
                player.vel_y = 0
            elif player.vel_y < 0:  # Colliding from below
                player.rect.y = platform.rect.y + platform.rect.height
                player.vel_y = 0
            elif player.vel_x > 0:  # Colliding from the left
                player.rect.x = platform.rect.x - player.rect.width
            elif player.vel_x < 0:  # Colliding from the right
                player.rect.x = platform.rect.x + platform.rect.width

    screen.fill((0, 0, 0))
    for platform in platforms:
        screen.blit(
            platform.image, camera_rect.topleft + pg.Vector2(platform.rect.topleft)
        )

    screen.blit(player.image, camera_rect.topleft + pg.Vector2(player.rect.topleft))
    pg.display.flip()
    pg.time.Clock().tick(60)

pg.quit()
sys.exit()
