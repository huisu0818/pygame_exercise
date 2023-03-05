import pygame

# ********************************************************************************** #
# 1. 기본 초기화 (필수)

pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 키기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 (게임 이름)
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()

# ********************************************************************************** #
# 2. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)


# ********************************************************************************** #

# 3. 진행 처리
# 3-1) 이벤트 처리 (키보드, 마우스 등)
# 3-2) 게임 캐릭터 위치 정의
# 3-3) 충돌 처리
# 3-4) 화면에 그리기

# ********************************************************************************** #


running = True 
while running:
    dt = clock.tick(144)

    # 3-1) 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3-2) 게임 캐릭터 위치 정의

    # 3-3) 충돌 처리

    # 3-4) 화면에 그리기

    pygame.display.update() # 게임화면을 계속 그려줌

# pygame 종료
pygame.quit()