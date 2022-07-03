from Bots import RandBot, MLBot1
from GameInterface import Game

bot1 = MLBot1(0,15)
bot2 = RandBot(1)


while (True):
    maingame = Game()
    while (not maingame.has_won()):
        if (maingame.has_drawn()): break
        maingame.print_game()
        print("-----------------------")
        if maingame.current_player() == 'Player 1':
            row, col, maxVal = bot1.playMove(maingame)
            print("p1", maxVal)
        else:
            row, col = bot2.playMove(maingame)
            print("p2")
        maingame.make_move(row, col)
        
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