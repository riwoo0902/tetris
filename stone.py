import pygame
from random import randrange as rand
from board import *
class Stone():
    shapes = [    
        
        [[(255, 85,  85), (255, 85,  85), (255, 85,  85)],
         [None,(255, 85,  85),None]],

        [[None, (100, 200, 115), (100, 200, 115)],
        [(100, 200, 115), (100, 200, 115), None]],

        [[(120, 108, 245), (120, 108, 245), None],
        [None, (120, 108, 245), (120, 108, 245)]],

        [[(255, 140, 50), None, None],
        [(255, 140, 50), (255, 140, 50), (255, 140, 50)]],

        [[None, None, (50,  120, 52)],
        [(50,  120, 52), (50,  120, 52), (50,  120, 52)]],

        [[(146, 202, 73), (146, 202, 73), (146, 202, 73), (146, 202, 73)]],

        [[(150, 161, 218), (150, 161, 218)],
        [(150, 161, 218), (150, 161, 218)]]
        
        
    ]

    def __init__(self,  rows,cols,board):
        self.rows = rows
        self.cols = cols
        self.board = board
        
        self.level = 1            
        self.score = 0
        self.lines = 0
        
        self.gameover = False
        self.stone_x = 0
        self.stone_y = 0
        self.stone = []
        self.save_stone = [[(146, 202, 73), (146, 202, 73), (146, 202, 73), (146, 202, 73)]]
        self.next_stone = self.shapes[rand(len(self.shapes))]
        self.next_stone2 = self.shapes[rand(len(self.shapes))]
        self.next_stone3 = self.shapes[rand(len(self.shapes))]
        self.snd_dic = {
            'move':pygame.mixer.Sound('./sound/move.wav'),
            'score':pygame.mixer.Sound('./sound/score.wav'),
            'game_over':pygame.mixer.Sound('./sound/game_over.wav'),
        }
            
    def new_stone(self):        
        self.stone = self.next_stone[:]
        self.next_stone = self.next_stone2[:]
        self.next_stone2 = self.next_stone3[:]
        self.next_stone3 = self.shapes[rand(len(self.shapes))]
        self.stone_x = int(self.cols / 2 - len(self.stone[0])/2)
        self.stone_y = 0
        
        if self.check_collision():
            if self.gameover== False:
                self.snd_dic['game_over'].play()
                
            self.gameover = True
    
    def hold_stone(self):
        w = self.stone
        self.stone = self.save_stone
        self.save_stone = w
        self.stone_x = int(self.cols / 2 - len(self.stone[0])/2)
        self.stone_y = 0
        
        
        
    
        
        pass
    
    def check_collision(self):
        for cy, row in enumerate(self.stone):
            for cx, cell in enumerate(row):
                try:
                    if cell and self.board.board[cy + self.stone_y][cx + self.stone_x]:
                        return True
                except IndexError:
                    return True
        return False    

    def lrotate_clockwise(self):
        result = []
        for x in range(len(self.stone[0]) - 1, -1, -1):
            col = []
            for y in range(len(self.stone)):
                col.append(self.stone[y][x])
                print(self.stone[y][x])
            result.append(col)        
        return result

    def lrotate_stone(self):
        stone_sto = self.stone
        new_stone = self.lrotate_clockwise()
        self.stone = new_stone
        if self.check_collision():
            self.stone = stone_sto
    
    def rrotate_clockwise(self):
        result = []
        for x in range(len(self.stone[0])):
            col = []
            for y in range(len(self.stone)-1 ,-1 ,-1):
                col.append(self.stone[y][x])
                print(self.stone[y][x])
            result.append(col)        
        return result
    
    def rrotate_stone(self):
        stone_sto = self.stone
        new_stone = self.rrotate_clockwise()
        self.stone = new_stone
        if self.check_collision():
            self.stone = stone_sto
    
    
    
    
    def move(self, delta_x):
        new_x = self.stone_x + delta_x
        if new_x < 0:
            new_x = 0
        if new_x > self.cols - len(self.stone[0]):
            new_x = self.cols - len(self.stone[0])
        if not self.check_collision():
            self.stone_x = new_x
            if self.check_collision():
                self.stone_x -= delta_x
    def drop(self,delta_y):
        new_y = self.stone_y + delta_y
        if new_y > self.rows - len(self.stone):
            new_y = self.rows - len(self.stone)
            self.draw_board()
        else:
            if not self.check_collision():
                self.stone_y = new_y
                if self.check_collision():
                    self.stone_y -= 1
                    self.draw_board()
            else:
                self.stone_y -= 1
                self.draw_board()

    def insta_drop(self,delta_y):
        while True:
            new_y = self.stone_y + delta_y
            if new_y > self.rows - len(self.stone):
                new_y = self.rows - len(self.stone)
                self.draw_board()
                break
            else:
                if not self.check_collision():
                    self.stone_y = new_y
                    if self.check_collision():
                        self.stone_y -= 1
                        self.draw_board()
                        break
                    
                else:
                    self.stone_y -= 1
                    self.draw_board()
                    break

    def draw_board(self):
        for cy, row in enumerate(self.stone):
            for cx, cell in enumerate(row):
                if cell != None:
                    self.board.board[cy + self.stone_y][cx + self.stone_x] = cell
        self.new_stone()
        
    
