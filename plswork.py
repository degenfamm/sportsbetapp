import streamlit as st
import pandas as pd
import os

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

    os.makedirs("data/processed", exist_ok=True)
    nba_picks.to_csv("data/processed/nba_features_2025-04-22.csv", index=False)
    mlb_picks.to_csv("data/processed/mlb_features_2025-04-22.csv", index=False)

# Streamlit button to trigger the function
st.title("Inject Model Picks")
if st.button("Inject 3 NBA & 3 MLB picks for April 22, 2025"):
    inject_daily_picks()
    st.success("✅ Model picks injected successfully!")
