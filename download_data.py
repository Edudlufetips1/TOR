from pybaseball import statcast, playerid_reverse_lookup
import pandas as pd
from datetime import date
import glob
import os

# ── Ensure the directory exists so the script doesn't crash ──
os.makedirs('statcast_data', exist_ok=True)

def add_batter_names(df):
    if df.empty:
        return df
    batter_ids = df['batter'].unique().tolist()
    batter_info = playerid_reverse_lookup(batter_ids, key_type='mlbam')
    # Combine names into a single readable column
    batter_info['batter_name'] = batter_info['name_last'] + ', ' + batter_info['name_first']
    batter_info = batter_info.rename(columns={'key_mlbam': 'batter'})
    return df.merge(batter_info[['batter', 'batter_name']], on='batter', how='left')

# ── HISTORICAL DATA ──────────────────────────────────────────
# Use if there is a need to re-download full past seasons

# print("Downloading 2023 full season...")
# df_2023 = statcast(start_dt='2023-03-30', end_dt='2023-11-01')
# df_2023 = add_batter_names(df_2023)
# df_2023.to_csv('statcast_data/2023_full.csv', index=False)

# print("Downloading 2024 full season...")
# df_2024 = statcast(start_dt='2024-03-20', end_dt='2024-11-01')
# df_2024 = add_batter_names(df_2024)
# df_2024.to_csv('statcast_data/2024_full.csv', index=False)

# print("Downloading 2025 full season...")
# df_2025 = statcast(start_dt='2025-03-27', end_dt='2025-11-01')
# df_2025 = add_batter_names(df_2025)
# df_2025.to_csv('statcast_data/2025_full.csv', index=False)


# ── ACTIVE UPDATE: 2026 SEASON (Run Periodically) ───────────────────────────
print(f"Updating 2026 season data as of {date.today()}...")

# Opening Night 2026 was March 25th
df_2026 = statcast(start_dt='2026-03-25', end_dt=str(date.today()))
df_2026 = add_batter_names(df_2026)

output_path = 'statcast_data/2026_to_date.csv'
df_2026.to_csv(output_path, index=False)

print(f"Done! 2026 data saved to {output_path}")
print(f"Total pitches processed for 2026: {len(df_2026)}")