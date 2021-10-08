from typing import List

from pandas import DataFrame

from position.decorator.measurement import measure_time
from position.nba_players_data.sorting import get_active_nba_players
from position.nba_players_data.sorting import get_nba_career_stats_by_id
from position.nba_players_data.sorting import get_nba_player_info


# player 10명 중 guard 추출 걸리는 시간: 1.6sec, 2.53sec
# player 100명 중 guard 추출 걸리는 시간: 70sec
# TODO: player info 가져오는 부분을 Thread 사용하기
@measure_time
def filter_guard_position_players() -> List[DataFrame]:
    players_list = []
    players = get_active_nba_players()
    count = 1
    for player in players:
        player_info = get_nba_player_info(player["id"])
        guard_player = player_info.loc[player_info["POSITION"] == "Guard"]
        if guard_player.empty:
            count += 1
        else:
            players_list.append(player_info)
        count += 1
        if count == 20:
            break
    return players_list


@measure_time
def add_nba_career_stats(guard_players: List[DataFrame]) -> List[DataFrame]:
    players_list = []
    for guard_player in guard_players:
        guard_player_stats = get_nba_career_stats_by_id(guard_player["PERSON_ID"])
        guard_player_stats.insert(0, "FULL_NAME", guard_player.get("DISPLAY_FIRST_LAST")[0])
        guard_player_stats.insert(1, "HEIGHT", guard_player.get("HEIGHT")[0])
        guard_player_stats.insert(2, "WEIGHT", guard_player.get("WEIGHT")[0])
        players_list.append(guard_player_stats)
    return players_list


if __name__ == "__main__":
    a = filter_guard_position_players()
    print(len(a))
    career = add_nba_career_stats(a)
    print(len(career))
