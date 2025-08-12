# app.py - Streamlit skeleton for Bliss Tide COT FX Insights
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

st.set_page_config(page_title='Bliss Tide COT FX Insights', layout='wide')
st.title('Bliss Tide — COT FX Insights (Phase 1)')

DATA = Path('cot_data_latest.csv')
SAMPLE = Path('sample_cot_data.csv')

@st.cache_data
def load_data():
    if DATA.exists():
        df = pd.read_csv(DATA, parse_dates=['date'])
    else:
        df = pd.read_csv(SAMPLE, parse_dates=['date'])
    return df

df = load_data()

st.sidebar.header('Controls')
pairs = sorted(df['pair'].unique())
pair = st.sidebar.selectbox('Pair', pairs)

df_pair = df[df['pair']==pair].sort_values('date')

st.subheader(f'{pair} — Net Specs & Open Interest')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_pair['date'], y=df_pair['net_spec'], name='Net Spec'))
fig.add_trace(go.Bar(x=df_pair['date'], y=df_pair['open_interest'], name='Open Interest', yaxis='y2'))
fig.update_layout(yaxis2=dict(overlaying='y', side='right', title='Open Interest'))
st.plotly_chart(fig, use_container_width=True)

st.subheader('Raw Data')
st.dataframe(df_pair.reset_index(drop=True))
