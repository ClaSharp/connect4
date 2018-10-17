class Board:
    def __init__(self,w,h):
        self.height = h
        self.width = w
        self.board = [[' '] * w for i in range(h)]
        self.border = [['--'] * w]
        self.num = [[' '] * w]
        
                
    def place_piece(self, piece, column):
        for row in range(self.height - 1, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = piece
                break
        else:
            raise ValueError('Invalid input')
    
    def check_win(self):
        for i in range(self.height):
            for j in range(self.width - 4):
                if self.board[i][j] != ' ':
                    ls = [self.board[i][j], self.board[i][j + 1], self.board[i][j + 2], self.board[i][j + 3]]
                    for l in range(len(ls)):
                        if ls[l] == ls[l + 1] and ls[l] == ls[l + 2] and ls[l] == ls[l + 3]:
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
    
def main():
    board = Board(7,6)
    board.disp_board()
    board.place_piece('x', 1)
    board.place_piece('x', 2)
    board.place_piece('x', 3)
    board.place_piece('x', 5)
    board.disp_board()
    print(board.check_win())

if __name__ == "__main__":
    # test code
    main()