class Game(object):
    def __init__(self):
        self.board = [ ['-','-','-',] , ['-','-','-',], ['-','-','-']]
        self.turn = 0

    def make_move(self, row, col):
        if not self.board[row][col] == '-' or row > 2 or col > 2 or row < 0 or col < 0: return False
        if self.turn == 0:
            self.board[row][col] = 'X'
        else: 
            self.board[row][col] = 'O'
        self.turn = (self.turn + 1) % 2
        return True

    def has_won(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and not self.board[0][0] == '-': return True
        if self.board[1][0] == self.board[1][1] == self.board[1][2] and not self.board[1][0] == '-': return True
        if self.board[2][0] == self.board[2][1] == self.board[2][2] and not self.board[2][0] == '-': return True 
        if self.board[0][0] == self.board[1][0] == self.board[2][0] and not self.board[0][0] == '-': return True
        if self.board[0][1] == self.board[1][1] == self.board[2][1] and not self.board[0][1] == '-': return True
        if self.board[0][2] == self.board[1][2] == self.board[2][2] and not self.board[0][2] == '-': return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and not self.board[0][0] == '-': return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and not self.board[0][2] == '-': return True
        return False

    def has_drawn(self):
        if self.has_won():
            return False
        for row in self.board:
            for elem in row:
                if elem == '-':
                    return False
        return True

    def print_game(self):
        for row in range(len(self.board)):
            print(self.board[row][0], ' ', self.board[row][1], ' ', self.board[row][2])
        
    def current_player(self):
        if self.turn == 0:
            return 'Player 1'
        return 'Player 2'

    def cur_turn(self):
        return self.turn

    def getBoard(self):
        return self.board

    def get_pastTurn(self):
        return (self.turn + 1) % 2
    
    def get_moves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '-':
                    moves += [(row,col)]
        return moves

    def revert_move(self,row,col):
        if row > 2 or col > 2 or row < 0 or col < 0: return False
        self.board[row][col] = '-'
        self.turn = (self.turn + 1) % 2
        return True


'''
while (True):
    maingame = Game()
    while (not maingame.has_won()):
        if (maingame.has_drawn()): break
        maingame.print_game()
        row = int(input(maingame.current_player() + "'s move. Enter row ")) - 1
        col = int(input(maingame.current_player() + "'s move. Enter col ")) - 1
        while not maingame.make_move(row, col):
            print("That was an invalid move, please try again")
            row = int(input(maingame.current_player() + "'s move. Enter row ")) - 1
            col = int(input(maingame.current_player() + "'s move. Enter col ")) - 1
    maingame.print_game()
    if maingame.has_drawn():
        print("Game has been drawn.")
    elif maingame.turn == 0:
        print("Congrat's Player 2!")
    else:
        print("Congrat's Player 1!")
    answer = input("Do you want to play again: (Y/N)")
    if answer == "N":
        break
'''