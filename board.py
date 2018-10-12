class Board:
    def __init__(self,h,w):
        self.h = h
        self.w = w
        self.board = [[' '] * h for i in range(w)]
        self.border = [['--'] * w]
        self.num = [[' '] * w]
        
        
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
                
        
    def place_piece(self, piece, column):
        pass
    
    def empty_board(self):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = ' '
                
    
def main():
    board = Board(3,3)

if __name__ == "__main__":
    # test code
    main()