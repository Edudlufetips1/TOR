from at_bat import AtBat

def player_tor(player_name, list_of_atbats) -> float:
    # Player's average TOR for all at bats
    scores = [calculate_tor_for_atbat(ab) for ab in list_of_atbats]
    return sum(scores) / len(scores) if scores else 0
    
def rank_players(all_at_bats):
    # This function asks each AtBat for its score
    # and then sorts them!
    ranked = sorted(all_at_bats, key=lambda ab: ab.calculate_tor(), reverse=True)
    return ranked
