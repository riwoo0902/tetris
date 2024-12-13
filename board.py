
class Board():
    def __init__(self,rows,cols):
        
        self.rows = rows
        self.cols = cols
        self.score = 0
        self.board = []
        self.new_board()
    
        self.bground_grid = []
        self.set_bground_grid()
        
    def set_bground_grid(self): #바둑판 모양 그리기 데이타
        for y in range(self.rows):
            col = []
            for x in range(self.cols):
                if x % 2 == y%2:
                    col.append((35,  35,  35))
                else:
                    col.append(None)
            self.bground_grid.append(col)
            
    def new_board(self):        
        self.board = []
        for y in range(self.rows):
            col = []
            for x in range(self.cols):
                col.append(None)
            self.board.append(col)
            
    def board_clear(self):
        j = 0
        for i in range(self.rows):
            c = 0
            for a in range(self.cols):
                if self.board[i][a] != None:
                    c += 1
            if c == 10:
                del self.board[i]
                self.board.insert(0, [None,None,None,None,None,None,None,None,None,None])
                j += 1
        return j

            
            
            
            
            
            
            
            
            
            
            
            
#0 1 2 3 4 5 6 7 8 9
#                    0
#                    1
#                    2
#                    3
#                    4
#                    5
#                    6
#                    7
#                    8
#                    9
#                    10
#                    11
#                    12
#                    13
#                    14
#                    15
#                    16
#                    17
#                    18
#                    19
#                    20
#                    21
#                    22











