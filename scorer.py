from at_bat import AtBat

def player_tor(list_of_atbats) -> float:
    # Player's average TOR for all at bats
    scores = [ab.calculate_tor() for ab in list_of_atbats]
    return sum(scores) / len(scores) if scores else 0

def group_by_player(all_at_bats):
    player_map = {}
    for ab in all_at_bats:
        name = ab.player_name
        if name not in player_map:
            player_map[name] = []
        player_map[name].append(ab)
    return player_map

def rank_plate_appearances(all_at_bats):
    return sorted(all_at_bats, key=lambda ab: ab.calculate_tor(), reverse=True)

def rank_players(all_at_bats):
    player_map = group_by_player(all_at_bats)
    player_avg = {}
    for name, atbats in player_map.items():
        player_avg[name] = player_tor(atbats)
    return sorted(player_avg.items(), key=lambda x: x[1], reverse=True)