import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('VNL2023.csv')

st.set_page_config(
    page_title='Filter',
    page_icon='🔎',
    layout='wide',
)
st.title('🔎 Filter')
st.write('Options to filter the dataset:  by country, position, or player name')
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     byCountry = st.checkbox('By Country')
# with col2:
#     byPosition = st.checkbox('By Position')
# with col3:
#     byPlayer = st.checkbox('By Player')
# with col3:
#     allTabs = st.checkbox('All Tabs')

st.divider()

# country
st.subheader('🏳️ Filter by Country: ')

country = st.text_input("Enter the country name")

country_details = df[df['Country'] == country].drop(columns=['Country']).reset_index(drop=True)

if country:
    if country_details.empty:
        st.write(f"No data found for country: {country}. Check for correct spelling, as well as upper and lower case letters. Please always start with a capital letter.")
    else:
        st.write(f"Country: {country}")
        st.dataframe(country_details, hide_index=True)

st.divider()

# position
st.subheader('❎ Filter by Position: ')


position = st.text_input("Enter the player's position")
st.write("Available positions: OH, OP, MB, S, L")

position_details = df[df['Position'] == position].drop(columns=['Position']).reset_index(drop=True)

if position:
    if position_details.empty:
        st.write(f"No data found for position: {position}. Check for correct spelling, as well as upper and lower case letters. Please always start with a capital letter.")
    else:
        st.write(f"Position: {position}")
        st.dataframe(position_details, hide_index=True)
st.divider()

# player
st.subheader('🧍 Filter by Player: ')

player = st.text_input("Enter the player's name")

player_details = df[df['Player'] == player].drop(columns=['Player']).reset_index(drop=True)

if player:
    if player_details.empty:
        st.write(f"No data found for player: {player}. Check for correct spelling, as well as upper and lower case letters. Please always start with a capital letter.")
    else:
        st.write(f"Player: {player}")
        st.dataframe(player_details, hide_index=True)






 

