from pico2d import load_music, load_wav, Wav, Music
import Global_Variables as gv

attack_sounds: dict[str, Wav] = {}
hit_sound: Wav = None
game_end_sound: Wav = None
button_sound: Wav = None
selector_move_sound: Wav = None
selected_sound: Wav = None

title_bgm: Music = None
ingame_bgm: Music = None

sound_root = 'Sounds/'

current_bgm_state = None

def init(): pass
def play_title_bgm(): pass
def play_ingame_bgm(): pass
def stop_all_bgm(): pass