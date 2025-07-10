import streamlit as st
import pandas as pd

df = pd.read_csv('VNL2023.csv')

st.set_page_config(
    page_title='Statistics',
    page_icon='📊',
    layout='wide',
)

st.title('📊 Statistics Filtering')

st.markdown('''
Here is some highlights of the dataset:
''')
st.divider()

st.subheader('📈 Overview:')
st.write('Players:', df['Player'].nunique())
st.write('Countries:', df['Country'].nunique())
st.write('Setters:', df[df['Position'] == 'S']['Player'].nunique())
st.write('Middle Blockers:', df[df['Position'] == 'MB']['Player'].nunique())
st.write('Outside Hitters:', df[df['Position'] == 'OH']['Player'].nunique())
st.write('Liberos:', df[df['Position'] == 'L']['Player'].nunique())
st.write('Opposites:', df[df['Position'] == 'OP']['Player'].nunique())

st.subheader('🏆 The bests of each category:')
# attack
st.write('Attack:')
ba = df.loc[df['Attack'] == df['Attack'].max()]
st.dataframe(ba, hide_index=True)

# block
st.write('Block:')
bb = df.loc[df['Block'] == df['Block'].max()]
st.dataframe(bb, hide_index=True)

# serve
st.write('Serve:')
bs = df.loc[df['Serve'] == df['Serve'].max()]
st.dataframe(bs, hide_index=True)

# set
st.write('Set:')
bs = df.loc[df['Set'] == df['Set'].max()]
st.dataframe(bs, hide_index=True)

# dig
st.write('Dig:')
bd = df.loc[df['Dig'] == df['Dig'].max()]
st.dataframe(bd, hide_index=True)

# receive
st.write('Receive:')   
br = df.loc[df['Receive'] == df['Receive'].max()]
st.dataframe(br, hide_index=True)


