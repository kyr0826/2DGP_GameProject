from Character import Character
from pico2d import *
import Global_Variables as gv
from StateMachine import States

class Player_Info_bar:
    health_bar_frame : Image = None
    ingame_face_frame : Image = None
    character_face_images = {}
    character_dead_face_images = {}

    def __init__(self, owner:Character, isPlayer1):
        self.owner = owner
        self.isPlayer1 = isPlayer1

        if not Player_Info_bar.health_bar_frame:
            Player_Info_bar.health_bar_frame = load_image('UI/Health_Bar_Frame.png')

        if not Player_Info_bar.ingame_face_frame:
            Player_Info_bar.ingame_face_frame = load_image('UI/InGame_Face_Frame.png')

        if not Player_Info_bar.character_face_images:
            for name in gv.characters:
                Player_Info_bar.character_face_images[name] = load_image(name+'/select_face.png')

        if not Player_Info_bar.character_dead_face_images:
            for name in gv.characters:
                Player_Info_bar.character_dead_face_images[name] = load_image(name+'/select_face_dead.png')

    def draw(self):
        # 선택된 캐릭터 얼굴
        x = 45 if self.isPlayer1 else gv.GAME_WINDOW_WIDTH - 45
        y = gv.GAME_WINDOW_HEIGHT - 50

        Player_Info_bar.ingame_face_frame.draw(x,y,80,80)
        if self.owner.Health > 0.0:
            Player_Info_bar.character_face_images[self.owner.name].draw(x, y, 60, 60)
        else:
            Player_Info_bar.character_dead_face_images[self.owner.name].draw(x, y, 60, 60)


        # 체력바
        y = y - 40
        Player_Info_bar.health_bar_frame.draw(x,y, 70, 22)

        if self.owner.state_machine.current is States.DEAD: return
        healthbar_width = 60
        health_rate = self.owner.Health / self.owner.MAX_HEALTH
        left = x - healthbar_width // 2
        bottom = y - 6

        right = left + healthbar_width * health_rate
        top = y + 6

        draw_rectangle(left, top, right, bottom, 255, 100, 100, 255, True)
