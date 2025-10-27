print('Welcome to Tic-Tac-Toe!')
WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
print("Winning lines ready!")
# -------------------------------------------------------------------
class Board:
    def __init__(self):
        self.cells = [" "]*9
    def display(self):
        b = self.cells
        print(f' {b[0]} | {b[1]} | {b[2]} \n---+---+---\n {b[3]} | {b[4]} | {b[5]} \n---+---+---\n {b[6]} | {b[7]} | {b[8]} ')
    def place(self,position,mark):
        if not 1 <= position <= 9:
            raise ValueError("Position must be between 1 and 9")
        i = position - 1
        if self.cells[i] != " ":
            return False
        self.cells[i] = mark
        return True
    def check_winner(self,mark:str) -> bool:
        return any(all(self.cells[i] == mark for i in line) for line in WIN_LINES)
    def check_draw(self) -> bool:
        return all(c != " " for c in self.cells)
#--------------------------------------------------------------------
class Player:
    def __init__(self,mark:str):
        self.mark = mark
        self.name = input(f"Player selecting {mark}, enter your name: ").strip() or f"Player {mark}"
    def ask_replay() -> bool:
        while True:
            replay = input("Play again? (y/n): ").strip().lower()
            if replay in ("y","n"):
                return replay == "y"
            print("Please enter 'y' or 'n'.")
#--------------------------------------------------------------------
class Game:
    def __init__(self):
        self.board = Board()
        self.p1 = Player("X")
        self.p2 = Player("O")
        self.current = self.p1
    def _ask_position(self):
        name = self.current.name
        mark = self.current.mark
        position = int(input(f"{name} ({mark}), choose a position (1-9):"))
        while not (1 <= position <= 9):
            raise ValueError("Please enter a number from 1 to 9")
            position = int(input())
        return position
    def play(self):
        self.board = Board()
        self.current = self.p1
        while True:
            self.board.display()
            pos = self._ask_position()
            if not self.board.place(pos,self.current.mark):
                print("That position is already taken.")
                continue

            if self.board.check_winner(self.current.mark):
                self.board.display()
                print(f"{self.current.name} ({self.current.mark}) wins! 🏆")
                break
            if self.board.check_draw():
                self.board.display()
                print("It's a draw! 🤝")
                break
            self.current = self.p2 if self.current == self.p1 else self.p1
    def play_many(self):
        while True:
            self.play()
            if not Player.ask_replay():
                print("Thanks for playing Tic-Tac-Toe! 👋")
                break
Game().play_many()