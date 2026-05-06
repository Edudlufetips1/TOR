from pybaseball import statcast, playerid_reverse_lookup
import pandas as pd
from datetime import date
import glob


def add_batter_names(df):
    batter_ids = df['batter'].unique().tolist()
    batter_info = playerid_reverse_lookup(batter_ids, key_type='mlbam')
    batter_info['batter_name'] = batter_info['name_last'] + ', ' + batter_info['name_first']
    batter_info = batter_info.rename(columns={'key_mlbam': 'batter'})
    return df.merge(batter_info[['batter', 'batter_name']], on='batter', how='left')


# ── One-time fix: add batter names to existing CSVs ──────────────────────────
# Run this if CSVs are missing batter_name column, then comment back out
# for filepath in glob.glob('statcast_data/*.csv'):
#     print(f"Processing {filepath}...")
#     df = pd.read_csv(filepath)
#     df = add_batter_names(df)
#     df.to_csv(filepath, index=False)
#     print(f"Done with {filepath}!")


# ── Update current season (run periodically) ──────────────────────────────────
print("Updating 2025 season...")
df_2025 = statcast(start_dt='2025-03-27', end_dt=str(date.today()))
df_2025 = add_batter_names(df_2025)
df_2025.to_csv('statcast_data/2025_to_date.csv', index=False)
print("Done!")


# ── Template for future seasons ───────────────────────────────────────────────
# print("Downloading 20XX full season...")
# df_20XX = statcast(start_dt='20XX-03-XX', end_dt='20XX-11-01')
# df_20XX = add_batter_names(df_20XX)
# df_20XX.to_csv('statcast_data/20XX_full.csv', index=False)
# print("20XX done!")