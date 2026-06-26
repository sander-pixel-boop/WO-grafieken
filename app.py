import streamlit as st
import pandas as pd
import plotly.express as px

# WielerOrakel-stijl: Donker thema
st.set_page_config(layout="wide", page_title="WOC Tour de France Dashboard")

st.markdown("<h2 style='text-align: center;'>Tour de France 2026: WOC Polls</h2>", unsafe_allow_html=True)

# Custom CSS voor extra styling
st.markdown(
    """
    <style>
    /* Styling voor de expanders om ze meer in de stijl te krijgen */
    .streamlit-expanderHeader {
        background-color: #301141;
        color: #ed83ff;
        border-radius: 5px;
    }
    div[data-testid="stExpander"] div[role="button"] p {
        font-weight: bold;
        color: #ed83ff;
        font-size: 1.1rem;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #5d04ad;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def create_chart(title, data_dict):
    """
    Helper function to create a plotly horizontal bar chart.
    data_dict is a dictionary mapping category names to percentages.
    If the total percentage is less than 100, an 'Overig' category is added.
    """
    categories = list(data_dict.keys())
    percentages = list(data_dict.values())

    total = sum(percentages)
    if total < 100:
        categories.append("Overig")
        percentages.append(100 - total)

    df = pd.DataFrame({
        'Categorie': categories,
        'Percentage': percentages
    })

    fig = px.bar(
        df,
        x='Percentage',
        y='Categorie',
        orientation='h',
        title=title,
        color='Categorie',
        color_discrete_sequence=['#ed83ff', '#5d04ad', '#d65ce8', '#fffc', '#a855f7'],
        text='Percentage'
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        yaxis={'categoryorder':'total ascending'},
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    # Update x-axis to always end at 100
    fig.update_xaxes(range=[0, 110])

    return fig


st.markdown("---")
st.markdown("### Algemene Samenvatting")

st.markdown('''
Op basis van alle peilingen schetst de WOC-community het volgende verloop van de Tour de France:

- **Start & Geel:** Een bloedstollende ploegentijdrit levert een nek-aan-nekrace op tussen Visma, UAE en Red Bull. De eerste gele trui is direct een tweestrijd tussen topfavorieten Pogacar en Vingegaard.
- **Dominantie Pogacar:** De heuvel- en bergritten zijn een prooi voor de klassementsmannen, waarbij Tadej Pogacar afgetekend domineert. Hij wint meerdere ritten en houdt de gele trui stevig in handen.
- **Tijdverlies Vingegaard:** Jonas Vingegaard krijgt in de bergen tikken te verwerken. Na etappe 15 staat hij volgens de peilingen op een aanzienlijke achterstand van 2 tot 3+ minuten.
- **Strijd om Groen:** Waar Mads Pedersen in de zware sprintritten (zoals etappe 4) nog uitgesproken favoriet is, neemt Jasper Philipsen gedurende de Tour het initiatief over. Tegen het einde van de ronde is de verwachting overweldigend dat Philipsen het groen wint.
- **Tijdrit & Witte Trui:** Remco Evenepoel heerst in het tijdrijden (etappe 16). In het jongerenklassement is Isaac Del Toro veruit de grootste kanshebber voor de witte trui.
- **Vluchters:** Er zijn duidelijke kansen voor het type 'klim-vluchter' (denk aan Healy, Simmons, Van Gils) in etappes 3 en 13.
''')

st.markdown("#### Verwachtingen (Gebaseerd op specifieke peilingen)")
sum_cols = st.columns(4)

with sum_cols[0]:
    fig1 = create_chart("Eerste Gele Trui (Etappe 1)", {"Pogacar": 45, "Vingegaard": 42})
    st.plotly_chart(fig1, use_container_width=True)
with sum_cols[1]:
    fig2 = create_chart("Achterstand Vingegaard (Na Et. 15)", {"3+ minuten": 46, "2-3 minuten": 35})
    st.plotly_chart(fig2, use_container_width=True)
with sum_cols[2]:
    fig3 = create_chart("Groene Trui Verwachting (Et. 17)", {"Philipsen": 83})
    st.plotly_chart(fig3, use_container_width=True)
with sum_cols[3]:
    fig4 = create_chart("Witte Trui Verwachting (Et. 16)", {"Del Toro": 67})
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.markdown("### Uitslagen per Etappe")

stages_data = [
    {
        "name": "Etappe 1 (TTT)",
        "text": "Nek-aan-nekrace tussen Visma (34%) en UAE (31%), met Red Bull (26%) als outsider. Het eerste geel gaat nipt naar Pogacar (45%) of Vingegaard (42%).",
        "charts": [
            {"title": "Ploegen TTT", "data": {"Visma": 34, "UAE": 31, "Red Bull": 26}},
            {"title": "Eerste Gele Trui", "data": {"Pogacar": 45, "Vingegaard": 42}}
        ]
    },
    {
        "name": "Etappe 2 (Montjuic)",
        "text": "100% voor de GC-mannen (95%). Pogacar domineert: hij pakt de rit (90%) en het geel (77%).",
        "charts": [
            {"title": "Ritwinst", "data": {"Pogacar": 90}},
            {"title": "Gele Trui", "data": {"Pogacar": 77}}
        ]
    },
    {
        "name": "Etappe 3",
        "text": "Duidelijke vluchtersdag (79%), gericht op het type 'Klim-' (95%, bijv. Healy, Simmons, Van Gils). De gele trui is een muntopgooi: Pogacar behoudt hem (49%) of een vroege vluchter pakt hem (47%).",
        "charts": [
            {"title": "Scenario", "data": {"Vluchters": 79}},
            {"title": "Gele Trui", "data": {"Pogacar": 49, "Vroege vluchter": 47}}
        ]
    },
    {
        "name": "Etappe 4",
        "text": "Zware sprint ('Sprint+', 84%). Dit is op het lijf geschreven van Pedersen, die veruit favoriet is om hier het groen te pakken (66%).",
        "charts": [
            {"title": "Scenario", "data": {"Sprint+": 84}},
            {"title": "Groene Trui", "data": {"Pedersen": 66}}
        ]
    },
    {
        "name": "Etappe 5 (Massasprint)",
        "text": "Merlier pakt de ritwinst (59%), maar Philipsen verovert de groene trui (70%) doordat de groep hem consistenter inschat over de hele week.",
        "charts": [
            {"title": "Ritwinst", "data": {"Merlier": 59}},
            {"title": "Groene Trui", "data": {"Philipsen": 70}}
        ]
    },
    {
        "name": "Etappe 6 (Tourmalet)",
        "text": "Totale consensus. Pogacar wint de rit (94%) en staat stevig in het geel (92%). Scenario: een solo (44%) of een finish vanuit een klein groepje (39%).",
        "charts": [
            {"title": "Ritwinst", "data": {"Pogacar": 94}},
            {"title": "Finish Scenario", "data": {"Solo": 44, "Klein groepje": 39}}
        ]
    },
    {
        "name": "Etappe 12 (Massasprint)",
        "text": "Philipsen is heerser. Hij wint de sprint (47%) en verstevigt de groene trui (64%).",
        "charts": [
            {"title": "Ritwinst", "data": {"Philipsen": 47}},
            {"title": "Groene Trui", "data": {"Philipsen": 64}}
        ]
    },
    {
        "name": "Etappe 13 (Heuvelrit)",
        "text": "100% vroege vlucht, ideaal voor types als Simmons/Van Gils (56%). De daguitslag wordt aangevuld door de klassementsmannen (91%).",
        "charts": [
            {"title": "Type Vluchter Ritwinst", "data": {"Simmons/Van Gils": 56}}
        ]
    },
    {
        "name": "Etappe 14 (Bergrit)",
        "text": "Volledig voor de GC-mannen (100%). Pogacar is afgetekend favoriet (94%).",
        "charts": [
            {"title": "Ritwinst", "data": {"Pogacar": 94}}
        ]
    },
    {
        "name": "Etappe 15 (Bergrit)",
        "text": "Opnieuw de klassementsrenners (96%). Vingegaard krijgt hier een tik en staat na deze rit op 3+ minuten (46%) of 2-3 minuten (35%) achterstand.",
        "charts": [
            {"title": "Achterstand Vingegaard", "data": {"3+ minuten": 46, "2-3 minuten": 35}}
        ]
    },
    {
        "name": "Etappe 16 (ITT)",
        "text": "Evenepoel wint afgetekend (86%). Del Toro stelt de witte trui veilig (67%). De top 15 wordt gevuld door specialisten (Ganna, Vacek) en sterke GC-rijders.",
        "charts": [
            {"title": "Ritwinst", "data": {"Evenepoel": 86}},
            {"title": "Witte Trui", "data": {"Del Toro": 67}}
        ]
    },
    {
        "name": "Etappe 17 (Vlucht/Sprint)",
        "text": "Gereduceerde sprint in een 'Sprint+' scenario (76%). Ritwinst is een direct duel tussen Pedersen (36%) en Philipsen (32%). Het groen blijft veilig bij Philipsen (83%).",
        "charts": [
            {"title": "Ritwinst", "data": {"Pedersen": 36, "Philipsen": 32}},
            {"title": "Groene Trui", "data": {"Philipsen": 83}}
        ]
    }
]

for stage in stages_data:
    with st.expander(stage["name"]):
        st.markdown(f"**{stage['text']}**")

        # Display charts side by side if there are multiple
        num_charts = len(stage["charts"])
        if num_charts > 0:
            cols = st.columns(num_charts)
            for i, chart_info in enumerate(stage["charts"]):
                with cols[i]:
                    fig = create_chart(chart_info["title"], chart_info["data"])
                    st.plotly_chart(fig, use_container_width=True)

