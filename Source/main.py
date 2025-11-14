from Character import *
from InputManager import *
from Source.CollisionManager import add_collision_pair, add_list_collision_pair, handle_collisions
from MapGenerator import *
from Volcano import Volcano

def main():
    open_canvas(800,750)

    init_map()

    running = True
    input_mgr = InputManager()

    player1 = Character('Shinobi',300,300,
                       {'left':SDLK_a, 'right':SDLK_d, 'jump':SDLK_w, 'down':SDLK_s,
                                'attack':SDLK_g, 'defense':SDLK_h, 'parrying':SDLK_j})

    player2 = Character('Samurai', 500, 300,
                        {'left': SDLK_LEFT, 'right': SDLK_RIGHT, 'jump': SDLK_UP,'down':SDLK_DOWN,
                         'attack': SDLK_KP_1, 'defense': SDLK_KP_2, 'parrying': SDLK_KP_3})

    volc = Volcano()
    players = [player1, player2]
    platforms = get_platforms()

    add_list_collision_pair('player:map', players, platforms)
    add_list_collision_pair('player:player', players, players)

    add_list_collision_pair('attack:hit', players, players)
    add_list_collision_pair('player:volcano', players, None)
    add_collision_pair('player:volcano', None, volc)

    while running:
        input_mgr.update()
        running = not input_mgr.get_key_down(SDLK_ESCAPE)
        volc.isLavaRising = input_mgr.get_key_down(SDLK_SPACE)

        player1.update(input_mgr, 0.01)
        player2.update(input_mgr, 0.01)
        volc.update(0.01)

        handle_collisions()

        clear_canvas()
        draw_map()
        player1.draw()
        player2.draw()
        volc.draw()
        update_canvas()

        delay(0.01)

    close_canvas()

if __name__ == '__main__':
    main()