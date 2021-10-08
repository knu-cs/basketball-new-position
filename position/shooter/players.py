from position.decorator.measurement import measure_time
from position.nba_players_data.sorting import get_all_nba_players
from position.nba_players_data.sorting import get_nba_player_info


# player 10명 중 guard 추출 걸리는 시간: 1.6sec
# player 100명 중 guard 추출 걸리는 시간: 70sec
@measure_time
def filter_guard_position_players():
    players = get_all_nba_players()
    count = 1
    for player in players:
        player_info = get_nba_player_info(player["id"])
        player_info.loc[player_info['POSITION'] == 'Guard']
        count += 1
        if count == 2:
            break


if __name__ == '__main__':
    filter_guard_position_players()