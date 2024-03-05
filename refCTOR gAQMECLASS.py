import pygame as pg
import sys
from pygame.math import Vector2
from galaxy import Galaxy
from get_info import get_font
from player import Player
from nme import Nme
from bullets import Bullet
from probe import Probe
from constants import Constants
from controls import Controls

pg.init()

class Game:
    def __init__(self):
        self.con = Constants()
        self.screen = self.con.screen
        self.clock = self.con.clock
        self.dt = self.con.dt
        self.all_sprites = pg.sprite.Group()
        self.player = Player()

        self.font = get_font(None, 18)
        self.textsurface = self.font.render('Screen Grid Options                          greybutton                     off                   green grid            Button5', False, (255, 255, 255))

        self.background = Galaxy(self.player)

        self.all_sprites.add(self.background)

        self.control = Controls(self.player, self.dt)
        self.all_sprites.add(self.control)

        self.nme = Nme(70000, 50000)
        self.nme2 = Nme(35000, 32000)

        self.nme_group = pg.sprite.Group(self.nme)
        self.nme2_group = pg.sprite.Group(self.nme2)

        self.bullets = []
        self.probes = []

        self.hit_count = 0
        self.counter = 0
        self.time_delay = 1
        self.timer_event = pg.USEREVENT+1
        pg.time.set_timer(self.timer_event, self.time_delay)

    def run(self):
        while True:
            self.clock.tick(self.con.fps)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == self.timer_event:
                    self.counter += 1
                    self.bullets.append(Bullet(self.player.position, self.player.direction))

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        probe = Probe(self.player.position, self.player.direction, self.player)
                        self.probes.append(probe)

                elif event.type == pg.KEYUP:
                    if event.key == pg.K_p:
                        if self.probes:
                            probe = self.probes.pop()
                            self.screen.blit(probe.probe, probe.position)

            self.screen.fill((0, 0, 0))

            self.all_sprites.update(self.dt)
            self.all_sprites.draw(self.screen)

            self.screen.blit(self.textsurface, (10, 50))
            self.screen.blit(self.player.image, self.player.position)

            for bullet in self.bullets[:]:
                bullet.update()
                if not self.screen.get_rect().collidepoint(bullet.pos):
                    self.bullets.remove(bullet)
                else:
                    bullet.draw(self.screen)

            self.check_collision()
            self.update_text()

            pg.display.flip()

    def check_collision(self):
        for bullet in self.bullets:
            if bullet.rect.colliderect(self.nme.hitbox):
                print("NME took a hit!")
            if bullet.rect.colliderect(self.nme2.rect):
                print("NME2 took a hit!")

    def update_text(self):
        nme_dist = self.player.position.distance_to(self.nme.truepos)
        nme2_dist = self.player.position.distance_to(self.nme2.position)
        text8 = self.font.render("NME position: " + str(self.nme.truepos), True, self.con.WHITE)
        text9 = self.font.render("NME dist: " + str(nme_dist), True, self.con.WHITE)
.
