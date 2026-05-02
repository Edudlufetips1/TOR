from at_bat import AtBat
    
def get_player_tor(player_name, plate_appearances):
    pass
    # ONE player → their season data dict
    
def rank_players(all_at_bats):
    # This function asks each AtBat for its score
    # and then sorts them!
    ranked = sorted(all_at_bats, key=lambda ab: ab.calculate_tor(), reverse=True)
    return ranked
