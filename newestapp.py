import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import random

# Simulated picks with detailed explanations
def get_daily_picks():
    mlb_games = [
        ("Red Sox vs Yankees", "Over 9", "Both teams rank top 5 in home run rate and are starting back-end pitchers. The wind is blowing out at Fenway Park."),
        ("Dodgers vs Mets", "Dodgers ML", "Dodgers are 14-3 at home this month. Facing a Mets starter with a 5.60 ERA and poor road splits."),
        ("Giants vs Cubs", "Under 8", "Wrigley wind is blowing in 12mph. Both starters are top 20 in ground ball rate."),
        ("Astros vs Rangers", "Rangers +1.5", "Rangers have covered 7 of last 9 games as underdogs. Astros bullpen has a 6.20 ERA last 10."),
        ("Phillies vs Braves", "Braves ML", "Braves starter has a 0.87 WHIP in last 3 starts. Phillies struggle vs right-handed power pitchers."),
    ]

    nba_games = [
        ("Celtics vs Heat", "Under 206", "Game 1 historically trends under. Both teams in top 5 defensive rating and play slower pace in playoffs."),
        ("Warriors vs Lakers", "Lakers ML", "LeBron-led teams are 12-2 in playoff Game 1s. Lakers rested; Warriors on short travel turnaround."),
        ("Knicks vs Cavs", "Knicks +4.5", "Sharp money hitting Knicks. Public is heavily on Cavs but line moved in opposite direction."),
        ("Nuggets vs Suns", "Over 215", "Top 2 pace matchup with elite ISO scorers. Both teams average 116+ in last 5 games."),
        ("Bucks vs Bulls", "Bucks -8", "Bucks are 11-1 ATS vs teams under .500. Bulls without 2 key starters tonight."),
    ]

    mlb_sample = random.sample(mlb_games, 5)
    nba_sample = random.sample(nba_games, 5)

    mlb_df = pd.DataFrame(mlb_sample, columns=["Game", "Pick", "Why"])
    mlb_df["Sport"] = "MLB"
    nba_df = pd.DataFrame(nba_sample, columns=["Game", "Pick", "Why"])
    nba_df["Sport"] = "NBA"

    return pd.concat([mlb_df, nba_df], ignore_index=True)

# Display picks by sport
def display_picks_by_sport(picks_df, sport_name):
    sport_df = picks_df[picks_df['Sport'] == sport_name]
    for i, row in sport_df.iterrows():
        with st.container():
            cols = st.columns([3, 2, 2])
            cols[0].markdown(f"**{row['Game']}**")
            cols[1].markdown(f"**Pick:** {row['Pick']}")
            with cols[2]:
                with st.expander("📘 Why this pick?"):
                    st.markdown(row['Why'])
                if st.button(f"➕ Add to Bankroll ({row['Game']})", key=f"{sport_name}_{i}"):
                    add_to_bankroll_auto(row['Game'], row['Pick'])

# Auto-add to bankroll
def add_to_bankroll_auto(game, pick):
    odds = -110 if "Under" in pick or "Over" in pick else -120
    new_row = pd.DataFrame([[
        date.today(), game, 10.0, odds, "", 0.0
    ]], columns=['Date', 'Game', 'Bet Size', 'Odds', 'Result (W/L)', 'Profit/Loss'])

    if 'bankroll' not in st.session_state:
        st.session_state['bankroll'] = new_row
    else:
        st.session_state['bankroll'] = pd.concat([st.session_state['bankroll'], new_row], ignore_index=True)

# Bankroll tracker
def bankroll_tracker():
    st.subheader("📊 Bankroll Tracker")
    if 'bankroll' not in st.session_state:
        st.session_state['bankroll'] = pd.DataFrame(columns=['Date', 'Game', 'Bet Size', 'Odds', 'Result (W/L)', 'Profit/Loss'])

    with st.form("bet_entry"):
        col1, col2 = st.columns(2)
        date_input = col1.date_input("Date", value=date.today())
        game = col2.text_input("Game")
        bet_size = col1.number_input("Bet Size", min_value=1.0, step=1.0)
        odds = col2.number_input("Odds", value=-110)
        result = col1.selectbox("Result", ['W', 'L'])
        submitted = st.form_submit_button("Add Bet")

        if submitted:
            profit = bet_size * (abs(odds) / 100) if odds < 0 else bet_size * (odds / 100)
            profit = profit if result == 'W' else -bet_size
            new_row = pd.DataFrame([[date_input, game, bet_size, odds, result, round(profit, 2)]],
                                   columns=['Date', 'Game', 'Bet Size', 'Odds', 'Result (W/L)', 'Profit/Loss'])
            st.session_state['bankroll'] = pd.concat([st.session_state['bankroll'], new_row], ignore_index=True)

    st.write("### Bet History")
    st.dataframe(st.session_state['bankroll'])
    total_profit = st.session_state['bankroll']['Profit/Loss'].sum()
    st.write(f"**Total Profit/Loss: ${round(total_profit, 2)}**")

# App layout
st.set_page_config(page_title="DegenFamm Sports Betting Dashboard", layout="wide")
st.title("💸 DegenFamm Sports Betting Dashboard")

daily_picks = get_daily_picks()

tab1, tab2, tab3 = st.tabs(["🏀 NBA Picks", "⚾ MLB Picks", "💼 Bankroll"])

with tab1:
    st.subheader(f"NBA Picks for {date.today().strftime('%B %d, %Y')}")
    display_picks_by_sport(daily_picks, "NBA")

with tab2:
    st.subheader(f"MLB Picks for {date.today().strftime('%B %d, %Y')}")
    display_picks_by_sport(daily_picks, "MLB")

with tab3:
    bankroll_tracker()
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
