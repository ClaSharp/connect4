
class Player:
    def __init__(self):
        self.name = self.get_name()
        self.piece = self.get_name()
        
    def get_name(self):
        self.name = input("What is your name?\n> ")
    
    def get_choice(self, Board):
        self.piece = input("What shape would you like to use?\n1) '*'\n2) '^'\n> ")
        
def main():
    Player()
    
if __name__ == "__main__":
    main()