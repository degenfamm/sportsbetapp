# Combine the processed pick injection script into the model project as a single module

inject_picks_script = """
import pandas as pd

def inject_daily_picks():
    today = "2025-04-22"

    nba_picks = pd.DataFrame([
        {
            'sport': 'basketball_nba',
            'game_id': 'nba1',
            'commence_time': f'{today}T17:00:00Z',
            'home_team': 'Oklahoma City Thunder',
            'away_team': 'Memphis Grizzlies',
            'bookmaker': 'DraftKings',
            'team': 'Thunder',
            'price': -110,
            'injury_flag': 0
        },
        {
            'sport': 'basketball_nba',
            'game_id': 'nba2',
            'commence_time': f'{today}T19:30:00Z',
            'home_team': 'Los Angeles Lakers',
            'away_team': 'Minnesota Timberwolves',
            'bookmaker': 'FanDuel',
            'team': 'Timberwolves',
            'price': +105,
            'injury_flag': 0
        },
        {
            'sport': 'basketball_nba',
            'game_id': 'nba3',
            'commence_time': f'{today}T20:00:00Z',
            'home_team': 'Indiana Pacers',
            'away_team': 'Milwaukee Bucks',
            'bookmaker': 'Caesars',
            'team': 'Pacers',
            'price': -120,
            'injury_flag': 1
        }
    ])

    mlb_picks = pd.DataFrame([
        {
            'sport': 'baseball_mlb',
            'game_id': 'mlb1',
            'commence_time': f'{today}T16:10:00Z',
            'home_team': 'Kansas City Royals',
            'away_team': 'Colorado Rockies',
            'bookmaker': 'DraftKings',
            'team': 'Bobby Witt Jr. over 1.5 total bases',
            'price': -125,
            'injury_flag': 0
        },
        {
            'sport': 'baseball_mlb',
            'game_id': 'mlb2',
            'commence_time': f'{today}T17:10:00Z',
            'home_team': 'Minnesota Twins',
            'away_team': 'Chicago White Sox',
            'bookmaker': 'BetMGM',
            'team': 'Twins -1.5',
            'price': -114,
            'injury_flag': 0
        },
        {
            'sport': 'baseball_mlb',
            'game_id': 'mlb3',
            'commence_time': f'{today}T18:10:00Z',
            'home_team': 'Toronto Blue Jays',
            'away_team': 'Houston Astros',
            'bookmaker': 'FanDuel',
            'team': 'Blue Jays ML',
            'price': -116,
            'injury_flag': 0
        }
    ])

    nba_picks.to_csv(f"data/processed/nba_features_{today}.csv", index=False)
    mlb_picks.to_csv(f"data/processed/mlb_features_{today}.csv", index=False)
    print("Daily picks injected for April 22, 2025.")

if __name__ == '__main__':
    inject_daily_picks()
"""

# Save the picks injection script to the project
with open("sports_betting_model/src/models/inject_picks.py", "w") as f:
    f.write(inject_picks_script)

# Repackage everything into a final unified model build
shutil.make_archive("sports_betting_model_full_combined", 'zip', "sports_betting_model")

"sports_betting_model_full_combined.zip created with model + daily picks injector."
