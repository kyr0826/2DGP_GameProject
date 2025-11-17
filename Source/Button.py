from pico2d import *

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
            Button.btn_font.draw(400 - (len(self.btn_text) * self.font_size * 0.28), 68, self.btn_text, self.font_color)

        else:
            Button.btn_disable_img.draw(self.x, self.y, btn_w, btn_h)
            Button.btn_font.draw(400 - (len(self.btn_text) * self.font_size * 0.28), 68, self.btn_text, (125,125,125))