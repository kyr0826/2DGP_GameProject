from pico2d import *
import game_framework

def init(): pass

def finish(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            pass

        if event.type == SDL_MOUSEBUTTONDOWN:
            pass


def draw():
    clear_canvas()
    draw_rectangle(0, 0, 800, 750, 0, 0, 0, 255, True)
    update_canvas()

def update(): pass

def pause(): pass

def resume(): pass