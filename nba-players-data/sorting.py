from typing import List

from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from pandas import DataFrame


def get_all_nba_players() -> List:
    return players.get_players()


def get_nba_career_stats_by_id(player_id: str) -> DataFrame:
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0]


def get_nba_player_info(player_id: str) -> DataFrame:
    player = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    return player.common_player_info.get_data_frame()


all_players = get_all_nba_players()
count = 0
for player in all_players:
    player_career = get_nba_career_stats_by_id(player["id"])
    player_info = get_nba_player_info(player["id"])
    player_career.insert(1, "HEIGHT", player_info.get("HEIGHT")[0])
    player_career.insert(2, "WEIGHT", player_info.get("WEIGHT")[0])
    print(player_career)
    count += 1
    if count == 7:
        break
