from pico2d import open_canvas, close_canvas
import game_framework
import Splash_scene
import GameSounds as gs

open_canvas(800,750)
gs.init()

game_framework.run(Splash_scene)
close_canvas()