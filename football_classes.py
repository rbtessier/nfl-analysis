import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fb_data_transformations import add_fantasy_points_off, add_win_lose_col, win_lose_draw


class player():
    
    def __init__(self, input_player):

        #reads the 19, 20, 21 season data and the yahoo points for my current league
        self.data = pd.read_csv("Data/nfl_pass_rush_rec_winlose_yahoo_data.csv")
        self.off_points = pd.read_csv("fan_off_points.csv", index_col="stat_code")
        
        #converts the game_date column to datetime to simplify things
        self.data['game_date'] = pd.to_datetime(self.data['game_date'])
        
        #selects the player passed as input_player
        player = self.data[self.data['player'] == input_player]

    def hist(player):
        sns.displot(data=player.data, x='yahoo_fan_pts', kind='hist')
        plt.show()

#class roster():

#    def __init__(self, off_starters, bench):
#        for player in off_starters:
            

