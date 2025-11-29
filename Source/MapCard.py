from pico2d import *
import Global_Variables as gv


class MapCard:
    map_card_img: Image = None
    map_card_highlight_img: Image = None
    map_card_font: Font = None

    def __init__(self, map_name, map_num, x, y, font_color=(255, 225, 125), scale=1):
        self.map_name = map_name
        self.map_num = map_num
        self.x, self.y = x, y
        self.font_color = font_color
        self.scale = 0.7 * scale
        self.click_events = []
        self.font_size = int(22 * scale)
        self.map_img = load_image(f'UI/InGame_bg_{map_num}.png')

        if not MapCard.map_card_img:
            MapCard.map_card_img = load_image('UI/Map_Card_Frame.png')
        if not MapCard.map_card_highlight_img:
            MapCard.map_card_highlight_img = load_image('UI/Map_Card_Highlight.png')
        if not MapCard.map_card_font:
            MapCard.map_card_font = load_font('ENCR10B.TTF', self.font_size)

    def draw(self):
        if gv.map_idx == self.map_num:
            MapCard.map_card_highlight_img.draw(self.x, self.y, MapCard.map_card_highlight_img.w * self.scale,
                                                MapCard.map_card_highlight_img.h * self.scale)
        MapCard.map_card_img.draw(self.x, self.y, MapCard.map_card_img.w * self.scale,
                                  MapCard.map_card_img.h * self.scale)

        font_y = self.y + MapCard.map_card_img.h * self.scale * 0.35
        MapCard.map_card_font.draw(self.x - (len(self.map_name) * 22 * 0.28), font_y, self.map_name, self.font_color)

        map_img_w = map_img_h = 260*self.scale
        self.map_img.clip_draw(0,0,self.map_img.w,self.map_img.h,self.x, self.y-34*self.scale, map_img_w, map_img_h)

        if gv.SHOW_DEBUG_RECT:
            draw_rectangle(*self.get_bb())

    def is_clicked(self, mx, my):
        card_bb = self.get_bb()
        if ((card_bb[0] <= mx <= card_bb[2]) and
            (card_bb[1] <= (get_canvas_height() - my) <= card_bb[3])):
            gv.map_idx = self.map_num

    def get_bb(self):
        card_w = int(MapCard.map_card_img.w * self.scale)
        card_h = int(MapCard.map_card_img.h * self.scale)

        return (self.x - card_w / 2, self.y - card_h / 2,
                self.x + card_w / 2, self.y + card_h / 2)
