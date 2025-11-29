from pico2d import *
import game_framework
import Global_Variables as gv
from Button import Button
import play_scene
import character_select_scene

bg_img: Image = None
title_font: Font = None

map_sel_frame: Image = None
map_sel_frame_highlight: Image = None
map_sel_font: Font = None

map_sel_btn: Button = None


def init():
    global bg_img, title_font, map_sel_frame, map_sel_frame_highlight, map_sel_font, map_sel_btn
    bg_img = load_image('UI/Map_Select_bg.png')
    title_font = load_font('ENCR10B.TTF', 48)

    map_sel_frame = load_image('UI/Map_Card_Frame.png')
    map_sel_frame_highlight = load_image('UI/Map_Card_Highlight.png')
    map_sel_font = load_font('ENCR10B.TTF', 24)

    map_sel_btn = Button('Select', gv.GAME_WINDOW_WIDTH // 2, 163)
    map_sel_btn.enabled = True
    map_sel_btn.add_event(lambda: game_framework.change_mode(play_scene))

    gv.map_idx = 0


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


def draw_map_frame(map_name, x, y, highlight, scale=0.65):
    global map_sel_frame, map_sel_frame_highlight, map_sel_font

    if highlight:
        map_sel_frame_highlight.draw(x, y, map_sel_frame_highlight.w * scale, map_sel_frame_highlight.h * scale)
    map_sel_frame.draw(x, y, map_sel_frame.w * scale, map_sel_frame.h * scale)

    font_y = y + map_sel_frame.h * scale * 0.35
    map_sel_font.draw(x - (len(map_name) * 24 * 0.28), font_y, map_name, (255, 125, 0))


def draw():
    clear_canvas()
    w = gv.GAME_WINDOW_WIDTH
    h = gv.GAME_WINDOW_HEIGHT
    bg_img.draw(w // 2, h // 2, w, h)

    # 800
    #  200 400 600
    # 310 376
    map_frame_x_offset = (w // 2) // 2 + 50
    map_card_y = h // 2

    map_card_1_x = w // 2 - map_frame_x_offset
    map_card_2_x = w // 2
    map_card_3_x = w // 2 + map_frame_x_offset

    draw_map_frame("map_1", map_card_1_x, map_card_y, gv.map_idx == 0)
    draw_map_frame("map_2", map_card_2_x, map_card_y, gv.map_idx == 1)
    draw_map_frame("map_3", map_card_3_x, map_card_y, gv.map_idx == 2)

    title_font.draw(w // 2 - (len('MAP SELECT') * 48 * 0.28), h - 60, 'MAP SELECT', (255, 125, 0))
    map_sel_btn.draw()
    update_canvas()


def update(): pass


def pause(): pass


def resume(): pass
