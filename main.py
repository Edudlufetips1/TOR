from at_bat import AtBat, Pitch
from fetcher import load_statcast_csv, build_at_bats, fetch_statcast_api
from scorer import player_tor, rank_players
from pybaseball import statcast
import glob
import pandas as pd 

DATA_SOURCE = "CSV" 

def main():
    print("Welcome to TOR: True Offensive Rating")
    all_files = glob.glob("statcast_data/*.csv")
    if not all_files:
        print("Wait! I couldn't find any CSV files in the 'statcast_data' folder.")
        print("Check the folder name and make sure the files are inside it!")
        return 
    df_list = [load_statcast_csv(f) for f in all_files]    
    df = pd.concat(df_list, ignore_index=True)
    print(f"Total rows in CSV: {len(df)}")

    # DIAGNOSTIC: top 5 players by row count
    print("Top players by pitch count:")
    print(df['player_name'].value_counts().head(5))
    print("Example names from the file:")
    print(df['player_name'].unique()[:10])
    players = df['player_name'].unique()
    
    all_at_bats = []
    for player in players:
        at_bats = build_at_bats(df, player)
        all_at_bats.extend(at_bats)

    print("\n--- PLAYER RANKINGS ---")
    leaderboard = rank_players(all_at_bats)
    
    for i, (name, score) in enumerate(leaderboard[:50], 1):
        print(f"{i}. {name}: {score:.2f}")

if __name__ == "__main__":
    main()