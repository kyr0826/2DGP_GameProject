from StateMachine import States

def collide(a_bb,b_bb):
    left_a, bottom_a, right_a, top_a = a_bb
    left_b, bottom_b, right_b, top_b = b_bb

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

collision_pairs= {}
def add_list_collision_pair(group, list_a, list_b):
    if group not in collision_pairs:
        collision_pairs[group] = [[],[]]

    if list_a:
        collision_pairs[group][0] = list_a
    if list_b:
        collision_pairs[group][1] = list_b

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [[],[]]

    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def handle_collisions():
    for group, pairs in collision_pairs.items():
        list_a = pairs[0]
        list_b = pairs[1]

        for a in list_a:
            for b in list_b:
                if a == b: continue
                a_box, b_box = None, None

                if group == 'player:map':
                    a_box = a.get_foot_bb()
                    b_box = b.rect
                elif group == 'player:player' or group == 'player:volcano':
                    a_box = a.get_bb()
                    b_box = b.get_bb()
                elif group == 'attack:hit': # a -> b
                    if a.state_machine.current != States.ATTACK: continue
                    a_box = a.get_attack_bb()
                    b_box = b.get_bb()
                if a_box and b_box and collide(a_box, b_box):
                    if group == 'attack:hit':
                        b.handle_collision('attack:hit', a)
                    else:
                        a.handle_collision(group, b)
