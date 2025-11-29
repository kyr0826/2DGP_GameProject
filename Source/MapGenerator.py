from pico2d import *
from collections import namedtuple

# 플랫폼 데이터를 저장할 구조체 정의 (사각형, 색상, 타입)
# type ground (통과 불가) one-way (아래에서 위로 통과 가능)
PlatformData = namedtuple('PlatformData', ['rect', 'color', 'type'])

platforms = []

def init_map_coliseum():
    pass

def init_map_double_decker():
    pass

def init_map_canyon():
    pass

def init_map_pyramid():
    pass

def init_map_towers():
    pass

def init_map_islands():
    pass

def init_map(map_type=1):
    global platforms
    platforms.clear()

    if map_type == 1:
        init_map_coliseum()

    elif map_type == 2:
        init_map_double_decker()

    elif map_type == 3:
        init_map_canyon()

    elif map_type == 4:
        init_map_pyramid()

    elif map_type == 5:
        init_map_towers()

    elif map_type == 6:
        init_map_islands()

def init_map_old():
    global platforms
    platforms.clear() # 맵 초기화

    # ground
    ground = PlatformData((0, 0, 800, 30), (100, 255, 100, 1), 'ground')
    platforms.append(ground)

    # floor_l_1 (one-way)
    left, width = 100, 200
    bottom, height = 120, 50
    floor_l_1 = PlatformData((left, bottom, left+width, bottom+height), (100,255,150,1), 'one-way')
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