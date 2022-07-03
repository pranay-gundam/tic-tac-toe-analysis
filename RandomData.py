from Bots import RandBot
from GameInterface import Game
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#import time

timeseries_df = pd.DataFrame(columns = ["Games Played", "Player 1 Wins", "Player 2 Wins", "Draws"])

bot1 = RandBot()
bot2 = RandBot()

p1count = 0
p2count = 0
drawcount = 0

n = 0
timeseries_df.loc[n+1] = [n, p1count, p2count, drawcount]
while (n < 10000):
    maingame = Game()
    while (not maingame.has_won()):
        if (maingame.has_drawn()): break
        #maingame.print_game()
        
        if maingame.current_player == 'Player 1':
            row, col = bot1.playMove(maingame.getBoard())
        else:
            row, col = bot2.playMove(maingame.getBoard())
        maingame.make_move(row, col)
        
    #maingame.print_game()
    if maingame.has_drawn():
        drawcount += 1
    elif maingame.turn == 0:
        p2count += 1
    else:
        p1count += 1
    n += 1
    timeseries_df.loc[n] = [n, p1count, p2count, drawcount]
    if n % 1000 == 0: print(n)


plt.plot(timeseries_df['Games Played'], timeseries_df['Player 1 Wins'], label = "P1 Wins")
plt.plot(timeseries_df['Games Played'], timeseries_df['Player 2 Wins'], label = "P2 Wins")
plt.plot(timeseries_df['Games Played'], timeseries_df['Draws'], label = "Draws")
plt.legend()
plt.show()
    