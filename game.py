from board import Board
from players import Player

class Game:
    def __init__(self):
        self.board = Board
        self.players = []
        self.players.append(Player(piece))
        self.choice = self.get_choice
        self.turn = 0
        
    def play_game(self):
        board.disp_board()
        Player()
        board.place_piece(self.choice)
        if board.check_win():
            print(f"{self.players[turn]} wins!")
            return
        if board.is_full():
            empty_board()
            return
        turn = (turn + 1)% 2
        
def main():
    print("Welcome to Connect 4!")
    while True:
        play_game()
        if input("Play again?(y)es or (n)o.\n> ") == 'y':
            return True
        if input("Play again?(y)es or (n)o.\n> ") == 'n':
            return False
    print("Thanks for playing!")
    
if __name__ == "__main__":
    # test code
    main()