from at_bat import AtBat, Pitch
from fetcher import load_statcast_csv, build_at_bats
from scorer import player_tor, rank_players

def main():
    print("Welcome to TOR: True Offensive Rating")
    df = load_statcast_csv("statcast_data_2026.csv")

    players = df['player_name'].unique()
    
    all_at_bats = []
    for player in players:
        at_bats = build_at_bats(df, player)
        all_at_bats.extend(at_bats)

    print("\n--- PLAYER RANKINGS ---")
    leaderboard = rank_players(all_at_bats)
    
    for i, (name, score) in enumerate(leaderboard, 1):
        print(f"{i}. {name}: {score:.2f}")

if __name__ == "__main__":
    main()