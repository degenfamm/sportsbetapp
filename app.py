import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

def get_daily_picks():
    data = {
        'Sport': ['MLB', 'NBA', 'MLB'],
        'Game': ['Red Sox vs White Sox', 'Celtics vs Magic', 'Mets vs Cardinals'],
        'Pick': ['Over 9', 'Under 206', 'Mets ML'],
        'Odds': [-110, -105, -140],
        'Edge (%)': [7.2, 5.9, 6.8],
        'Trend Flag': ['High ERAs', 'Game 1 Under', 'Sharp Money']
    }
    return pd.DataFrame(data)

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

# Set page configuration
st.set_page_config(page_title="DegenFamm Sports Betting Dashboard", layout="wide")
st.title("💸 DegenFamm Sports Betting Dashboard")

# Load picks
all_picks = get_daily_picks()
mlb_picks = all_picks[all_picks['Sport'] == 'MLB']
nba_picks = all_picks[all_picks['Sport'] == 'NBA']

# Define tabs
tab1, tab2, tab3 = st.tabs(["🏀 NBA Picks", "⚾ MLB Picks", "💼 Bankroll"])

# NBA Tab
with tab1:
    st.subheader("Today's NBA Picks")
    if not nba_picks.empty:
        st.dataframe(nba_picks)
    else:
        st.info("No NBA picks available today.")

# MLB Tab
with tab2:
    st.subheader("Today's MLB Picks")
    if not mlb_picks.empty:
        st.dataframe(mlb_picks)
    else:
        st.info("No MLB picks available today.")

# Bankroll Tracker Tab
with tab3:
    bankroll_tracker()
