import pandas as pd
from at_bat import AtBat, Pitch 
from pybaseball import statcast

def fetch_statcast_api(start_date, end_date):
    df = statcast(start_dt=start_date, end_dt=end_date)
    return df

def load_statcast_csv(filepath):
    df = pd.read_csv(filepath)
    df['player_name'] = df['player_name'].str.strip()
    cols_we_need = [
    'player_name',
    'at_bat_number', 
    'pitch_number',
    'launch_speed',
    'description',
    'events',
    'balls',
    'strikes',
    'game_pk'
    ]
    df = df[cols_we_need]
    return df

def build_at_bats(df, player_name):
    player_df = df[df['player_name'] == player_name]
    at_bats = []
    for (game_id, ab_num), group in player_df.groupby(['game_pk', 'at_bat_number']):
        final_outcome = group['events'].dropna().iloc[-1] if not group['events'].dropna().empty else "unknown"
        current_ab = AtBat(player_name, final_outcome)
        
        # 3. Loop through every pitch in this group
        for _, row in group.iterrows():
            # Create a Pitch object (handling potential NaN for launch_speed)
            p = Pitch(
                pitch_number=row['pitch_number'],
                exit_velo=row['launch_speed'] if pd.notnull(row['launch_speed']) else 0,
                description=row['description'],
                balls=row['balls'],
                strikes=row['strikes']
            )
            current_ab.add_pitch(p)
            
        at_bats.append(current_ab)
        
    return at_bats