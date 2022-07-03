import pandas as pd
import numpy as np
from GameInterface import Game

class NaryTree(object):
    def __init__(self, info, playerNum):
        self.info = info 
        self.childs = []
        self.playerNum = playerNum

class RandBot(object):
    def __init__(self, pnum):
        self.playerNum = pnum

    def playMove(self, board):
        randnum = np.random.randint(9)
        row = randnum // 3
        col = randnum % 3

        while not board.getBoard()[row][col] == '-':
            randnum = np.random.randint(9)
            row = randnum // 3
            col = randnum % 3
        
        return row,col

def boardEval(game, pnum):
    pass

def moveEval(game, pnum, data):
    board = game.getBoard()
    if board in data: return data[board]

    if game.has_won():
        if pnum == game.get_pastTurn(): return None 




class MLBot1(object):
    def __init__(self, pnum, forward):
        self.foresight = forward
        self.playerNum = pnum
        
    def boardEval(self, board, pnum, foresight):
        if board.has_won() and pnum == board.cur_turn():
            return 1
        elif board.has_won():
            return -1
        elif board.has_drawn():
            return 0
        elif pnum == board.cur_turn():
            moves = board.get_moves()
            totalPos = len(moves)
            totalValue = 0
            for move in moves:
                # to debug u must make the making move mechanism different by making a new game object each
                # time you make a move or can make a function to revert a move
                board.make_move(move[0], move[1])
                totalValue += self.boardEval(board, pnum, foresight - 1)
                board.revert_move(move[0], move[1])
            return totalValue / totalPos
        elif pnum != board.cur_turn():
            moves = board.get_moves()
            for move in moves:
                board.make_move(move[0], move[1])
                placer = self.boardEval(board, pnum, foresight)
                board.revert_move(move[0], move[1])
                return placer

    def playMove(self, game):
        moves = game.get_moves()
        maxRow = 0
        maxCol = 0
        maxVal = None
        
        for move in moves:
            game.make_move(move[0], move[1])
            curVal = self.boardEval(game, (self.playerNum + 1) % 2, self.foresight)
            game.revert_move(move[0], move[1])
            if maxVal == None or curVal > maxVal:
                maxVal = curVal
                maxRow = move[0]
                maxCol = move[1]
            
        return maxRow, maxCol, maxVal

