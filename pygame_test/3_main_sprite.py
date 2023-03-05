import pygame


pygame.init() # 초기화 (필수)


# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 키기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Huisu Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/pc/Desktop/code_manager(DeskTop)/개인 프로젝트/pygame_exercise/pygame_test/background.png")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("C:/Users/pc/Desktop/code_manager(DeskTop)/개인 프로젝트/pygame_exercise/pygame_test/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
chacacter_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로 위치)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로 위치)

# 이벤트 루프 
running = True # 게임이 진행여부
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생 여부
            running = False

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (chacacter_x_pos, character_y_pos))
    pygame.display.update() # 게임화면을 계속 그려줌

# pygame 종료
pygame.quit()