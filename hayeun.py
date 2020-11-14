import pygame
pygame.init() # 초기화 (반드시 필요)

width = 960 #가로 크기
height = 720 #세로 크기
# 화면 해상도 지정
screen = pygame.display.set_mode((height,width)) 
# 타이틀
pygame.display.set_caption("Shooting Game") 
# 배경화면 설정
background = pygame.image.load("background.png")
# 캐릭터 스프라이트 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 세로크기
character_height = character_size[1] # 캐릭터의 가로크기
character_x_pos = width/2 - character_width / 2
character_y_pos = height

# 이벤트 루프
run = True # 게임이 진행중인가?
while run:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            run =False

    screen.blit(background,(0,0)) # 배경그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    pygame.display.update()# 게임화면을 다시 그리기

pygame.quit() # 게임 종료
