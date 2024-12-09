import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo

import json



class playerClient(object):
    def __init__(self):
        self.players=players.get_active_players()
        self.player_headshot_base = 'https://cdn.nba.com/headshots/nba/latest/1040x760/{}.png'
        

    def search(self, search_string):
        players_by_name=[]
        for player in self.players:
            if search_string.lower() in player['full_name'].lower():
               
                player.update({'player_headshot':self.player_headshot_base.format(player['id'])})
                players_by_name.append(player)
                
        return players_by_name

    def retrieve_player_by_id(self, player_id,player_name):

        try: 
            player_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_dict()
            regular_seasons_data = [item for item in player_stats["resultSets"] if item["name"] == "SeasonTotalsRegularSeason"][0]
            current_season_data = [item for item in regular_seasons_data['rowSet']][-1]
            easier_json = {
            "player_latest_season": current_season_data[regular_seasons_data['headers'].index('SEASON_ID')],
            "player_id":player_id,
            "player_name":player_name,
            "player_team": current_season_data[regular_seasons_data['headers'].index('TEAM_ABBREVIATION')],
            "player_age": current_season_data[regular_seasons_data['headers'].index('PLAYER_AGE')],
            "player_gp": current_season_data[regular_seasons_data['headers'].index('GP')],
            "player_gs": current_season_data[regular_seasons_data['headers'].index('GS')],
            "player_min": current_season_data[regular_seasons_data['headers'].index('MIN')],
            "player_fgm": current_season_data[regular_seasons_data['headers'].index('FGM')],
            "player_fga": current_season_data[regular_seasons_data['headers'].index('FGA')],
            "player_fgpct": current_season_data[regular_seasons_data['headers'].index('FG_PCT')],
            "player_fg3m": current_season_data[regular_seasons_data['headers'].index('FG3M')],
            "player_fg3a": current_season_data[regular_seasons_data['headers'].index('FG3A')],
            "player_fg3pct": current_season_data[regular_seasons_data['headers'].index('FG3_PCT')],
            "player_ftm": current_season_data[regular_seasons_data['headers'].index('FTM')],
            "player_fta": current_season_data[regular_seasons_data['headers'].index('FTA')],
            "player_ft_pct": current_season_data[regular_seasons_data['headers'].index('FT_PCT')],
            "player_oreb": current_season_data[regular_seasons_data['headers'].index('OREB')],
            "player_dreb": current_season_data[regular_seasons_data['headers'].index('DREB')],
            "player_reb": current_season_data[regular_seasons_data['headers'].index('REB')],
            "player_ast": current_season_data[regular_seasons_data['headers'].index('AST')],
            "player_stl": current_season_data[regular_seasons_data['headers'].index('STL')],
            "player_blk": current_season_data[regular_seasons_data['headers'].index('BLK')],
            "player_tov": current_season_data[regular_seasons_data['headers'].index('TOV')],
            "player_pf": current_season_data[regular_seasons_data['headers'].index('PF')],
            "player_pts": current_season_data[regular_seasons_data['headers'].index('PTS')],
            "player_headshot":str(self.player_headshot_base.format(player_id))
    }   

            return easier_json 
        except Exception as e:
            raise Exception(f"Error retrieving player stats: {str(e)}")  
