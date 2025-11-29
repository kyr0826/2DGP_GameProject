from MapGenerator import *
from Character import *
from InputManager import *
from Source import game_world, character_select_scene
from Volcano import Volcano
from Source.CollisionManager import add_collision_pair, add_list_collision_pair, handle_collisions
import Lobby_scene
import Global_Variables as gv
from Player_Info_bar import Player_Info_bar
from Button import Button

input_mgr = None
p1_info, p2_info = None, None
volcano_rising_timer = 0.0
volcano = None

time_frame_img: Image = None
time_font: Font = None

popup_bg_img: Image = None
popup_font: Font = None
retry_btn: Button = None
exit_btn: Button = None

def init():
    global input_mgr, p1_info, p2_info, volcano_rising_timer, volcano

    global time_frame_img, time_font
    time_frame_img = load_image("UI/Time_Frame.png")
    time_font = load_font("ENCR10B.TTF", size=24)

    global popup_bg_img, popup_font, retry_btn, exit_btn
    popup_bg_img = load_image("UI/PopUp_BG_Alpha.png")
    popup_font = load_font("ENCR10B.TTF", size=32)

    retry_btn = Button("FightAgain", 0, 0)
    retry_btn.add_event(lambda: game_framework.change_mode(character_select_scene))

    exit_btn = Button("Exit", 0, 0)
    exit_btn.add_event(lambda: game_framework.change_mode(Lobby_scene))

    volcano_rising_timer = gv.Volcano_rising_wait_time
    init_map(gv.map_idx)

    input_mgr = InputManager()

    cx = gv.GAME_WINDOW_WIDTH // 2
    player1 = Character(gv.selected_characters['player1'], cx-50, 150, input_mgr,
                        {'left': SDLK_a, 'right': SDLK_d, 'jump': SDLK_w, 'down': SDLK_s,
                         'attack': SDLK_g, 'defense': SDLK_h, 'parrying': SDLK_j})

    p1_info = Player_Info_bar(player1, True)

    player2 = Character(gv.selected_characters['player2'], cx+50, 150, input_mgr,
                        {'left': SDLK_LEFT, 'right': SDLK_RIGHT, 'jump': SDLK_UP, 'down': SDLK_DOWN,
                         'attack': SDLK_KP_1, 'defense': SDLK_KP_2, 'parrying': SDLK_KP_3})

    p2_info = Player_Info_bar(player2, False)

    players = [player1, player2]
    game_world.add_objects(players)

    if volcano is None:
        volcano = Volcano()
    volcano.isLavaRising = False
    volcano.height = 0

    game_world.add_object(volcano, 1)

    platforms = get_platforms()

    add_list_collision_pair('player:map', players, platforms)
    add_list_collision_pair('player:player', players, players)

    add_list_collision_pair('attack:hit', players, players)

    add_list_collision_pair('player:volcano', players, None)
    add_collision_pair('player:volcano', None, volcano)


def finish():
    global collision_pairs, volcano
    game_world.clear()
    collision_pairs = {}
    gv.isGameEnd = False
    gv.isGamePaused = False
    game_framework.set_time_scale(1.0)

def handle_events():
    global retry_btn, exit_btn
    events = get_events()

    input_mgr.update(events)
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE and not gv.isGameEnd:
                gv.isGamePaused = not gv.isGamePaused
                global retry_btn, exit_btn
                if gv.isGamePaused:
                    retry_btn.enabled = True
                    exit_btn.enabled = True
                    game_framework.set_time_scale(0.0)
                else:
                    retry_btn.enabled = False
                    exit_btn.enabled = False
                    game_framework.set_time_scale(1.0)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                retry_btn.is_clicked(event.x, event.y)
                exit_btn.is_clicked(event.x, event.y)

def draw_popup():
    global popup_bg_img, popup_font, retry_btn, exit_btn
    popup_x = gv.GAME_WINDOW_WIDTH // 2
    popup_y = gv.GAME_WINDOW_HEIGHT // 2 - 30

    popup_bg_img.draw(popup_x, popup_y)

    if gv.isGameEnd:
        retry_btn.enabled = True
        exit_btn.enabled = True
        popup_font.draw(popup_x-(len("Winer : ") * 32 * 0.28), popup_y, "Winer : ", (255, 120, 55))

    retry_btn.x = popup_x - 150
    retry_btn.y = popup_y - popup_bg_img.h//2 + 100
    retry_btn.draw()

    exit_btn.x = popup_x + 150
    exit_btn.y = popup_y - popup_bg_img.h//2 + 100
    exit_btn.draw()


def draw():
    global time_frame_img, time_font

    clear_canvas()

    draw_map()

    game_world.render()

    p1_info.draw()
    p2_info.draw()

    time_frame_w = 140
    time_frame_h = 40

    time_frame_x = gv.GAME_WINDOW_WIDTH // 2
    time_frame_y = gv.GAME_WINDOW_HEIGHT - time_frame_h // 2 - 6

    time_frame_img.draw(time_frame_x, time_frame_y, time_frame_w, time_frame_h)
    minutes = int(volcano_rising_timer // 60)
    seconds = int(volcano_rising_timer % 60)
    time_text = f"{minutes:02d}:{seconds:02d}"
    time_font.draw(time_frame_x - (len(time_text) * 24 * 0.28), time_frame_y, time_text, (255, 125, 0))

    if gv.isGamePaused or gv.isGameEnd:
        draw_popup()

    update_canvas()


def update():
    global volcano_rising_timer

    if not volcano.isLavaRising and volcano_rising_timer > 0:
        volcano_rising_timer -= game_framework.frame_time
        if volcano_rising_timer <= 0:
            volcano_rising_timer = 0
            volcano.isLavaRising = True

    game_world.update()
    handle_collisions()


def pause():
    pass


def resume():
    pass
