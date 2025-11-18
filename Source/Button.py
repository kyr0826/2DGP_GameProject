from pico2d import *

from Source import GameConstants


class Button:
    btn_enable_img:Image = None
    btn_disable_img:Image = None
    btn_font:Font = None

    def __init__(self, btn_text, x, y, font_color=(255,200,0), scale=1, enabled = True):
        self.btn_text = btn_text

        self.x = x
        self.y = y
        self.scale = scale
        self.enabled = enabled

        self.BTN_WIDTH, self.BTN_HEIGHT = 230, 84

        self.font_color = font_color
        self.font_size = int(26 * scale)

        if not Button.btn_enable_img:
            Button.btn_enable_img = load_image('UI/Button_Frame.png')
        if not Button.btn_disable_img:
            Button.btn_disable_img = load_image('UI/Button_Frame_Disable.png')
        if not Button.btn_font:
            Button.btn_font = load_font('ENCR10B.TTF', self.font_size)

    def draw(self):
        btn_w = self.BTN_WIDTH * self.scale
        btn_h = self.BTN_HEIGHT * self.scale

        if self.enabled:
            Button.btn_enable_img.draw(self.x, self.y, btn_w, btn_h)
            Button.btn_font.draw(self.x - (len(self.btn_text) * self.font_size * 0.28), self.y, self.btn_text, self.font_color)

        else:
            Button.btn_disable_img.draw(self.x, self.y, btn_w, btn_h)
            Button.btn_font.draw(self.x - (len(self.btn_text) * self.font_size * 0.28), self.y, self.btn_text, (125,125,125))

        # 클릭범위 확인용
        if GameConstants.SHOW_DEBUG_RECT:
            draw_rectangle(*self.get_bb())

    def is_clicked(self, mx, my):
        btn_bb = self.get_bb()
        if (self.enabled and
                (btn_bb[0] <= mx <= btn_bb[2]) and
                (btn_bb[1] <= (get_canvas_height()-my) <= btn_bb[3])):

            return True

        return False


    def get_bb(self):
        btn_w = int(self.BTN_WIDTH * self.scale)
        btn_h = int(self.BTN_HEIGHT * self.scale)

        return (self.x - btn_w / 2, self.y - btn_h / 2,
                self.x + btn_w / 2, self.y + btn_h / 2)