from pico2d import *
from collections import namedtuple
import Global_Variables as gv

# 플랫폼 데이터를 저장할 구조체 정의 (사각형, 색상, 타입)
# type ground (통과 불가) one-way (아래에서 위로 통과 가능)
PlatformData = namedtuple('PlatformData', ['rect', 'color', 'type'])

ingame_bgs = []
platform_imgs = []
platforms = []


def init_map_pyramid():
    global platforms
    platforms.clear()

    platforms.append(PlatformData((0, 0, 800, 50), (100, 255, 100, 1), 'ground'))
    center = gv.GAME_WINDOW_WIDTH // 2

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

    W = gv.GAME_WINDOW_WIDTH
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

    W = gv.GAME_WINDOW_WIDTH
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

    global ingame_bgs, platform_imgs
    if not ingame_bgs:
        for i in range(3):
            ingame_bgs.append(load_image(f'UI/InGame_bg_{i}.png'))
    if not platform_imgs:
        for i in range(3):
            platform_imgs.append(load_image(f'UI/platform_{i}.png'))

    gv.map_idx = map_type - 1

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
    global ingame_bgs, platform_imgs
    w = gv.GAME_WINDOW_WIDTH
    h = gv.GAME_WINDOW_HEIGHT

    selected_bg = ingame_bgs[gv.map_idx]
    selected_platform_img = platform_imgs[gv.map_idx]

    selected_bg.draw(w // 2, h // 2, w, h)

    # ------------------------------------------------------------------
    # [설정값 조정] 이 수치들을 조절하여 자연스러운 타일링을 만드세요.
    # ------------------------------------------------------------------
    IMG_W = selected_platform_img.w  # 616
    IMG_H = selected_platform_img.h  # 189

    # 1. 전체 크기 배율 (0.3 ~ 0.5 추천)
    DRAW_SCALE = 0.4

    # 2. 양쪽 끝(Cap)으로 사용할 원본 이미지 너비
    SRC_MARGIN = 108

    # 3. [핵심] 가운데 반복될 블록 패턴의 원본 너비
    # 이 값을 조절하면 "벽돌이 몇 개 쌓인 느낌인지" 결정됩니다.
    SRC_TILE_WIDTH = 400

    # ------------------------------------------------------------------
    # [자동 계산] 여기서부터는 위 설정값에 따라 자동으로 계산됩니다.
    # ------------------------------------------------------------------
    # 화면에 그려질 실제 사이즈들
    DST_MARGIN = int(SRC_MARGIN * DRAW_SCALE)  # 화면상 캡 너비
    DST_TILE_WIDTH = int(SRC_TILE_WIDTH * DRAW_SCALE)  # 화면상 타일 1개 너비
    DST_HEIGHT = int(IMG_H * DRAW_SCALE)  # 화면상 높이

    for p in platforms:
        # 바닥(ground) 타입은 그리지 않고 건너뜀 (요청사항 반영)
        if p.type == 'ground': continue

        pl, pb, pr, pt = p.rect
        platform_width = pr - pl
        feet_offset = 5
        # 그리기 중심 Y좌표 (Top 기준 정렬)
        cy = pt - (DST_HEIGHT // 2)

        # -----------------------------------------------------
        # Case A: 발판이 충분히 넓을 때 (3-Slice + Tiling 적용)
        # -----------------------------------------------------
        if platform_width > DST_MARGIN * 2:

            # 1. 왼쪽 끝 (Left Cap) 그리기
            # 위치: 왼쪽 끝에서 캡의 절반만큼 오른쪽
            selected_platform_img.clip_draw(
                0, 0, SRC_MARGIN, IMG_H,
                pl + (DST_MARGIN // 2), cy + feet_offset,
                DST_MARGIN, DST_HEIGHT
            )

            # 2. 오른쪽 끝 (Right Cap) 그리기
            # 위치: 오른쪽 끝에서 캡의 절반만큼 왼쪽
            selected_platform_img.clip_draw(
                IMG_W - SRC_MARGIN, 0, SRC_MARGIN, IMG_H,
                pr - (DST_MARGIN // 2), cy + feet_offset,
                DST_MARGIN, DST_HEIGHT
            )

            # 3. 가운데 (Center) - [반복 채우기 로직]

            # 가운데 채워야 할 총 공간의 너비
            fill_width = platform_width - (DST_MARGIN * 2)

            # 시작 x좌표 (왼쪽 캡 바로 다음)
            start_x = pl + DST_MARGIN

            # 현재까지 그린 너비
            current_drawn_w = 0

            # 공간이 남은 동안 계속 타일(블록)을 그립니다.
            while current_drawn_w < fill_width:
                # 이번에 그릴 타일의 너비 결정 (기본은 DST_TILE_WIDTH)
                # 남은 공간이 타일 1개보다 작으면 남은 만큼만 그림 (자투리 처리)
                remaining_w = fill_width - current_drawn_w
                draw_w = min(DST_TILE_WIDTH, remaining_w)

                # 원본에서 가져올 너비 (비율 역계산)
                src_w = int(draw_w / DRAW_SCALE)

                # 그릴 위치 (중심점 기준이므로 반지름만큼 이동)
                draw_x = start_x + current_drawn_w + (draw_w / 2)

                # 타일 그리기 (가운데 소스 이미지의 앞부분을 계속 가져옴)
                # 소스 위치: SRC_MARGIN (왼쪽 캡 끝난 지점) 부터
                selected_platform_img.clip_draw(
                    SRC_MARGIN, 0, src_w, IMG_H,  # 소스
                    draw_x, cy+feet_offset,  # 화면 위치
                    draw_w, DST_HEIGHT  # 화면 크기
                )

                current_drawn_w += draw_w

        else:
            selected_platform_img.draw(
                pl + platform_width // 2, cy,
                platform_width, DST_HEIGHT
            )

        # 디버깅용 (필요시 주석 해제)
        # draw_rectangle(*p.rect, *p.color)
