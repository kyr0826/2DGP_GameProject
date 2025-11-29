from pico2d import *
import Global_Variables as gv


class MapCard:
    map_card_img: Image = None
    map_card_highlight_img: Image = None
    map_card_font: Font = None

    def __init__(self, map_name, map_num, x, y, font_color=(255, 125, 0), scale=1, highlight=False):
        self.map_name = map_name
        self.map_num = map_num
        self.x, self.y = x, y
        self.font_color = font_color
        self.scale = 0.7 * scale
        self.highlight = highlight
        self.click_events = []
        self.font_size = int(26 * scale)
        self.map_img = load_image(f'UI/InGame_bg_{map_num}.png')

        if not MapCard.map_card_img:
            MapCard.map_card_img = load_image('UI/Map_Card_Frame.png')
        if not MapCard.map_card_highlight_img:
            MapCard.map_card_highlight_img = load_image('UI/Map_Card_Highlight.png')
        if not MapCard.map_card_font:
            MapCard.map_card_font = load_font('ENCR10B.TTF', self.font_size)

    def draw(self): pass

    def is_clicked(self, mx, my): pass

    def add_event(self, event): pass

    def get_bb(self): pass
