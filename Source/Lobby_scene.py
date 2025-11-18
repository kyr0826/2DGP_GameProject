from pico2d import *
import game_framework
import character_select_scene
from Button import Button
import GameConstants as gc

bg: Image = None
font: Font = None
start_button:Button = None

def init():
    global bg, font, start_button
    bg = load_image('UI/Game_Title_bg.png')
    font = load_font('ENCR10B.TTF',32)

    start_button = Button('Game Start',gc.GAME_WINDOW_WIDTH//2,163)
    start_button.add_event(lambda :game_framework.change_mode(character_select_scene))

    print('Lobby Init')
    gc.p1_index = 0
    gc.p2_index = 0
    print(gc.p1_index, gc.p2_index)

def finish(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                start_button.is_clicked(event.x, event.y)


def draw():
    clear_canvas()
    draw_rectangle(0, 0, 800, 750, 0, 0, 0, 255, True)
    bg.draw(400, 375, 900, 600)
    start_button.draw()
    update_canvas()

def update(): pass

def pause(): pass

def resume(): pass