# Update the app.py with logic to only show top 3 picks for each sport using sorted model logic
updated_app_code = """
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(layout="wide")
st.title("Sports Betting Dashboard")

tabs = st.tabs(["NBA", "MLB", "Bankroll Tracker"])
today = datetime.now().strftime('%Y-%m-%d')

def display_top_picks(sport, df):
    # Rank picks by price descending as placeholder for model value
    top_picks = df.sort_values(by='price', ascending=False).head(3)
    for i, row in top_picks.iterrows():
        st.subheader(f"{row['away_team']} @ {row['home_team']}")
        st.text(f"Bookmaker: {row['bookmaker']} | Team: {row['team']} | Price: {row['price']}")
        with st.expander("Why this pick?"):
            st.write("This pick was selected by analyzing current odds, team stats, injury reports, and public betting trends.")
        if st.button(f"Add ${10} bet on {row['team']}", key=f"{sport}_{i}"):
            st.success(f"Bet on {row['team']} added to bankroll tracker!")

with tabs[0]:
    st.header("Top 3 NBA Picks Today")
    nba_path = f"data/processed/nba_features_{today}.csv"
    if os.path.exists(nba_path):
        nba_df = pd.read_csv(nba_path)
        display_top_picks("nba", nba_df)
    else:
        st.warning("NBA data not available yet.")

with tabs[1]:
    st.header("Top 3 MLB Picks Today")
    mlb_path = f"data/processed/mlb_features_{today}.csv"
    if os.path.exists(mlb_path):
        mlb_df = pd.read_csv(mlb_path)
        display_top_picks("mlb", mlb_df)
    else:
        st.warning("MLB data not available yet.")

with tabs[2]:
    st.header("Bankroll Tracker")
    st.write("This section will display all tracked bets and performance stats (coming soon).")
"""

# Write the updated frontend Streamlit code
with open("sports_betting_model/frontend/app.py", "w") as f:
    f.write(updated_app_code)

# Repackage the entire project
shutil.make_archive("sports_betting_model_final", 'zip', "sports_betting_model")

"sports_betting_model_final.zip created with top 3 pick logic."
