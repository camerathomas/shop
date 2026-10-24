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

cols = st.columns(3)

for i, product in enumerate(producten["producten"]):
    with cols[i % 3]:
        st.image("static/box1.jpg")
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
