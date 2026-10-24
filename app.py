import json
import streamlit as st

st.set_page_config(page_title="Het Grote Niets", page_icon="🛒", layout="wide")

@st.cache_data
def laad_producten():
    with open("producten.json", "r", encoding="utf-8") as f:
        return json.load(f)

producten = laad_producten()

st.title("🛒 Het Grote Niets")
st.caption("Heeft u ook alles al? Dan bent u hier in de juiste winkel!")
st.markdown("---")

# HARDCODEER HIER DE URL VAN JOUW APP
# Vervang dit door de echte URL die je in je browser ziet
APP_URL = "https://shopshop.streamlit.app"  # <-- PAS DIT AAN

cols = st.columns(3)

for i, product in enumerate(producten["producten"]):
    with cols[i % 3]:
        # product["afbeelding"] is "app/static/box1.jpg"
        image_url = f"{APP_URL}/{product['afbeelding']}"
        try:
            st.image("app/static/box1.jpg",)
        except Exception as e:
            st.warning(f"Afbeelding niet gevonden: {e}")
        st.subheader(product["naam"])
        st.write(f"**{product['prijs']}**")
        st.write(product["beschrijving"])
        if st.button("Bestel nu", key=product["id"]):
            st.success(
                f"Gefeliciteerd! U hebt **{product['naam']}** besteld. "
                f"U ontvangt niets. Uw bestelling wordt niet verzonden. "
                f"Bedankt voor uw betaling van {product['prijs']}."
            )
        st.markdown("---")

st.caption(f"Totaal aantal producten: {len(producten['producten'])} · Allemaal even afwezig.")
