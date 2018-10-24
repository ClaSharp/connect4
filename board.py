class Board:
    def __init__(self,w,h):
        self.height = h
        self.width = w
        self.board = [[' '] * w for i in range(h)]
        self.border = [['--'] * w]
        self.num = [[' '] * w]
           
    def add_piece(self, column, piece):
        '''Adds a piece to a chosen column and returns errors
           for an invalid column and for when it is full
        '''
        if column > self.width or column == 0: #what about negative columns
            raise ValueError('Invalid Column')
        
        for row in range(self.height - 1, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = piece
                break
        else:
            raise ValueError('Column Full')
    
    def check_win(self):
        '''Checks for a 4 in a row for the horizontal line,
           vertical line, and diagonals: major and minor.
           Returns a true or false
        '''
        #Horizontal check
        for i in range(self.height):
            for j in range(self.width - 4) # missing last column:
                if self.board[i][j] != ' ':
#                   ls = [self.board[i][j], self.board[i][j + 1], self.board[i][j + 2], self.board[i][j + 3]]
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
            for j in range(self.width - 4) # missing last column:
                if self.board[i][j] != ' ':
#                    mds = [self.board[i][j], self.board[i + 1][j + 1], self.board[i + 2][j + 2], self.board[i + 3][j + 3]]
#                    for c in range(len(mds)): 
                    if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                        return True
        #Minor Diagonal check
        for i in range(3, self.height):
            for j in range(self.width - 4) # missing last column:
                if self.board[i][j] != ' ':
                    if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3]:
                        return True
        return False
    
    
    def empty_board(self):
        '''Empties the board completely to empty strings
           returns nothing
        '''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = ' '
                
    def disp_board(self):
        '''Prints the current board
        '''
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
        '''Checks if the board is full
           Returns True if true and false if it is not full
        '''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != ' ':
                    return True
        return False
    
def main():
    new_board = Board(7,6)
    new_board.add_piece(4,'x')
    new_board.add_piece(2,'o')
    new_board.add_piece(5,'x')
    new_board.add_piece(3,'o')
    new_board.add_piece(3,'o')
    new_board.add_piece(6,'x')
    new_board.add_piece(7,'x')
    new_board.add_piece(4,'o')
    new_board.add_piece(4,'o')
    new_board.add_piece(4,'x')
    new_board.disp_board()
    print(new_board.check_win())

if __name__ == "__main__":
    # test code
    main()
    