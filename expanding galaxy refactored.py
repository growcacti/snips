import pygame as pg
import random


class Expanding_Galaxy:
    def __init__(self, player):
        self.colorlist = [
            pg.Color(color)
            for color in [
                "white",
                "gray59",
                "turquoise1",
                "mediumspringgreen",
                "lavender",
                "cyan1",
                "cyan2",
                "aquamarine",
                "aquamarine2",
                "antiquewhite",
                "gray70",
                "gray80",
                "maroon",
                "khaki",
                "darkturquoise",
                "cornsilk",
                "azure",
                "linen",
                "aliceblue",
                "ivory1",
                "snow",
                "paleturquoise1",
            ]
        ]

        self.surfaces = [pg.Surface((6, 6)).convert_alpha() for _ in range(12)]
        self.starlist = [f"surf{i+1}" for i in range(12)]

        self.radius = 1
        self.pos = (3, 3)

        for surf in self.surfaces:
            color = random.choice(self.colorlist)
            pg.draw.circle(surf, color, self.pos, self.radius)

        self.initialize_player(player)

    def initialize_player(self, player):
        self.player = player
        self.cam = self.player.camera
        self.camx, self.camy = self.cam
        self.bgdata = []

    def coordinates(self, camx, camy, objw, objh):
        start_x = camx - W // 1
        stop_x = camx + W // 1
        start_y = camy - H // 1
        stop_y = camy + H // 1

        while True:
            rx, ry = random.randint(start_x, stop_x), random.randint(start_y, stop_y)
            obj_rect = pg.Rect(rx, ry, objw, objh)
            if not obj_rect.colliderect(pg.Rect(camx, camy, W, H)):
                return rx, ry

    def add_bg(self, camx, camy):
        bg = {"img": self.starlist, "width": 6, "height": 6, "x": 0, "y": 0}
        bg["x"], bg["y"] = self.coordinates(camx, camy, bg["width"], bg["height"])
        bg["rect"] = pg.Rect(bg["x"], bg["y"], bg["width"], bg["height"])
        return bg

    def boundaries(self, camx, camy, bg):
        bounds_rect = pg.Rect(camx - W, camy - H, 2 * W, 2 * H)
        return not bounds_rect.colliderect(
            pg.Rect(bg["x"], bg["y"], bg["width"], bg["height"])
        )

    def bgupdate(self, camx, camy):
        self.camx, self.camy = camx, camy
        if len(self.bgdata) < 3000000:
            self.bgdata.append(self.add_bg(camx, camy))

        for bg in self.bgdata:
            mrect = pg.Rect(bg["x"] - camx, bg["y"] - camy, bg["width"], bg["height"])
            for surf in self.surfaces:
                screen.blit(surf, mrect)

        self.bgdata = [bg for bg in self.bgdata if not self.boundaries(camx, camy, bg)]
