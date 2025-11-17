from pico2d import *
import game_framework
import select_scene

bg: Image = None
font: Font = None
button_img: Image = None


def init():
    global bg, button_img, font

    resize_canvas(800, 600)
    bg = load_image('UI/Game_Title_bg.png')
    font = load_font('ENCR10B.TTF',32)

    button_img = load_image('UI/Button_Frame.png')

def finish(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.change_scene(select_scene)

            elif event.key == SDLK_ESCAPE:
                game_framework.quit()


def draw():
    clear_canvas()
    bg.draw(400, 300, 900, 600)

    # 버튼 위치 테스트
    button_img.draw(400, 68, 230, 84)
    btn_text = 'Start'
    font.draw(400 - (len(btn_text) * 32 * 0.28), 68, btn_text, (255,255,100))
    update_canvas()

def update(): pass

def pause(): pass

def resume(): pass