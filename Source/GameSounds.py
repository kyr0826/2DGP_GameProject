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

def init():
    global attack_sounds, hit_sound, sound_root
    global button_sound, selector_move_sound, selected_sound
    global game_end_sound, title_bgm, ingame_bgm, current_bgm_state

    for name in gv.characters:
        attack_sounds[name] = load_wav(sound_root + name + '_Attack.wav')

    hit_sound = load_wav(sound_root + 'hit.wav')
    hit_sound.set_volume(32)
    game_end_sound = load_wav(sound_root + 'game_end_sound.wav')

    button_sound = load_wav(sound_root + 'button_click.wav')
    button_sound.set_volume(14)

    selector_move_sound = load_wav(sound_root + 'selector_move_sound.wav')
    selected_sound = load_wav(sound_root + 'selected_sound.wav')

    title_bgm = load_music(sound_root + 'title_bgm.mp3')
    title_bgm.set_volume(24)

    ingame_bgm = load_music(sound_root + 'ingame_bgm.mp3')
    ingame_bgm.set_volume(24)

    current_bgm_state = None


def play_title_bgm():
    global current_bgm_state, ingame_bgm, title_bgm

    if current_bgm_state == 'title':
        return

    if ingame_bgm and current_bgm_state == 'ingame':
        ingame_bgm.stop()

    title_bgm.repeat_play()
    current_bgm_state = 'title'


def play_ingame_bgm():
    global current_bgm_state, ingame_bgm, title_bgm

    if current_bgm_state == 'ingame':
        return

    if title_bgm and current_bgm_state == 'title':
        title_bgm.stop()

    ingame_bgm.repeat_play()
    current_bgm_state = 'ingame'