from AnimationSystem import *
import game_framework
from Source import Global_Variables

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
GRAVITY = 9.81
KNOCKBACK_SPEED = PIXEL_PER_METER * 5.0

class Character:
    def __init__(self, name, x, y, input_mgr, controls):
        self.input_mgr = input_mgr
        self.name = name

        self.MAX_HEALTH = 150.0
        self.Health = self.MAX_HEALTH

        self.pos_x,self.pos_y = x, y
        self.speed, self.x_speed, self.y_speed = 20, 0, 0
        self.last_dir = 1

        self.isGrounded = True
        self.useShield = False

        self.isJumping = False
        self.MIN_JUMP_SPEED = PIXEL_PER_METER * 5.0
        self.MAX_JUMP_SPEED = PIXEL_PER_METER * 20.0

        self.isBrakingJump = False
        self.JUMP_BREAK_FACTOR = 20.0

        self.is_dropping_down = False
        self.dropping_timer = 0.0
        self.just_landed = False

        self.PARRY_COOLDOWN = 1.0
        self.parry_cooldown_timer = 0.0

        self.STUN_DURATION = 2.0
        self.stun_timer = 0.0

        self.INVINCIBLE_DURATION_HIT = 0.3
        self.INVINCIBLE_DURATION_DEFENSE = 0.1
        self.INVINCIBLE_DURATION_Volcano = 1.0
        self.invincible_timer = 0.0

        self.controls = controls
        self.animator = Animator(self)
        self.state_machine = StateMachine(self)
        self.load_animations()

    def load_animations(self):
        idle = load_image(self.name + '/Idle.png')
        run =  load_image(self.name + '/Run.png')

        self.animator.add(States.IDLE, Animation(self, idle, 6, 12, True))
        self.animator.add(States.RUN, Animation(self, run, 8, 16, True))

        attack_frame_count = 0
        defense_frame_count = 0
        parrying_frame_count = 0
        jump_frame_count = 0
        hit_frame_count = 0
        dead_frame_count = 0

        attack, defense, parrying, jump, hit = None, None, None, None, None

        if self.name == 'Fighter':
            attack = load_image(self.name + '/Attack_1.png')
            defense = load_image(self.name + '/Shield.png')
            parrying = load_image(self.name + '/Attack_3.png')
            attack_frame_count = 4
            defense_frame_count = 2
            parrying_frame_count = 4
            jump_frame_count = 5
            hit_frame_count = 3
            dead_frame_count = 3

        elif self.name == 'Samurai':
            attack = load_image(self.name + '/Attack_3.png')
            defense = load_image(self.name + '/Shield.png')
            parrying = load_image(self.name + '/Attack_1.png')
            attack_frame_count = 3
            defense_frame_count = 2
            parrying_frame_count = 6
            jump_frame_count = 7
            hit_frame_count = 2
            dead_frame_count = 3

        elif self.name == 'Shinobi':
            attack = load_image(self.name + '/Attack_1.png')
            defense = load_image(self.name + '/Shield.png')
            parrying = load_image(self.name + '/Attack_3.png')
            attack_frame_count = 5
            defense_frame_count = 4
            parrying_frame_count = 4
            jump_frame_count = 6
            hit_frame_count = 2
            dead_frame_count = 4

        jump = load_image(self.name + '/Jump.png')
        self.animator.add(States.JUMP, Animation(self, jump, jump_frame_count, jump_frame_count * 6, False))

        self.animator.add(States.ATTACK, Animation(self, attack, attack_frame_count, attack_frame_count * 3, False))
        self.animator.add(States.DEFENSE, Animation(self, defense, defense_frame_count, defense_frame_count * 8, True))
        self.animator.add(States.PARRYING, Animation(self, parrying, parrying_frame_count, parrying_frame_count * 6, False))

        hit = load_image(self.name + '/Hurt.png')
        self.animator.add(States.HIT, Animation(self, hit, hit_frame_count, hit_frame_count * 6, False))
        self.animator.add(States.STUN, Animation(self, hit, hit_frame_count, hit_frame_count * 6, True))

        dead = load_image(self.name + '/Dead.png')
        self.animator.add(States.DEAD, Animation(self, dead, dead_frame_count, dead_frame_count * 6, False))

        self.animator.play(States.IDLE)

    def update(self):
        delta_time = game_framework.frame_time

        if GameConstants.isGamePaused:
            return

        if GameConstants.isGameEnd:
            self.animator.update(delta_time)
            if self.Health > 0:
                if self.state_machine.current is not States.IDLE:
                    self.state_machine.change(States.IDLE)
            return

        SPEED_MPM = (self.speed * 1000.0 / 60.0)
        SPEED_MPS = (SPEED_MPM / 60.0)
        SPEED_PPS = (SPEED_MPS * PIXEL_PER_METER)

        # 무적시간
        if self.invincible_timer > 0:
            self.invincible_timer -= delta_time
            if self.invincible_timer <= 0:
                self.invincible_timer = 0
                self.animator.isBlinking = False
                self.animator.isVisible = True

        if self.parry_cooldown_timer > 0:
            self.parry_cooldown_timer -= delta_time

        if self.stun_timer > 0:
            self.stun_timer -= delta_time

        if self.dropping_timer > 0:
            self.dropping_timer -= delta_time
            if self.dropping_timer <= 0:
                self.dropping_timer = 0
                self.is_dropping_down = False

        if self.state_machine.current == States.STUN:
            self.x_speed = 0
            if self.stun_timer <= 0:
                self.state_machine.change(States.IDLE)
            return

        if not self.isGrounded:
            self.just_landed = False

        self.y_speed -= GRAVITY * SPEED_PPS * delta_time

        if self.isGrounded:
            self.useShield = self.input_mgr.get_key_down(self.controls['defense'])

            if self.just_landed and self.input_mgr.get_key_press(self.controls['down']):
                self.dropping_timer = 0.3
                self.is_dropping_down = True
                self.isGrounded = False

            if (not self.is_dropping_down) and self.input_mgr.get_key_down(self.controls['jump']):
                self.y_speed = self.MAX_JUMP_SPEED
                self.isGrounded = False
                self.isJumping = True
                self.isBrakingJump = False
                self.state_machine.change(States.JUMP)

            if not self.useShield and self.state_machine.current != States.HIT:
                if self.input_mgr.get_key_press(self.controls['attack']):
                    self.state_machine.change(States.ATTACK)

                elif self.input_mgr.get_key_press(self.controls['parrying']) and self.parry_cooldown_timer <= 0:
                    self.state_machine.change(States.PARRYING)
                    self.parry_cooldown_timer = self.PARRY_COOLDOWN
        else:
            self.useShield = False

        if self.input_mgr.get_key_up(self.controls['jump']) and self.isJumping:
            self.isJumping = False
            self.isBrakingJump = True

        if self.isBrakingJump:
            target_speed = self.MIN_JUMP_SPEED
            self.y_speed += (target_speed - self.y_speed)*self.JUMP_BREAK_FACTOR * delta_time
            if self.y_speed <= target_speed:
                self.isBrakingJump = False

        if (self.isJumping or self.isBrakingJump) and self.y_speed <= 0:
            self.isJumping = False
            self.isBrakingJump = False

        move = self.input_mgr.get_axis(self.controls['left'], self.controls['right'])
        is_busy = self.state_machine.current in [States.ATTACK, States.PARRYING, States.DEFENSE, States.HIT, States.STUN]
        if move != 0 and not is_busy:
            self.last_dir = move

        air_multiplier = 1.0 if self.isGrounded else 0.8

        if is_busy:
            if self.state_machine.current != States.HIT:
                self.x_speed = 0
        else:
            self.x_speed = move * air_multiplier * SPEED_PPS

        self.pos_x += self.x_speed * 1.5 * delta_time
        if self.pos_x <= 20:            self.pos_x = 20
        elif self.pos_x >= 800-20:      self.pos_x = 800-20

        self.pos_y += self.y_speed * delta_time

        self.state_machine.update()
        self.animator.update(delta_time)

        self.just_landed = False
        self.isGrounded = False

    def take_damage(self, amount, group):
        if self.invincible_timer > 0 : return

        self.Health -= amount
        if self.Health <= 0:  # dead
            self.Health = 0
            self.animator.isBlinking = False
            self.animator.isVisible = True
            self.state_machine.change(States.DEAD)
            GameConstants.isGameEnd = True
            return

        if group == 'player:volcano':
            self.invincible_timer = self.INVINCIBLE_DURATION_Volcano
            self.animator.isBlinking = True
        elif self.state_machine.current is States.DEFENSE:
            self.invincible_timer = self.INVINCIBLE_DURATION_DEFENSE
        else:
            self.invincible_timer = self.INVINCIBLE_DURATION_HIT
            self.animator.isBlinking = True

    def handle_collision(self, group, other):
        if group == 'player:map':
            is_oneway = other.type == 'one-way'

            if is_oneway and self.is_dropping_down:
                return

            platform_rect = other.rect
            platform_top = platform_rect[3]

            player_foot_bottom = self.get_foot_bb()[1]
            diff = platform_top - player_foot_bottom

            LANDING_TOLERANCE = 10.0
            can_land = False

            is_moving_down = self.y_speed < 0

            if not is_oneway or (is_oneway and is_moving_down):
                if 0 <= diff <= LANDING_TOLERANCE:
                    can_land = True

            if can_land:
                self.y_speed = 0
                self.isGrounded = True
                self.isJumping = False
                self.isBrakingJump = False

                self.is_dropping_down = False

                self.just_landed = True

                self.pos_y = platform_top + 64

                if self.state_machine.current == States.JUMP:
                    self.state_machine.change(States.IDLE)
        elif group == 'player:player':
            my_bb = self.get_bb()
            other_bb = other.get_bb()

            overlap_left = other_bb[2] - my_bb[0]
            overlap_right = my_bb[2] - other_bb[0]

            overlap_depth = min(overlap_left, overlap_right)

            if self.pos_x < other.pos_x:
                self.pos_x -= overlap_depth / 2
            else:
                self.pos_x += overlap_depth / 2
        elif group == 'attack:hit':
            my_state = self.state_machine.current

            if my_state == States.PARRYING:
                other.handle_collision('parry:success',self)
                return

            if my_state == States.DEFENSE:
                self.take_damage(2 ,group)
                return

            if my_state == States.HIT:
                return

            self.state_machine.change(States.HIT)
            self.take_damage(15, group)
            self.x_speed = other.last_dir * KNOCKBACK_SPEED
            self.y_speed = KNOCKBACK_SPEED / 2

            self.isGrounded = False
            self.isJumping = False
            self.isBrakingJump = False

        elif group == 'parry:success':
            self.state_machine.change(States.STUN)
            self.stun_timer = self.STUN_DURATION
            self.x_speed = 0
        elif group == 'player:volcano':
            if self.invincible_timer != 0: return
            self.take_damage(50, group)

    def get_attack_bb(self):
        if self.state_machine.current != States.ATTACK:
            return None

        left, bottom, right, top = 0,0,0,0
        if self.name == 'Fighter':
            if self.last_dir > 0:
                left, bottom, right, top = self.pos_x, self.pos_y - 48, self.pos_x + 35, self.pos_y
            else:
                left, bottom, right, top = self.pos_x - 35, self.pos_y - 48, self.pos_x, self.pos_y

        if self.name == 'Samurai':
            if self.last_dir > 0:
                left, bottom, right, top = self.pos_x, self.pos_y - 48, self.pos_x + 60, self.pos_y
            else:
                left, bottom, right, top = self.pos_x - 60, self.pos_y - 48, self.pos_x, self.pos_y

        if self.name == 'Shinobi':
            if self.last_dir > 0:
                left, bottom, right, top = self.pos_x, self.pos_y - 48, self.pos_x + 60, self.pos_y
            else:
                left, bottom, right, top = self.pos_x - 60, self.pos_y - 48, self.pos_x, self.pos_y

        return left, bottom, right, top

    def get_foot_bb(self):
        return self.pos_x - 10, self.pos_y-64, self.pos_x+10, self.pos_y-63

    def get_bb(self):
        if self.state_machine.current == States.DEAD:
            return 0,0,0,0

        return self.pos_x-16, self.pos_y-64, self.pos_x+16, self.pos_y+16

    def draw(self):
        self.animator.draw_current_frame()

        if GameConstants.SHOW_DEBUG_RECT:
            draw_rectangle(*self.get_bb(),0,255,150,1)
            draw_rectangle(*self.get_foot_bb(),255,255,0,1)

            if self.state_machine.current == States.ATTACK:
                attack_bb = self.get_attack_bb()
                if attack_bb:
                    draw_rectangle(*self.get_attack_bb())