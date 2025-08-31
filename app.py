import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="Rendement Calculator", layout="centered")
st.title("💰 Rendement Calculator — pensioen / belegging")
st.write("""
Bereken wat je belegging of pensioen kan opleveren.  
We kiezen voor een **realistische en defensieve aanpak**, gebaseerd op historische wereldwijde aandelenindex (MSCI World).  
""")

# -------------------------
# Info over rendementen
# -------------------------
with st.expander("📚 Waarom deze rendementen en bronnen?"):
    st.markdown("""
Historisch gezien is de wereldwijde aandelenmarkt (MSCI World) de afgelopen 40 jaar gemiddeld **ongeveer 8% per jaar** gestegen.  
We gebruiken deze gegevens om drie scenario’s te maken:  

| Scenario | Jaarlijks rendement | Uitleg |
|----------|------------------|-------|
| Tegenvallende markt | 3% | Voor conservatieve planning bij tegenvallende jaren |
| Neutrale markt | 6% | Realistisch, lange termijn gemiddeld |
| Optimistisch | 8% | Historisch haalbaar in goede jaren |

**Bronnen / data:**  
- [MSCI World Index Historical Returns](https://www.msci.com/our-solutions/indexes/world)  
- [Morningstar Global Market Index Data](https://www.morningstar.com/)  
- [Investopedia Historical Returns](https://www.investopedia.com/terms/h/historicalreturns.asp)

> ⚠️ Let op: verleden is geen garantie voor de toekomst.
""")

# -------------------------
# Inputs
# -------------------------
st.header("Stap 1 — Vul je gegevens in")

monthly_invest = st.number_input(
    "Maandelijkse inleg (€) 💰", 
    min_value=0.0, value=300.0, step=50.0,
    help="Het bedrag dat je elke maand opzij zet voor je belegging/pensioen."
)

years = st.number_input(
    "Aantal jaren inleggen ⏳", 
    min_value=1, value=30, step=1,
    help="Hoe lang je blijft inleggen voordat je het geld nodig hebt."
)

start_age = st.number_input(
    "Startleeftijd 👶", 
    min_value=18, max_value=70, value=30, step=1,
    help="Wanneer je begint met inleggen (voor pensioenplanning)."
)

scenario_options = {
    "Tegenvallende markt (3%) 📉": 0.03,
    "Neutrale markt (6%) ⚖️": 0.06,
    "Optimistische markt (8%) 🚀": 0.08
}

scenario = st.selectbox("Kies een scenario:", list(scenario_options.keys()), help="Kies hoe de markt zich ontwikkelt: conservatief, gemiddeld of optimistisch.")
yearly_return = scenario_options[scenario]

# -------------------------
# Berekening
# -------------------------
def future_value(P, r, n):
    """Bereken FV van maandelijkse inleg P, jaarlijks rendement r, n jaar"""
    return P * (((1 + r/12)**(12*n) - 1) / (r/12))

def monthly_payout(FV, payout_years):
    """Simpel lineair uitkering per maand"""
    return FV / (payout_years * 12)

# -------------------------
# Bereken knop
# -------------------------
if st.button("🔹 Bereken opbouw"):
    FV = future_value(monthly_invest, yearly_return, years)
    payout_20yr = monthly_payout(FV, 20)

    st.success(f"📊 Verwachte eindwaarde na {years} jaar: **€ {FV:,.0f}**")
    st.info(f"💸 Bij uitkering over 20 jaar: ca. **€ {payout_20yr:,.0f} per maand**")

    # Jaarlijkse opbouw grafiek
    with st.expander("📈 Toon jaarlijkse groei van je belegging"):
        yearly_balance = [future_value(monthly_invest, yearly_return, i) for i in range(1, years+1)]
        df = pd.DataFrame({"Jaar": list(range(1, years+1)), "Saldo (€)": yearly_balance})

        fig, ax = plt.subplots()
        ax.plot(df["Jaar"], df["Saldo (€)"], marker='o', color='green')
        ax.set_xlabel("Jaar")
        ax.set_ylabel("Saldo (€)")
        ax.grid(True)
        st.pyplot(fig)

    st.markdown("""
    ⚠️ **Disclaimer:**  
    - Dit is een indicatie op basis van historische gemiddelden.  
    - Werkelijke rendementen kunnen hoger of lager uitvallen.  
    - Deze tool houdt geen rekening met belastingen, inflatie of kosten.
    """)
