
class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        
    def get_name(self):
        return input("What is your name?\n> ")
    
    def get_choice(self,Board):
        while True:
            try:
                choice = int(input(f"{self.name} pick a column.\n> "))
                if 1 <= choice <= 7:
                    return choice
            except:
                print('\nYour choice is invalid.')
#
#    
#def main():
#    p1 = Player('x')
#    p1.get_choice(7)
#    p2 = Player('o')
#    p2.get_choice(7)
#    
#if __name__ == "__main__":
#    main()