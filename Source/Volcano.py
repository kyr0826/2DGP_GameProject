from pico2d import Image, load_image, draw_rectangle
import game_framework
from Source import GameConstants


class Volcano:
    volcano = None
    def __init__(self):
        self.width = 800
        self.height = 0
        self.isLavaRising = False
        self.RISING_SPEED = 5.0

        self.flow_speed = 60.0
        self.scroll = 0.0

        if self.volcano is None:
            Volcano.volcano = load_image("alpha_volcano.png")

        self.tex_w = Volcano.volcano.w
        self.tex_h = Volcano.volcano.h


    def update(self):

        if not GameConstants.isGameEnd and self.isLavaRising:
            self.height += self.RISING_SPEED * game_framework.frame_time
            if self.height > self.tex_h:
                self.height = self.tex_h

        self.scroll = (self.scroll + self.flow_speed * game_framework.frame_time) % self.tex_h

    def get_bb(self):
        return 0, 0, self.width, self.height

    def draw(self):
        if self.height <= 0: return
        draw_rectangle(*self.get_bb(),255,0,255,255)
        src_h = int(self.height)
        offset = int(self.scroll) % self.tex_h

        cx = self.width / 2
        cy = self.height / 2
        if offset + src_h <= self.tex_h:
            Volcano.volcano.clip_composite_draw(
                0, offset,  self.tex_w  , src_h,
                0, '',
                cx, cy, self.width, self.height)
        else:
            h1 = self.tex_h - offset
            dest_h1 = self.height * (h1/src_h)

            Volcano.volcano.clip_composite_draw(
                0, offset, self.tex_w, h1,
                0, '',
                cx, dest_h1/2, self.width, dest_h1)

            h2 = src_h - h1
            dest_h2 = self.height - dest_h1

            Volcano.volcano.clip_composite_draw(
                0, 0, self.tex_w, h2,
                0, '',
                cx, dest_h1 + (dest_h2/2), self.width, dest_h2)
