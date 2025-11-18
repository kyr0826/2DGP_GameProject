from pico2d import *
import game_framework
from Button import Button
import Lobby_scene
import play_scene
import GameConstants as gc

name_frame: Image = None
select_frame: Image = None
bg: Image = None

character_images = []
font: Font = None
key_font: Font = None
play_button: Button = None

def init():
    global bg, character_images, select_frame, name_frame, play_button
    global font, key_font
    print('character select Init')
    print(gc.p1_index, gc.p2_index)
    # 초기화
    gc.selected_characters['player1'] = gc.characters[gc.p1_index]
    gc.selected_characters['player2'] = gc.characters[gc.p2_index]

    gc.p1_selected = False
    gc.p2_selected = False

    # 리소스 로드
    bg = load_image('UI/Character_Select_bg.png')
    name_frame = load_image('UI/Name_Frame.png')
    select_frame = load_image('UI/Select_Frame.png')

    # 캐릭터 이미지 로드
    for char in gc.characters:
        character_images.append(load_image(f'{char}/select_face.png'))

    font = load_font('ENCR10B.TTF', 24)
    key_font = load_font('ENCR10B.TTF', 15)
    play_button = Button('Game Play', gc.GAME_WINDOW_WIDTH // 2, 143)
    play_button.add_event(lambda: game_framework.change_mode(play_scene))

def finish():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if not gc.p1_selected:
                if event.key == SDLK_a:
                    gc.p1_index = (gc.p1_index - 1) % len(gc.characters)
                elif event.key == SDLK_d:
                    gc.p1_index = (gc.p1_index + 1) % len(gc.characters)
                elif event.key == SDLK_g:
                    gc.p1_selected = True
                gc.selected_characters['player1'] = gc.characters[gc.p1_index]

            if not gc.p2_selected:
                if event.key == SDLK_LEFT:
                    gc.p2_index = (gc.p2_index - 1) % len(gc.characters)
                elif event.key == SDLK_RIGHT:
                    gc.p2_index = (gc.p2_index + 1) % len(gc.characters)
                elif event.key == SDLK_KP_1:
                    gc.p2_selected = True
                gc.selected_characters['player2'] = gc.characters[gc.p2_index]

            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(Lobby_scene)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                play_button.is_clicked(event.x, event.y)


def update():
    pass


def draw():
    clear_canvas()
    draw_rectangle(0, 0, 800, 750, 0, 0, 0, 255, True)

    # 배경
    bg.draw(gc.GAME_WINDOW_WIDTH // 2, gc.GAME_WINDOW_HEIGHT // 2, bg.w, bg.h)

    # 캐릭터 카드 그리기
    card_y = 375
    card_size = 200
    card_spacing = 30

    name_card_spacing = 20
    name_w = int(card_size * 0.9)
    name_h = int(name_w * 0.2)
    name_y = card_y - card_size / 2 - name_card_spacing

    # P1
    x = gc.GAME_WINDOW_WIDTH // 2 - card_size / 2 - card_spacing
    font.draw(x - (len('P1') * 24 * 0.28), card_y + 110, 'P1', (125, 125, 125))

    select_frame.draw(x, card_y, card_size, card_size)
    character_images[gc.p1_index].draw(x, card_y, card_size - 50, card_size - 50)
    name_frame.draw(x, name_y, name_w, name_h)
    font_color = (255, 255, 255) if not gc.p1_selected else (255, 255, 0)
    font.draw(x - (len(gc.characters[gc.p1_index]) * 24 * 0.28), name_y, gc.characters[gc.p1_index], font_color)

    # Key
    key_texts = ['[ P1 Controls ]',
                 'Move     A/D',
                 'Jump     W',
                 'Down     S',
                 'Attack   G',
                 'Select   G',
                 'Defend   H',
                 'Parry    J']
    key_x = 25
    key_y = card_y + card_size//2 - 25
    for i in range(len(key_texts)):
        key_font.draw(key_x, key_y - 20 * i, key_texts[i], (125, 125, 125))

    # P2
    x = gc.GAME_WINDOW_WIDTH // 2 + card_size / 2 + card_spacing

    font.draw(x - (len('P2') * 24 * 0.28), card_y + 110, 'P2', (125, 125, 125))

    select_frame.draw(x, card_y, card_size, card_size)
    character_images[gc.p2_index].draw(x, card_y, card_size - 50, card_size - 50)
    name_frame.draw(x, name_y, name_w, name_h)
    font_color = (255, 255, 255) if not gc.p2_selected else (255, 255, 0)
    font.draw(x - (len(gc.characters[gc.p2_index]) * 24 * 0.28), name_y, gc.characters[gc.p2_index], font_color)

    # Key
    key_texts = ['[ P2 Controls ]',
                 'Move   LEFT/RIGHT',
                 'Jump   UP',
                 'Down   DOWN',
                 'Attack NUMPAD_1',
                 'Select NUMPAD_1',
                 'Defend NUMPAD_2',
                 'Parry  NUMPAD_3']
    key_x = x + card_size//2 + 5
    for i in range(len(key_texts)):
        key_font.draw(key_x, key_y - 20 * i, key_texts[i], (125, 125, 125))

    # 준비 상태 표시
    if gc.p1_selected:
        x = 400 - card_size / 2 - card_spacing
        font.draw(x - (len("1P Ready!") * 24 * 0.28), name_y - 35, "1P Ready!", (255, 200, 0))

    if gc.p2_selected:
        x = 400 + card_size / 2 + card_spacing
        font.draw(x - (len("2P Ready!") * 24 * 0.28), name_y - 35, "2P Ready!", (255, 200, 0))

    play_button.enabled = gc.p1_selected and gc.p2_selected
    play_button.draw()

    update_canvas()


def pause(): pass


def resume(): pass
