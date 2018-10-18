class Board:
    def __init__(self,w,h):
        self.height = h
        self.width = w
        self.board = [[' '] * w for i in range(h)]
        self.border = [['--'] * w]
        self.num = [[' '] * w]
        
                
    def add_piece(self, column, piece):
        for row in range(self.height - 1, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = piece
                break
        else:
            raise ValueError('Invalid input')
    
    def check_win(self):
        #Horizontal check
        for i in range(self.height):
            for j in range(self.width - 4):
                if self.board[i][j] != ' ':
                    ls = [self.board[i][j], self.board[i][j + 1], self.board[i][j + 2], self.board[i][j + 3]]
                    if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                        return True
        #Vertical check
        for i in range(self.height - 3):
            for j in range(self.width):
                if self.board[i][j] != ' ':
 #                   vs = [self.board[i][j], self.board[i + 1][j], self.board[i + 2][j], self.board[i + 3][j]]
                    if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j]:
                        return True
        #Major Diagonal check
        for i in range(self.height - 3):
            for j in range(self.width - 4):
                if self.board[i][j] != ' ':
#                    mds = [self.board[i][j], self.board[i + 1][j + 1], self.board[i + 2][j + 2], self.board[i + 3][j + 3]]
#                    for c in range(len(mds)): 
                    if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                        return True
        return False
    
    
    def empty_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = ' '
                
    def disp_board(self):
        for row in self.border:
            for element in row:
                print(element,end='')
            print()
        
        for row in self.board:
            for element in row:
                print(element,end=' ')
            print()
        
        for row in self.border:
            for element in row:
                print(element,end='')
            print()
            
        for i in range(len(self.num)):
            for j in range(len(self.num[i])):
                self.num[i][j] = (j + 1)
                
        for row in self.num:
            for element in row:
                print(element,end=' ')
            print()
        
    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != ' ':
                    return True
        return False
    
def main():
#    board = Board(7,6)
#    board.place_piece('y', 2)
#    board.place_piece('x', 2)
#    board.place_piece('x', 3)
#    board.place_piece('y', 2)
#    board.place_piece('x', 4)
#    board.place_piece('x', 7)
#    board.place_piece('x', 4)
#    board.place_piece('x', 5)
#    board.place_piece('x', 3)
#    board.place_piece('x', 3)
#    board.place_piece('y', 2)
#    board.place_piece('y', 2)
#    board.place_piece('y', 3)
#    board.place_piece('y', 4)
#    board.place_piece('y', 5)
#    board.disp_board()
#    print(board.check_win())
    new_board = Board(7,6)
    for i in range(7):
         for j in range(6):
             new_board.add_piece(i+1,'x')

if __name__ == "__main__":
    # test code
    main()
    