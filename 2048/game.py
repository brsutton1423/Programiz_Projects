import random
import copy

class Game:
    def __init__(self):
        self.grid = [[0]*4 for i in range(4)]
        [self.add_random_tile() for i in range(2)]
        self.move_action = {"a":self.move_left,"d":self.move_right,"w":self.move_up,"s":self.move_down}

    def display_grid(self):
        for row in self.grid:
            print(' '.join(str(num) for num in row))

    def add_random_tile(self):
        cell = [random.choice(range(4)) for i in range(2)]
        a = cell[0]
        b = cell[1]
        if self.grid[a][b] == 0:
            self.grid[a][b] = random.choice((2,4))
        else:
            self.add_random_tile()
        return self.grid
    
    def move_left(self):
        for n in self.grid:
            i = self.grid.index(n)
            self.grid[i] = [num for num in self.grid[i] if num != 0]
            j = 0
            while j < len(self.grid[i])-1:
                if self.grid[i][j] == self.grid[i][j+1]:
                    self.grid[i][j] *= 2
                    self.grid[i][j+1] = 0
                    j += 2
                else:
                    j += 1
            self.grid[i] = [num for num in self.grid[i] if num != 0]
            self.grid[i] += [0]*(4 - len(self.grid[i]))
    
    def move_right(self):
        for n in self.grid:
            i = self.grid.index(n)
            self.grid[i].reverse()
            self.grid[i] = [num for num in self.grid[i] if num != 0]
            j = 0
            while j < len(self.grid[i])-1:
                if self.grid[i][j] == self.grid[i][j+1]:
                    self.grid[i][j] *= 2
                    self.grid[i][j+1] = 0
                    j += 2
                else:
                    j += 1
            self.grid[i] = [num for num in self.grid[i] if num != 0]
            self.grid[i] += [0]*(4 - len(self.grid[i]))
            self.grid[i].reverse()
    
    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()  
    
    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()
    
    def transpose(self):
        t_grid = [[0]*4 for num in range(4)]
        i = 0
        j = 0
        while i < len(range(4)) and j < len(range(4)):
            t_grid[i][j] = self.grid[j][i]
            if j < len(range(4))-1:
                j+=1
            else:
                i+=1
                j=0
        self.grid = t_grid.copy()
    
    def is_game_won(self):
        return any([2048 in self.grid[i] for i in range(4)])

    def is_game_over(self):
        full_board = all([all(self.grid[i]) for i in range(4)])
        possible_moves = []
        for move in self.move_action:
            grid_before = copy.deepcopy(self.grid)
            self.move_action[move]()
            if grid_before != self.grid:
                possible_moves.append(False)
                self.grid = copy.deepcopy(grid_before)
            else:
                possible_moves.append(True)
        return all(possible_moves) and full_board
    
    def run(self):
        while True:
            self.display_grid()
            move = input("Enter move (w/a/s/d) or q to quit: ").lower()
            while move not in ("w","a","s","d","q"):
                print("Invalid input!")
                move = input("Enter move (w/a/s/d) or q to quit: ").lower()
            if move == "q":
                print("Thanks for playing!")
                break
            else:
                print(f"You pressed: {move}")
                grid_before = copy.deepcopy(self.grid)
                self.move_action[move]()
                if grid_before != self.grid:
                    self.add_random_tile()
                if self.is_game_won():
                    print("Congratulations! You've reached 2048")
                if self.is_game_over():
                    print("Game over! No moves left")