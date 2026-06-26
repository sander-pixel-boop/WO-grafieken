import streamlit as st
import pandas as pd
import plotly.express as px

# WielerOrakel-stijl: Donker thema
st.set_page_config(layout="wide", page_title="WOC Tour de France Dashboard")

st.markdown("<h2 style='text-align: center;'>Tour de France 2026: WOC Polls</h2>", unsafe_allow_html=True)

# Data preparatie
data_e1 = pd.DataFrame({
    'Ploeg': ['Visma', 'UAE', 'Red Bull', 'Ineos'],
    'Percentage': [34, 31, 26, 7]
})

data_e2_winst = pd.DataFrame({
    'Renner': ['Pogacar', 'Overig GC', 'Vluchter'],
    'Percentage': [90, 10, 0]
})

# Grafiek Etappe 1 (TTT)
fig_e1 = px.bar(
    data_e1, 
    x='Percentage', 
    y='Ploeg', 
    orientation='h', 
    title='Etappe 1: Ritwinst TTT',
    color='Ploeg',
    color_discrete_map={
        'Visma': '#ffe500', 
        'UAE': '#aaaaaa', 
        'Red Bull': '#001a4d', 
        'Ineos': '#ff0000'
    },
    text='Percentage'
)

fig_e1.update_layout(
    template='plotly_dark', 
    showlegend=False, 
    yaxis={'categoryorder':'total ascending'}
)
fig_e1.update_traces(texttemplate='%{text}%', textposition='outside')

st.plotly_chart(fig_e1, use_container_width=True)

# Grafiek Etappe 2 (Montjuic)
fig_e2 = px.bar(
    data_e2_winst, 
    x='Percentage', 
    y='Renner', 
    orientation='h', 
    title='Etappe 2: Ritwinst Montjuic',
    color_discrete_sequence=['#00bfff']
)

fig_e2.update_layout(
    template='plotly_dark', 
    yaxis={'categoryorder':'total ascending'}
)

st.plotly_chart(fig_e2, use_container_width=True)
