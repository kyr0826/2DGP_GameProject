from pico2d import Image
from StateMachine import *
from pico2d import *

class Animation:
    def __init__(self, owner, frames : Image, frame_count, fps, loop=True):
        self.owner = owner
        self.frames = frames
        self.frame_count = frame_count
        self.fps = fps
        self.loop = loop
        self.time = 0
        self.index = 0
        self.isEnd = False

    def update(self, delta_time):
        if not self.loop and self.isEnd:
            return

        self.time += delta_time
        frame_duration = 1.0 / self.fps
        if self.time > frame_duration:
            self.time -= frame_duration
            if self.loop:
                self.index = (self.index+1) % self.frame_count
            else:
                if self.index < self.frame_count-1:
                    self.index += 1
                else:
                    self.index = self.frame_count-1
                    self.isEnd = True
    # 128 * 128
    def draw_frame(self, isVisible):
        left = 0 + 128 * self.index
        fliped = '' if self.owner.last_dir > 0 else 'h'
        x, y = self.owner.pos_x, self.owner.pos_y
        if self.owner.state_machine.current == States.RUN and self.owner.name != 'Fighter' and self.owner.x_speed != 0:
            x += self.owner.last_dir * 16

        if isVisible:
            self.frames.clip_composite_draw(left, 0, 128, 128, 0, fliped,x, y,128,128)


class Animator:
    def __init__(self,owner):
        self.owner = owner
        self.animations = {}
        self.current = None

        self.isBlinking = False
        self.isVisible = True
        self.BLINK_INTERVAL = 0.05
        self.blinking_timer = 0.0

    def add(self, state, animation):
        self.animations[state] = animation

    def play(self, state):
        if state in self.animations:
            self.current = self.animations[state]
            self.current.index = 0
            self.current.time = 0
            self.current.isEnd = False

    def update(self, delta_time):
        if self.current:
            self.current.update(delta_time)

        if self.isBlinking:
            self.blinking_timer += delta_time
            if self.blinking_timer >= self.BLINK_INTERVAL:
                self.blinking_timer = 0.0
                self.isVisible = not self.isVisible

    def draw_current_frame(self):
        self.current.draw_frame(self.isVisible)