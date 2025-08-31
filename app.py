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
#
