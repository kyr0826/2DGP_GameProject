from pico2d import *
import game_framework
import Global_Variables as gv
from Button import Button
from MapCard import MapCard
import play_scene
import character_select_scene
import GameSounds as gs

bg_img: Image = None
title_font: Font = None

map_sel_btn: Button = None

map_card = []

def init():
    gs.play_title_bgm()
    global bg_img, title_font, map_sel_btn
    bg_img = load_image('UI/Map_Select_bg.png')
    title_font = load_font('ENCR10B.TTF', 48)

    gv.map_idx = 0

    w = gv.GAME_WINDOW_WIDTH
    h = gv.GAME_WINDOW_HEIGHT
    map_frame_x_offset = (w // 2) // 2 + 50
    map_card_y = h // 2

    map_card_0_x = w // 2 - map_frame_x_offset
    map_card_1_x = w // 2
    map_card_2_x = w // 2 + map_frame_x_offset

    map_card_0 = MapCard("Lava Field",0,map_card_0_x,map_card_y)
    map_card.append(map_card_0)

    map_card_1 = MapCard("Crystal Cave",1,map_card_1_x,map_card_y)
    map_card.append(map_card_1)

    map_card_2 = MapCard("Lush Forest",2,map_card_2_x,map_card_y)
    map_card.append(map_card_2)

    map_sel_btn = Button('Select', gv.GAME_WINDOW_WIDTH // 2, 163)
    map_sel_btn.enabled = True
    map_sel_btn.add_event(lambda: game_framework.change_mode(play_scene))

def finish(): pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(character_select_scene)

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                gs.selected_sound.play()
                for card in map_card:
                    card.is_clicked(event.x, event.y)
                map_sel_btn.is_clicked(event.x, event.y)

def draw():
    clear_canvas()
    w = gv.GAME_WINDOW_WIDTH
    h = gv.GAME_WINDOW_HEIGHT
    bg_img.draw(w // 2, h // 2, w, h)

    for card in map_card:
        card.draw()

    title_font.draw(w // 2 - (len('MAP SELECT') * 48 * 0.28), h - 60, 'MAP SELECT', (255, 125, 0))
    map_sel_btn.draw()
    update_canvas()


def update(): pass


def pause(): pass


def resume(): pass
