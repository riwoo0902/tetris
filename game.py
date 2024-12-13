import pygame
from pygame.locals import *

from board import *
from stone import *

# pip install pygame

#이벤트 처리함수
def eventProcess():
    global isActive
    for event in pygame.event.get():#이벤트 가져오기
        if event.type == QUIT: #종료버튼?
            isActive = False
        if event.type == pygame.KEYDOWN:#키 눌림?
            if event.key == pygame.K_ESCAPE:#ESC 키?
                isActive = False
                
            if stone.gameover:
                if event.key == pygame.K_RETURN:#재시작
                    init_game()
            else:
                if event.key == pygame.K_w:#한번에 내리기
                    stone.snd_dic['move'].play()
                    stone.insta_drop(1)
                if event.key == pygame.K_a:
                    stone.snd_dic['move'].play()
                    stone.move(-1)
                if event.key == pygame.K_d:
                    stone.snd_dic['move'].play()
                    stone.move(+1)
                if event.key == pygame.K_s:#한칸내리기
                    stone.snd_dic['move'].play()
                    stone.drop(1)
                if event.key == pygame.K_q:#회전하기
                    stone.snd_dic['move'].play()
                    stone.lrotate_stone()
                if event.key == pygame.K_e:#회전하기
                    stone.snd_dic['move'].play()
                    stone.rrotate_stone()
                if event.key == pygame.K_r:#저장
                    stone.snd_dic['move'].play()
                    stone.hold_stone()   
        if event.type == pygame.USEREVENT+1:#사용자 이벤트
            stone.drop(1)
        
def draw_matrix(matrix, off_x,off_y,Thickness):
    global cell_size
    for y, row in enumerate(matrix):
        for x, color in enumerate(row):
            if color is not None:
                pygame.draw.rect(screen,color,pygame.Rect((off_x+x) *cell_size,(off_y+y) *cell_size,cell_size,cell_size),Thickness)
                
def init_game():
    stone.new_stone()
    pygame.time.set_timer(pygame.USEREVENT+1, 400)#1초마다 "USEREVENT+1" 이벤트 발생

def restart_game():
    if stone.gameover == True:
        init_game()
        board.new_board()
        stone.score = 0
        stone.gameover = False
#1.초기화 하기
pygame.init() #pygame 초기화
pygame.display.set_caption("codingnow.co.kr") #타이틀
clock = pygame.time.Clock() #프레임을 처리 하기위해

#2.변수초기화
isActive = True
cell_size = 25
cols = 10
rows = 22
rlim = cell_size*cols
    
#3.스크린 생성하기
SCREEN_WIDTH = cell_size*(cols+7)
SCREEN_HEIGHT = cell_size*rows
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면생성

#4.클래스 생성
board = Board(rows,cols)
stone = Stone(rows,cols,board)

init_game()

while isActive:
    screen.fill((0, 0, 0)) #화면을 흰색으로 채우기
    eventProcess() #이벤트 처리
    
    #게임화면 구분선
    pygame.draw.line(screen,(255, 255, 255),(rlim+1, 0),(rlim+1, SCREEN_HEIGHT-1)) 
    pygame.draw.line(screen,(255, 255, 255),(rlim+1, 130),(SCREEN_WIDTH, 130)) 
    
    #게임화면 바둑판
    draw_matrix(board.bground_grid, 0, 0,0)
    #스톤 그리기
    draw_matrix(stone.stone,stone.stone_x, stone.stone_y, 1)
    draw_matrix(stone.save_stone,cols+1, 1, 1)
    draw_matrix(stone.next_stone,cols+1, 6, 1)
    draw_matrix(stone.next_stone2,cols+1, 9, 1)
    draw_matrix(stone.next_stone3,cols+1, 12, 1)
    #보드 그리기
    draw_matrix(board.board, 0, 0, 1)
    stone.score += board.board_clear()
    print(stone.score)
    restart_game()
    pygame.display.update() #화면 갱신
    clock.tick(10) #초당 30프레임 