from sportsreference.nba.roster import Player
from sportsreference.nba.schedule import Schedule

class PlayerStats:
    """
    Allows retrieval of a player's career, per season, and per game stats.

    Paramters
    ----------
    id : string
        Player's ID. Of the form 'LLLLLFFNN', where 'LLLLL' is the first
        5 letters of the player's last name, 'FF' is the first 2 letters
        of the player's first name, and 'NN' is the index number of the
        player (usually just 01).
    player : sportsreference.nba.roster.Player
        Player object.
    """
    def __init__(self, id):
        """
        Constructor for PlayerStats class.

        Arguments
        -----------
        id : string
            Player's ID. Of the form 'LLLLLFFNN', where 'LLLLL' is the first
            5 letters of the player's last name, 'FF' is the first 2 letters
            of the player's first name, and 'NN' is the index number of the
            player (usually just 01).
        """
        self.id = id
        self.player = Player(id)


    def career_stats(self):
        """
        Fetches career stats for player.

        Returns
        -------
        dict of stats
        """
        return stats(self.player, self.player.games_played)


    def season_stats(self, year):
        """
        Fetches stats for player from specified season.

        Arguments
        ---------
        year : int
            Second year of season (e.g. 2016 corresponds to the 2015-16 season).

        Returns
        -------
        dict of stats
        """
        year_str = str(year - 1) + '-' + str(year)[-2:]
        return stats(self.player(year_str), self.player(year_str).games_played)


    def game_stats(self, date):
        """
        Fetches stats for player from their game on the specified date.

        Arguments
        ---------
        date : datetime.date
            Date of game.

        Returns
        -------
        dict of stats or None if there was no game for the player on that date.
        """
        if date.month > 7:
            year_str = str(date.year) + '-' + str(date.year + 1)[-2:]
            year = date.year + 1
        else:
            year_str = str(date.year - 1) + '-' + str(date.year)[-2:]
            year = date.year
        team_schedule = Schedule(self.player(year_str).team_abbreviation, year)

        try:
            boxscore = team_schedule(date).boxscore
        except ValueError:
            return None

        for player in boxscore.away_players + boxscore.home_players:
            if player.name == self.player.name:
                return stats(player)


def stats(player, num_games = 1):
    """
    Returns stats for player.

    Arguments
    ---------
    player : sportsreference.nba.player.AbstractPlayer
        Player object.

    num_games : int
        number of games over which to evaluate stats

    Returns
    -------
    dict of stats.
    """
    stats = dict(points = player.points,
                 assists = player.assists,
                 offensive_rebounds = player.offensive_rebounds,
                 defensive_rebounds = player.defensive_rebounds,
                 steals = player.steals,
                 blocks = player.blocks,
                 turnovers = player.turnovers)

    if num_games > 1:
        stats = dict(ppg = player.points / num_games,
                     apg = player.assists / num_games,
                     orpg = player.offensive_rebounds / num_games,
                     drpg = player.defensive_rebounds / num_games,
                     spg = player.steals / num_games,
                     bpg = player.blocks / num_games,
                     tpg = player.turnovers / num_games,
                     **stats)

    return stats

from datetime import date

lbj = PlayerStats('jamesle01')
d = date(2007,1,24)
print(lbj.career_stats())
