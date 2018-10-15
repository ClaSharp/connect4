class Board:
    def __init__(self,w,h):
        self.height = h
        self.width = w
        self.board = [[' '] * h for i in range(w)]
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
        pass
    
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
    board.place_piece('x', 7)
    board.disp_board()

if __name__ == "__main__":
    # test code
    main()