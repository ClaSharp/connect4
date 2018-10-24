from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board(7,6)
        self.players = []
        self.turn = 0
        
    def play_game(self):
        self.players.append(Player('x'))
        self.players.append(Player('o'))
        while True:
            self.board.disp_board()
            choice = self.players[self.turn].get_choice(self.board)
            self.board.add_piece(choice)  # add_piece has 2 parameters
            if self.board.check_win():
                print(f"{self.players[self.turn]} wins!")
                return
            if self.board.is_full():
                self.board.empty_board()
                return
            self.turn = (self.turn + 1)% 2
        
def main():
    print("Welcome to Connect 4!")
    game = Game()
    while True:
        game.play_game()
        if input("Play again?(y)es or (n)o.\n> ") == 'y':
            return True
        if input("Play again?(y)es or (n)o.\n> ") == 'n':
            return False
    print("Thanks for playing!")
    
if __name__ == "__main__":
    # test code
    main()