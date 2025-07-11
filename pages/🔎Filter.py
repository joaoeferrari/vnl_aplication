import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('VNL2023.csv')

st.set_page_config(
    page_title='Filter',
    page_icon='🔎',
    layout='centered',
)
st.title('Filter')
st.write('Options to filter the dataset:  by country, position, or player name')

country = st.selectbox(
    'Select a country to filter the dataset:',
    options=['All'] + sorted(df['Country'].dropna().unique().tolist())
)
if country == 'All':
    country_details = df.copy()
else:
    country_details = df[df['Country'] == country].reset_index(drop=True)

position = st.selectbox('Select a position to filter the dataset:',
    options=['All']+ sorted(df['Position'].dropna().unique().tolist())
)
if position == 'All':
    position_details = country_details
else:
    position_details = country_details[country_details['Position'] == position].reset_index(drop=True)

if country == 'All' and position == 'All':
    position_details = df.copy()

search = st.button('Search')

if search:
    st.dataframe(position_details, hide_index=True)

st.divider()

# player
st.subheader('Filter by specific player: ')
player = st.selectbox('Select a player to filter the dataset:',
    options=df['Player'].unique(),
)
player_details = df[df['Player'] == player].drop(columns=['Player']).reset_index(drop=True)

if player:
    if player_details.empty:
        st.write(f"No data found for player: {player}. Check for correct spelling, as well as upper and lower case letters. Please always start with a capital letter.")
    else:
        st.write(f"Player: {player}")
        st.dataframe(player_details, hide_index=True)






 

