from pico2d import load_image, get_time, clear_canvas, update_canvas, resize_canvas, draw_rectangle
import game_framework
import Lobby_scene

splash_duration = 1.0


def init():
    global image, splash_start_time

    image = load_image('tuk_credit.png')
    splash_start_time = get_time()

def finish():
    global image
    del image

def handle_events(): pass

def draw():
    clear_canvas()
    draw_rectangle(0,0,800,750,0,0,0,255,True)
    image.draw(400, 375)
    update_canvas()

def update():
    global splash_start_time
    if get_time() - splash_start_time >= splash_duration:
        splash_start_time = get_time()
        game_framework.change_mode(Lobby_scene)

def pause(): pass

def resume(): pass