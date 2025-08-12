# app.py
import streamlit as st
import pandas as pd
import altair as alt
from analyze_cot import analyze_trends

st.set_page_config(page_title="COT FX Dashboard", layout="wide")

st.title("📊 Commitment of Traders - FX Trends")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("cot_data_latest.csv")
    except FileNotFoundError:
        st.warning("No live COT data found. Using sample fallback.")
        df = pd.read_csv("cot_sample.csv")
    return df

cot_df = load_data()
analysis_df = analyze_trends(cot_df)

st.subheader("Trend Summary")
st.dataframe(analysis_df, use_container_width=True)

pair = st.selectbox("Select Currency Pair", options=analysis_df['Pair'].unique())
pair_data = cot_df[cot_df['Pair'] == pair].copy()
pair_data['Date'] = pd.to_datetime(pair_data['Date'])

chart = alt.Chart(pair_data).mark_line(point=True).encode(
    x="Date:T",
    y="NonComm_Net:Q",
    tooltip=["Date", "NonComm_Net"]
).properties(
    title=f"{pair} - Non-Commercial Net Positions"
)

st.altair_chart(chart, use_container_width=True)
