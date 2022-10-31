import pandas as pd
import numpy as np

'''
Moved all this code here from the eda notebook as the transformation I needed to do at the beginning was
simply to add a W, L, D column to individual offensive players and ensure the yahoo fantasy points were being calculated for each player.
This is to remember the work I did more than anything else.
'''

def add_win_lose_col(off_stats):
    """In-place addition of a df column identifying whether the players team won or lost"""
    off_stats['player_won'] = off_stats.apply(lambda row: win_lose_draw(row), axis=1)


# probably overcomplicating things
def win_lose_draw(row):
    """outputs whether the row (which corresponds to a player) with a given side won or lost or drew"""
    
    if row['team'] == row['home_team']:
        side = 'home'
    else:
        side = 'vis'

    side_score = side + '_score'
    # ensures that if the row is on one side, the otherside is the opposite team
    otherside_score = 'vis_score' if side == 'home' else 'home_score'

    score_difference = row[side_score] - row[otherside_score]
    if score_difference > 0:
        return "W"
    elif score_difference < 0:
        return "L"
    else:
        return "D"


def add_fantasy_points_off(off_stats, fan_off_points):
    """in-place calculates a new column for input offensive data off_stats which has the total fantasy points earned based on the rules in the input dataset fan_off_points"""

    # take the fantasy offence points dataset and grab the stats which contribute fantasy points
    fan_off_stats_list = fan_off_points.index.values.tolist()

    # create a dataframe with games and their fantasy stats converted to points
    stat_points = pd.DataFrame()
    for stat in fan_off_stats_list:
        points = fan_off_points.loc[stat, :][1]
        stat_points[stat] = points*off_stats[stat]

    # total the points for each game
    temp_df = pd.DataFrame(np.zeros((len(off_stats), 1)))
    temp_df = stat_points.sum(axis=1)
    temp_df.head()

    # create a new column for off_ stats which contains fantasy point totals for each game
    off_stats['yahoo_fan_pts'] = temp_df

off_stats = pd.read_csv("Data/nfl_pass_rush_rec_winlose_yahoo_data.csv")
fan_off_points = pd.read_csv("Data/fan_off_points.csv", index_col= "stat_code")
add_win_lose_col(off_stats)
add_fantasy_points_off(off_stats, fan_off_points)
off_stats.to_csv('Data/nfl_pass_rush_rec_winlose_yahoo_data.csv')