import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


df = pd.read_csv('VNL2023.csv')

st.set_page_config(
    page_title='Graphs',
    page_icon='📈',
    layout='centered',
)

st.title('Graphs')
st.divider()

# graph 1
st.subheader('Top 10 Attack by Position')
position = st.selectbox('Select position:', df['Position'].unique())
df_filtered = df[df['Position'] == position]

fig = px.bar(df_filtered.sort_values('Attack', ascending=False).head(10), 
             x='Player', y='Attack', orientation='v', title=f'Top 10 Attack - {position}')
st.plotly_chart(fig)
st.divider()

# graph 2
st.subheader('Porcentual of Positions')
df_position = df['Position'].value_counts().reset_index()
fig = px.pie(df_position, values='count', names='Position',)
st.plotly_chart(fig)
st.divider()

# graph 3
st.subheader('Attack Variability')
df_skills = df[['Position', 'Attack']]
fig = px.box(df_skills,x='Position', y='Attack')
st.plotly_chart(fig)
st.divider()

# graph 4
st.subheader('Age vs Attack by Position')
fig = px.scatter(df, x='Age', y='Attack', color='Position',
                 hover_name='Player')
st.plotly_chart(fig)
