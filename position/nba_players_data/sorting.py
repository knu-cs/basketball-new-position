from typing import List

from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playerdashboardbyclutch
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


def get_nba_player_clutch_info(player_id: str) -> DataFrame:
    clutch_info = playerdashboardbyclutch.PlayerDashboardByClutch(player_id=player_id)
    return clutch_info.overall_player_dashboard.get_data_frame()
