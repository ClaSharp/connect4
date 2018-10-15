class Board:
    def __init__(self,w,h):
        self.h = h
        self.w = w
        self.board = [[' '] * h for i in range(w)]
        self.border = [['--'] * w]
        self.num = [[' '] * w]
        
                
    def place_piece(self, piece, column):
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
    board = Board(3,3)
    board.disp_board()

if __name__ == "__main__":
    # test code
    main()