from pico2d import *
import game_framework
import select_scene
from Button import Button

bg: Image = None
font: Font = None
start_button:Button = None

def init():
    global bg, button_img, font, start_button

    resize_canvas(800, 600)
    bg = load_image('UI/Game_Title_bg.png')
    font = load_font('ENCR10B.TTF',32)

    start_button = Button('Game Start',400,68)

def finish(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.change_mode(select_scene)

            elif event.key == SDLK_ESCAPE:
                game_framework.quit()


def draw():
    clear_canvas()
    bg.draw(400, 300, 900, 600)
    start_button.draw()
    update_canvas()

def update(): pass

def pause(): pass

def resume(): pass