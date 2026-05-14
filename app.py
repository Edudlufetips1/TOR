import streamlit as st
import pandas as pd
import glob

from fetcher import load_statcast_csv, build_at_bats
from scorer import rank_players

st.title("TOR: True Offensive Rating")
st.write("Pitch-level offensive analytics powered by Statcast data.")

# Load all CSVs from statcast_data folder
all_files = glob.glob("statcast_data/*.csv")
df_list = [load_statcast_csv(f) for f in all_files]
df = pd.concat(df_list, ignore_index=True)

# Build at-bats for every player
players = df['batter_name'].unique()
all_at_bats = []
for player in players:
    all_at_bats.extend(build_at_bats(df, player))

# Rank players and display
leaderboard = rank_players(all_at_bats)
df_out = pd.DataFrame(leaderboard, columns=["Player", "TOR"])
df_out.index = df_out.index + 1  # start rank at 1
df_out["TOR"] = df_out["TOR"].round(2)

st.subheader("Player Rankings")
st.dataframe(df_out, use_container_width=True)