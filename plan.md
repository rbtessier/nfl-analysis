# Planning

Overall plan

1. Explore data
2. Create classes and method files to reuse
3. Test using python script file
4. Find a way to template and deploy multiple analysis features on fractodata.com
    1. Player univariate analysis
    2. Player comparison analysis
    3. Swap player comparison
    4. Estimate point gain for swapping player

## Questions

What is the best way to select and compare multiple players?
How does having players who are playing against each other in a given week affect points on avg?
How does playing alongside another star affect points? Does an RB/WR on a winning team always net more points than a go-to RB/WR on a losing or not great team?
What types of opponents and games net the most points for individual positions: ie. I noticed that when a game is a blowout or team has a big lead, seems to be lots of running - makes it harder for QB to score points

## Classes

Eventually I'm going to add classes to help with organization and speed, I at least need

1. Player
1. Fantasy Roster
1. Team

### Player

1. Data:
    1. Name
    1. Position
    1. Team
    1. Pandas Dataframe - selecting the year and the player, it shoudl also reduce the dataset columns to just ones relevant to the player position.
        - add column with fantasy points per game
    1. Dictionary with metadata
1. Methods:
    1. Constructor - Accepts player and year and grabs data for the player and which year of data
        1. Initializes returning # columns and # entries
    1. Fantasy Analysis - A method that generates a set of graphs or summary graph suite that give a good indication of the player performance
    1. Hypothesis test win-loss fantasy gain.
    1. Other specific graphs
    1. Method comparing $n$ players with each other

### Roster

1. Data:
    1. Current Date
    2. offensive starter
    3. bench
    4. defense
    5. kicker (not going to be used initially since current league has no)
1. Methods
    1. Add
    2. Delete player
    3. Send (to bench or to line)

#### Team

1. Data:
1. Methods:
