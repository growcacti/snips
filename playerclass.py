import pygame as pg
import random
import sys
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2




class Player:
    def __init__(
        self, image, x, y):
        self.orig_image = pg.image.load("ship8.png").convert_alpha()
        self.image = pg.image.load("ship8.png").convert_alpha()
     
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = 0.0
        self.length = 4
        self.max_acceleration = 5.0
        self.max_rotation = 10
        self.max_velocity = 220
        self.thrust = 150
        self.sim_inertia = 10  # iner

        self.acceleration = 0.0
        self.rotation = 0.0
        self.camera = Vector2(0, 0)  # Assigned the camera as an attribute.
        self.direction = Vector2(0, 0)
    def controls(self):
        pressed = pg.key.get_pressed()

        if pressed[pg.K_UP]:
            if self.velocity.x < 0:
                self.acceleration = self.thrust
            else:
                self.acceleration += 890 * dt
        elif pressed[pg.K_DOWN]:
            if self.velocity.x > 0:
                self.acceleration = -self.thrust
            else:
                self.acceleration -= 1 * dt

        
           
        elif pressed[pg.K_h]:
            if abs(self.velocity.x) > dt * self.thrust:
                self.acceleration = -copysign(
                    self.thrust, self.velocity.x
                )
            else:
                self.acceleration = -self.velocity.x / dt
        else:
            if abs(self.velocity.x) > dt * self.sim_inertia:
                self.acceleration = -copysign(
                    self.sim_inertia, self.velocity.x
                )
            else:
                if dt != 0:
                    self.acceleration = -self.velocity.x / dt
        self.acceleration = max(
            -self.max_acceleration,
            min(self.acceleration, self.max_acceleration),
        )

        if pressed[pg.K_RIGHT]:
            self.rotation -= 20 * dt
            
        elif pressed[pg.K_LEFT]:
            self.rotation += 20 * dt
           
        else:
            self.rotation = 0
        self.rotation = max(
            -self.max_rotation,
            min(self.rotation, self.max_rotation),
        )

        
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(
            -self.max_velocity, min(self.velocity.x, self.max_velocity)
        )

        if self.rotation:
            turning_radius = self.length / tan(radians(self.rotation))
            angular_velocity = self.velocity.x / turning_radius / 2
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
        self.camera += vel  # Update the camera position as well.
        # If you use the rect as the blit position, you should update it, too.
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt
       
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        #self.direction = self.angle
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)
        pg.display.set_caption(str(self.rect.center))
        origin = (600, 400)
        destination = self.rect.center
        get_info.info(origin, destination)
