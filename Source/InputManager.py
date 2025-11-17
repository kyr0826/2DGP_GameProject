from pico2d import *

class InputManager:
    def __init__(self):
        self.key_state = {}
        self.key_up = {}
        self.key_down_events = {}

    def update(self, events):
        self.key_up.clear()
        self.key_down_events.clear()

        for e in events:
            if e.type == SDL_KEYDOWN:
                if not self.key_state.get(e.key,False):
                    self.key_down_events[e.key] = True
                self.key_state[e.key] = True
            elif e.type == SDL_KEYUP:
                self.key_state[e.key] = False
                self.key_up[e.key] = True

    def get_axis(self, left, right):
        left = -1 if self.key_state.get(left, False) else 0
        right = 1 if self.key_state.get(right, False) else 0

        return left + right

    def get_key_down(self, key):
        return self.key_state.get(key, False)

    def get_key_up(self, key):
        return self.key_up.get(key, False)

    def get_key_press(self, key):
        return self.key_down_events.get(key, False)