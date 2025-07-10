import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('VNL2023.csv')
st.set_page_config(
    page_title='Graphs',
    page_icon='📈',
    layout='wide',
)

st.title('📈 Graphs')

chart_data = df[['Player', 'Attack', 'Block', 'Serve', 'Set', 'Dig', 'Receive']]

st.bar_chart(chart_data, x="Player", y="Attack")

