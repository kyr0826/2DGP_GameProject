from pico2d import *
from collections import namedtuple
import GameConstants as gc

# 플랫폼 데이터를 저장할 구조체 정의 (사각형, 색상, 타입)
# type ground (통과 불가) one-way (아래에서 위로 통과 가능)
PlatformData = namedtuple('PlatformData', ['rect', 'color', 'type'])

platforms = []


def init_map_pyramid():
    global platforms
    platforms.clear()

    platforms.append(PlatformData((0, 0, 800, 70), (100, 255, 100, 1), 'ground'))
    center = gc.GAME_WINDOW_WIDTH // 2

    width = 700
    left = center - width // 2
    platforms.append(PlatformData((left, 140, left + width, 170), (100, 255, 150, 1), 'one-way'))

    width = 600
    left = center - width // 2
    platforms.append(PlatformData((left, 250, left + width, 280), (100, 255, 200, 1), 'one-way'))

    width = 450
    left = center - width // 2
    platforms.append(PlatformData((left, 360, left + width, 390), (100, 200, 255, 1), 'one-way'))

    width = 300
    left = center - width // 2
    platforms.append(PlatformData((left, 470, left + width, 500), (150, 150, 255, 1), 'one-way'))

    platforms.append(PlatformData((300, 580, 500, 610), (255, 100, 100, 1), 'one-way'))


def init_map_towers():
    global platforms
    platforms.clear()

    W = gc.GAME_WINDOW_WIDTH
    CENTER = W // 2

    # 탑 설정
    TOWER_WIDTH = 200
    MARGIN = 20

    platforms.append(PlatformData((0, 0, W, 50), (100, 255, 100, 1), 'ground'))

    heights = [160, 270, 380, 490, 600]

    for h in heights:
        bottom = h - 30
        top = h

        l_x1 = MARGIN
        l_x2 = MARGIN + TOWER_WIDTH
        platforms.append(PlatformData((l_x1, bottom, l_x2, top), (150, 200, 255, 1), 'one-way'))

        r_x1 = W - MARGIN - TOWER_WIDTH
        r_x2 = W - MARGIN
        platforms.append(PlatformData((r_x1, bottom, r_x2, top), (150, 200, 255, 1), 'one-way'))

    bridge_width = 200
    bridge_left = CENTER - bridge_width // 2
    platforms.append(PlatformData((bridge_left, 350, bridge_left + bridge_width, 380), (255, 255, 100, 1), 'one-way'))


def init_map_islands():
    global platforms
    platforms.clear()

    W = gc.GAME_WINDOW_WIDTH
    CENTER = W // 2
    SIDE_MARGIN = 50

    platforms.append(PlatformData((0, 0, W, 40), (100, 255, 100, 1), 'ground'))

    width = 150
    platforms.append(PlatformData((SIDE_MARGIN, 125, SIDE_MARGIN + width, 155), (100, 255, 150, 1), 'one-way'))
    platforms.append(PlatformData((W - SIDE_MARGIN - width, 125, W - SIDE_MARGIN, 155), (100, 255, 150, 1), 'one-way'))

    width = 200
    left = CENTER - width // 2
    platforms.append(PlatformData((left, 240, left + width, 270), (100, 255, 200, 1), 'one-way'))

    width = 150
    side_gap = 100
    platforms.append(PlatformData((side_gap, 355, side_gap + width, 385), (100, 200, 255, 1), 'one-way'))
    platforms.append(PlatformData((W - side_gap - width, 355, W - side_gap, 385), (100, 200, 255, 1), 'one-way'))

    width = 300
    left = CENTER - width // 2
    platforms.append(PlatformData((left, 470, left + width, 500), (255, 150, 150, 1), 'one-way'))

    width = 100
    platforms.append(PlatformData((SIDE_MARGIN, 585, SIDE_MARGIN + width, 615), (255, 100, 100, 1), 'one-way'))
    platforms.append(PlatformData((W - SIDE_MARGIN - width, 585, W - SIDE_MARGIN, 615), (255, 100, 100, 1), 'one-way'))


def init_map(map_type=1):
    global platforms
    platforms.clear()

    if map_type == 1:
        init_map_pyramid()

    elif map_type == 2:
        init_map_towers()

    elif map_type == 3:
        init_map_islands()


def init_map_old():
    global platforms
    platforms.clear()  # 맵 초기화

    # ground
    ground = PlatformData((0, 0, 800, 30), (100, 255, 100, 1), 'ground')
    platforms.append(ground)

    # floor_l_1 (one-way)
    left, width = 100, 200
    bottom, height = 120, 50
    floor_l_1 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_l_1)

    # floor_r_1 (one-way)
    left, width = 400, 300
    bottom, height = 100, 50
    floor_r_1 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_r_1)

    # floor_l_11 (one-way)
    left, width = 30, 80
    bottom, height = 200, 50
    floor_l_11 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_l_11)

    # floor_r_11 (one-way)
    left, width = 650, 80
    bottom, height = 185, 50
    floor_r_11 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_r_11)

    # floor_l_2 (one-way)
    left, width = 50, 650
    bottom, height = 280, 50
    floor_2 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_2)

    # floor_m_3 (one-way)
    left, width = 180, 400
    bottom, height = 400, 50
    floor_m_3 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_m_3)

    # floor_l_4 (one-way)
    left, width = 100, 160
    bottom, height = 520, 50
    floor_l_4 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_l_4)

    # floor_r_4 (one-way)
    left, width = 500, 160
    bottom, height = 520, 50
    floor_r_4 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_r_4)

    # floor_m_5 (one-way)
    left, width = 180, 400
    bottom, height = 620, 50
    floor_m_5 = PlatformData((left, bottom, left + width, bottom + height), (100, 255, 150, 1), 'one-way')
    platforms.append(floor_m_5)


def get_platforms():
    return platforms


def draw_map():
    for p in platforms:
        draw_rectangle(*p.rect, *p.color, filled=True)
