from board import Board
from players import Player

class Game:
    def __init__(self):
        self.Board = board
        self.players = []
        self.players.append(Player(piece))
        self.choice = self.get_choice
        self.turn = 0
        
    def play_game(self):
        Player()
        board.disp_board()
        board.add_piece()
        if board.check_win():
            players[turn].wins()
            return
        turn = (turn + 1)% 2
        if board.is_full():
            draw
            return
        

def main():
    Player()
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