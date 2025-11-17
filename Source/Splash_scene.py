from pico2d import *
import game_framework
import Lobby_scene

logo_duration = 1.0


def init():
    global image, logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global logo_start_time
    if get_time() - logo_start_time >= logo_duration:
        logo_start_time = get_time()
        game_framework.change_mode(Lobby_scene)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()