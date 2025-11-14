class States:
    IDLE = 0
    RUN = 1
    ATTACK = 2
    DEFENSE = 3
    PARRYING = 4
    JUMP = 5
    HIT = 6
    STUN = 7
    DEAD = 8

class StateMachine:
    def __init__(self, owner):
        self.owner = owner
        self.current = States.IDLE

    def change(self, new_state):
        if self.current != new_state:
            self.current = new_state
            self.owner.animator.play(new_state)

    def update(self):
        c = self.owner

        if self.current == States.DEAD:
            return

        if self.current == States.JUMP:
            return
        if self.current == States.STUN:
            return

        if self.current == States.HIT:
            if c.animator.current.isEnd:
                self.change(States.IDLE)
            return

        if self.current == States.ATTACK or self.current == States.PARRYING:
            if c.animator.current.isEnd:
                self.change(States.IDLE)
            return

        if c.useShield:
            self.change(States.DEFENSE)
            return

        if self.current == States.DEFENSE and not c.useShield:
            self.change(States.IDLE)

        if c.x_speed != 0:
            self.change(States.RUN)
        elif c.x_speed == 0:
            self.change(States.IDLE)