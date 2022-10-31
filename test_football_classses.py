import unittest
from football_classes import player
#from football_classes import roster
#from football_classes import team

print("Please enter a player you wish to analyze:")
player_input = input()

# should instantiate an instance of the player class corresponding to the player input
current_player = player(player_input)
print(f"{player_input} loaded")
current_player.hist()
