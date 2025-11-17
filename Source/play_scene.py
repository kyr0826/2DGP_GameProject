from MapGenerator import *
from Character import *
from InputManager import *
from Source import game_world, GameConstants
from Volcano import Volcano
from Source.CollisionManager import add_collision_pair, add_list_collision_pair, handle_collisions
import Lobby_scene
from GameConstants import *
from Player_Info_bar import Player_Info_bar

input_mgr = None
p1_info, p2_info = None, None
volcano_rising_timer = 0.0
volcano = None

time_frame_img : Image = None
time_font : Font = None

def init():
    global input_mgr,p1_info,p2_info, volcano_rising_timer, volcano

    global time_frame_img, time_font
    time_frame_img = load_image("UI/Time_Frame.png")
    time_font = load_font("ENCR10B.TTF", size=24)

    GameConstants.isGameEnd = False

    volcano_rising_timer = Volcano_rising_wait_time
    init_map()

    input_mgr = InputManager()

    player1 = Character(selected_characters['player1'], 300, 300, input_mgr,
                        {'left': SDLK_a, 'right': SDLK_d, 'jump': SDLK_w, 'down': SDLK_s,
                         'attack': SDLK_g, 'defense': SDLK_h, 'parrying': SDLK_j})

    p1_info = Player_Info_bar(player1,True)


    player2 = Character(selected_characters['player2'], 500, 300, input_mgr,
                        {'left': SDLK_LEFT, 'right': SDLK_RIGHT, 'jump': SDLK_UP, 'down': SDLK_DOWN,
                         'attack': SDLK_KP_1, 'defense': SDLK_KP_2, 'parrying': SDLK_KP_3})

    p2_info = Player_Info_bar(player2, False)

    volcano = Volcano()
    game_world.add_object(volcano,1)

    players = [player1, player2]
    game_world.add_objects(players)

    platforms = get_platforms()

    add_list_collision_pair('player:map', players, platforms)
    add_list_collision_pair('player:player', players, players)

    add_list_collision_pair('attack:hit', players, players)

    add_list_collision_pair('player:volcano', players, None)
    add_collision_pair('player:volcano', None, volcano)

def finish():
    global collision_pairs
    game_world.clear()
    collision_pairs={}

def handle_events():
    events = get_events()

    if not GameConstants.isGameEnd:
        input_mgr.update(events)

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(Lobby_scene)

def draw():
    global time_frame_img, time_font

    clear_canvas()

    draw_map()

    game_world.render()

    p1_info.draw()
    p2_info.draw()

    time_frame_w = 140
    time_frame_h = 40

    time_frame_x = GAME_WINDOW_WIDTH // 2
    time_frame_y = GAME_WINDOW_HEIGHT - time_frame_h//2 - 6

    time_frame_img.draw(time_frame_x, time_frame_y, time_frame_w, time_frame_h)
    minutes = int(volcano_rising_timer // 60)
    seconds = int(volcano_rising_timer % 60)
    time_text = f"{minutes:02d}:{seconds:02d}"
    time_font.draw(time_frame_x - (len(time_text) * 24 * 0.28), time_frame_y,time_text,(255,125,0))

    update_canvas()

def update():
    global volcano_rising_timer

    if not volcano.isLavaRising and volcano_rising_timer > 0 :
        volcano_rising_timer -= game_framework.frame_time
        if volcano_rising_timer <= 0 :
            volcano_rising_timer = 0
            volcano.isLavaRising = True

    game_world.update()
    handle_collisions()

def pause():
    pass

def resume():
    pass