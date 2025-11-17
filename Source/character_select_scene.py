from pico2d import *
import game_framework
from Button import Button
import Lobby_scene
import play_scene
from GameConstants import *


name_frame: Image = None
select_frame: Image = None
bg: Image = None

character_images = []
font: Font = None
play_button:Button = None

def init():
    global bg, character_images, select_frame, name_frame, play_button
    global p1_index, p2_index, p1_selected, p2_selected
    global font

    # 초기화
    p1_index = 0
    p2_index = 0
    p1_selected = False
    p2_selected = False
    selected_characters['player1'] = None
    selected_characters['player2'] = None

    # 리소스 로드
    bg = load_image('UI/Character_Select_bg.png')
    name_frame = load_image('UI/Name_Frame.png')
    select_frame = load_image('UI/Select_Frame.png')

    # 캐릭터 이미지 로드
    for char in characters:
        character_images.append(load_image(f'{char}/select_face.png'))

    font = load_font('ENCR10B.TTF', 24)
    play_button = Button('Game Play',GAME_WINDOW_WIDTH//2, 143)

def finish():
    pass


def handle_events():
    global p1_index, p2_index, p1_selected, p2_selected

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if not p1_selected:
                if event.key == SDLK_a:
                    p1_index = (p1_index - 1) % len(characters)
                elif event.key == SDLK_d:
                    p1_index = (p1_index + 1) % len(characters)
                elif event.key == SDLK_g:
                    p1_selected = True
                selected_characters['player1'] = characters[p1_index]

            if not p2_selected:
                if event.key == SDLK_LEFT:
                    p2_index = (p2_index - 1) % len(characters)
                elif event.key == SDLK_RIGHT:
                    p2_index = (p2_index + 1) % len(characters)
                elif event.key == SDLK_KP_1:
                    p2_selected = True
                selected_characters['player2'] = characters[p2_index]

            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(Lobby_scene)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                if play_button.is_clicked(event.x, event.y):
                    game_framework.change_mode(play_scene)




def update():
    pass


def draw():
    clear_canvas()
    draw_rectangle(0, 0, 800, 750, 0, 0, 0, 255, True)

    # 배경
    bg.draw(GAME_WINDOW_WIDTH//2, GAME_WINDOW_HEIGHT//2, bg.w, bg.h)

    # 캐릭터 카드 그리기
    card_y = 375
    card_size = 200
    card_spacing = 100

    name_card_spacing = 20
    name_w = int(card_size * 0.9)
    name_h = int(name_w * 0.2)
    name_y = card_y - card_size / 2 - name_card_spacing

    # P1
    x = 400 - card_size / 2 - card_spacing
    select_frame.draw(x, card_y, card_size, card_size)
    character_images[p1_index].draw(x, card_y, card_size - 50, card_size - 50)
    name_frame.draw(x, name_y, name_w, name_h)
    font_color = (255, 255, 255) if not p1_selected else (255, 255, 0)
    font.draw(x - (len(characters[p1_index]) * 24 * 0.28), name_y, characters[p1_index], font_color)

    # P2
    x = 400 + card_size / 2 + card_spacing
    select_frame.draw(x, card_y, card_size, card_size)
    character_images[p2_index].draw(x, card_y, card_size - 50, card_size - 50)
    name_frame.draw(x, name_y, name_w, name_h)
    font_color = (255, 255, 255) if not p2_selected else (255, 255, 0)
    font.draw(x - (len(characters[p2_index]) * 24 * 0.28), name_y, characters[p2_index], font_color)

    # 준비 상태 표시
    if p1_selected:
        x = 400 - card_size / 2 - card_spacing
        font.draw(x - (len("1P Ready!") * 24 * 0.28), name_y - 35, "1P Ready!", (255, 200, 0))

    if p2_selected:
        x = 400 + card_size / 2 + card_spacing
        font.draw(x - (len("2P Ready!") * 24 * 0.28), name_y - 35, "2P Ready!", (255, 200, 0))

    play_button.enabled = p1_selected and p2_selected
    play_button.draw()

    update_canvas()


def pause(): pass


def resume(): pass