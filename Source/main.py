from pico2d import *

def main():
    open_canvas(800,600)
    running = True
    # input_mgr = InputManager()

    #player = Character(400,300, {'left':SDLK_a, 'right':SDLK_d})

    while running:
        #input_mgr.update()
        #player.update(input_mgr, deltaTime)

        clear_canvas()
        #player.draw()
        update_canvas()

        delay(0.01)

    close_canvas()

if __name__ == '__main__':
    main()