# ... (Previous code initializing pygame and loading images)


# Define the enemy class
class Enemy:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.alive = True


# Define a basic bullet class
class Bullet:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.alive = True


# Create enemy and bullet instances
enemy_image = pg.image.load("enemy.png").convert_alpha()
bullet_image = pg.image.load("bullet.png").convert_alpha()

enemies = [Enemy((400, 300), enemy_image)]
bullets = [Bullet((350, 300), bullet_image)]

# ... (Game loop code)

# Inside your game loop, you would check for collisions like this:
for bullet in bullets:
    for enemy in enemies:
        if bullet.rect.colliderect(enemy.rect):
            print("Enemy took a hit!")
            enemy.alive = False
            bullet.alive = False
            explosions.append(Explosion(enemy.position, explosion_images))

# Remove dead enemies and bullets
enemies = [enemy for enemy in enemies if enemy.alive]
bullets = [bullet for bullet in bullets if bullet.alive]

# ... (Rest of game loop)
