import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import random

# Simulated daily picks with explanations
def get_daily_picks():
    mlb_games = [
        ("Red Sox vs Yankees", "Over 9", "Both teams have top 5 offenses and shaky bullpens."),
        ("Dodgers vs Mets", "Dodgers ML", "LA dominates at home and faces a rookie pitcher."),
        ("Giants vs Cubs", "Under 8", "Wind blowing in at Wrigley; two strong starters."),
        ("Astros vs Rangers", "Rangers +1.5", "Texas has covered the run line in 8 of last 10."),
        ("Phillies vs Braves", "Braves ML", "Braves have the starting pitching edge."),
        ("Tigers vs Twins", "Twins ML", "Twins are 7-1 vs Tigers this season."),
        ("White Sox vs Royals", "Over 8.5", "Both starters have ERA over 5.00."),
        ("Padres vs DBacks", "Padres -1.5", "Arizona struggles vs lefties."),
        ("Reds vs Brewers", "Under 8", "Two elite ground ball pitchers."),
        ("Athletics vs Mariners", "Mariners ML", "Oakland ranks bottom 3 in OPS.")
    ]

    nba_games = [
        ("Celtics vs Heat", "Under 206", "Game 1 trend + both teams top 5 defense."),
        ("Warriors vs Lakers", "Lakers ML", "LeBron's teams are 12-2 in playoff Game 1s."),
        ("Knicks vs Cavs", "Knicks +4.5", "Sharp money on Knicks; public all over Cavs."),
        ("Nuggets vs Suns", "Over 215", "Top 3 pace matchup with elite scorers."),
        ("Bucks vs Bulls", "Bucks -8", "Bucks 10-0 ATS vs sub-.500 teams."),
        ("Mavs vs Clippers", "Clippers ML", "Mavs on 3rd game in 4 nights."),
        ("76ers vs Raptors", "Under 210", "Both teams trend under in playoff Game 1s."),
        ("Kings vs Grizzlies", "Grizzlies +3", "Kings poor on road, 3-7 ATS last 10."),
        ("Pelicans vs Thunder", "Over 213", "Fast pace, both teams top 10 in FGA."),
        ("Nets vs Hawks", "Nets ML", "Hawks have worst road record in the East.")
    ]

    mlb_sample = random.sample(mlb_games, 8)
    nba_sample = random.sample(nba_games, 8)

    mlb_df = pd.DataFrame(mlb_sample, columns=["Game", "Pick", "Why"])
    mlb_df["Sport"] = "MLB"
    nba_df = pd.DataFrame(nba_sample, columns=["Game", "Pick", "Why"])
    nba_df["Sport"] = "NBA"

    return pd.concat([mlb_df, nba_df], ignore_index=True)

# Display picks by sport with explanation buttons
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
            st.markdown("---")

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

# Streamlit config and tab layout
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
