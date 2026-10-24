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

# Basis-URL van je Streamlit-app (deze werkt automatisch)
base_url = st.context.headers.get("Host", "localhost:8501")
# Gebruik https als de app op Streamlit Cloud draait
if "streamlit.app" in base_url:
    base_url = f"https://{base_url}"

cols = st.columns(3)

for i, product in enumerate(producten["producten"]):
    with cols[i % 3]:
        # Construeer de volledige URL naar het statische bestand
        # product["afbeelding"] is bijvoorbeeld "app/static/box1.jpg"
        image_url = f"{base_url}/{product['afbeelding']}"
        try:
            st.image(image_url, use_container_width=True)
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
