from pico2d import open_canvas, close_canvas
import game_framework

import Splash_scene
import map_select__scene

open_canvas(800,750)
game_framework.run(map_select__scene)
close_canvas()