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

# --- Tabs ---
tab_winkel, tab_over, tab_innovatie, tab_vacatures, tab_franchise, tab_ontspullen, tab_blind = st.tabs([
    "🛒 Winkel",
    "📖 Over ons",
    "💡 Innovatie",
    "💼 Vacatures",
    "📋 Franchise",
    "🗑️ Ontspullen",
    "🕶️ Blind kopen"
])

# ============================================================
# TAB 1: WINKEL
# ============================================================
with tab_winkel:
    # Actie-banner
    st.markdown("""
    > **🎁 TIJDELIJKE ACTIE:** Bij elke bestelling van €10,00 of meer ontvangt u een onzichtbaar kado.
    > Op=op! (Wat niet kan, want er is niets.)
    """)

    st.markdown("---")

    cols = st.columns(3)

    for i, product in enumerate(producten["producten"]):
        with cols[i % 3]:
            st.image(product["afbeelding"])
            st.subheader(product["naam"])
            st.write(f"**{product['prijs']}**")
            st.write(product["beschrijving"])

            # Voorraad-indicator (absurd)
            st.caption("📦 Op voorraad: **-465 stuks** · 🔥 POPULAIR PRODUCT · ⭐⭐⭐⭐⭐ (0 beoordelingen)")

            if st.button("Bestel nu", key=product["id"]):
                st.success(
                    f"Gefeliciteerd! U hebt **{product['naam']}** besteld. "
                    f"U ontvangt niets. Uw bestelling wordt niet verzonden. "
                    f"Bedankt voor uw betaling van {product['prijs']}."
                )
            st.markdown("---")

    # Klantenreviews
    st.header("⭐ Wat zeggen onze klanten?")
    st.write("**0/5 sterren** — Gebaseerd op 0 beoordelingen")
    st.write('*"..."* — Anoniem')
    st.write('*"..."* — Ook anoniem')
    st.write('*"..."* — Iemand anders')
    st.success("**Wat zeggen onze klanten? Helemaal niets! Dus ze zijn blij.**")

    st.markdown("---")

    # Filosofen-quotes
    st.header("📜 Grote denkers over het Niets")
    st.write('*"Niets is nutteloos, zelfs het nutteloze niet."* — Montaigne')
    st.write('*"Niets is nuttiger dan de nutteloze kunsten."* — Ovidius')
    st.write('*"Het nuttige is een nutteloze last."* — Ionesco')
    st.write('*"Niets is zo interessant als het niets."* — Graham Priest')
    st.info("Zelfs de grootste filosofen zijn het erover eens: Niets is het overdenken waard. En bij ons kunt u het ook kopen.")

# ============================================================
# TAB 2: OVER ONS
# ============================================================
with tab_over:
    st.header("📖 Over ons")
    st.write("""
    **Wie zijn wij?**
    Wij stellen ons niet voor. Eigenlijk stellen wij zelfs niets voor.

    **Wat doen wij?**
    Wij laten u in de waan dat u iets koopt. En hoe weten wij als geen ander hoe lekker, veilig en cozy die waan kan zijn.

    **Waarom?**
    Omdat u zonder die waan misschien wel zou beseffen dat u niets nodig hebt. En dat kunnen wij niet hebben.

    **Waarom wij?**
    Omdat u alles al hebt. En omdat wij het enige zijn dat u nog niet hebt: niets.
    """)

# ============================================================
# TAB 3: INNOVATIE
# ============================================================
with tab_innovatie:
    st.header("💡 Innovatie")
    st.write("""
    Heeft u ooit wel eens gehoord van een lege zak waar u niets in kan doen? Wij wel.

    Volgens onze omzetcijfers zit er een flinke stijging in het aantal klanten dat het liefste helemaal niets wil. En wij kunnen dat leveren! Wij zijn de eerste en enige, niet alleen in Nederland of Europa, nee wij leveren niets aan de hele wereld.

    Maar nu was er in ons hoofdkantoor een jongen van sales, die zich afvroeg waar de mensen al dat niets laten? In deze lege omhulsels, die zelf niets omhulsen, want eerlijk gezegd: het is niet alleen of ze er niet zijn, ze zijn er gewoon echt niet!

    Wij verwachten dat dit de uitvinding van 2012 had kunnen zijn, maar het is pas in dit jaar uitgevonden. En wij waren er als eerste bij een gigantische voorraad nietsomullende niet-omhulsels in te slaan.

    En vergeef hun die gekke naam, de fabrikant heeft nog geen marketingafdeling, net zoals de productieafdeling en de directeur ook nog aangetrokken moeten worden, maar dat geeft niets, want als ze er al wel waren geweest had u ook niets gekregen, en dat noemen wij topservice!
    """)

    st.subheader("📊 Onze cijfers")
    st.write("- Aantal klanten dat niets wil: **stijgende lijn**")
    st.write("- Aantal producten geleverd: **0**")
    st.write("- Aantal klachten: **0** (want er is niets om over te klagen)")
    st.write("- Tevredenheid: **100%** (van 0 klanten)")

# ============================================================
# TAB 4: VACATURES
# ============================================================
with tab_vacatures:
    st.header("💼 Vacatures")
    st.write("**Wilt u bij ons komen werken? Dan zou ik maar heel snel verder zoeken!**")

    st.subheader("Openstaande vacatures")
    st.write("**Marketingmanager Niets** (0 uur per week) — U hoeft niets te doen. Er is geen budget. Er is geen team. U bent aangenomen.")
    st.write("**Magazijnmedewerker** (0 uur per week) — U hoeft niets op te slaan. Er is niets. Het magazijn is leeg.")
    st.write("**Klantenservice** (0 uur per week) — U hoeft niemand te woord te staan. Er zijn geen klanten. En die zijn tevreden.")

    st.subheader("Arbeidsvoorwaarden")
    st.write("- Salaris: **niets**")
    st.write("- Vakantiedagen: **onbeperkt** (u werkt toch niet)")
    st.write("- Pensioen: **niets**")
    st.write("- Doorgroeimogelijkheden: **geen**")
    st.write("- Werkplezier: **gegarandeerd** (want u hoeft niets te doen)")

    st.info("Wij zijn een werkgever waar u niets aan hebt.")

# ============================================================
# TAB 5: FRANCHISE
# ============================================================
with tab_franchise:
    st.header("📋 Franchise")
    st.write("**Wilt u ook de voordelen genieten van het hebben van een eigen zaak waarvoor u helemaal niets hoeft te doen? Dat kan niet.**")

    st.subheader("Onze franchisevoorwaarden")
    st.write("Om franchise te worden bij Niets, moet u aan één voorwaarde voldoen: u moet **tegenstribbelen** als wij zeggen dat het eigenlijk niet kan.")
    st.write("Als u dat doet, mag u franchise worden. Maar dan wel onder de volgende voorwaarden:")
    st.write("- U mag ons logo niet gebruiken")
    st.write("- U mag onze naam niet gebruiken")
    st.write("- U deelt niet mee in de gezamenlijke lagere inkookosten")
    st.write("- U krijgt niets")
    st.write("*\"Maar dat is toch geen franchise?\"* zult u zeggen. En dat is precies de bedoeling.")

    st.subheader("Hoe word ik franchise?")
    st.write("1. Lees onze franchisevoorwaarden.")
    st.write("2. Zeg dat het zo niet kan.")
    st.write("3. Wij zeggen dat het wel kan.")
    st.write("4. U zegt dat het echt niet kan.")
    st.write("5. Wij zeggen: \"Dan toch.\"")
    st.write("6. U zegt: \"Vooruit dan maar.\"")
    st.write("7. Gefeliciteerd, u bent franchise. U krijgt niets.")

# ============================================================
# TAB 6: ONTSPULLEN
# ============================================================
with tab_ontspullen:
    st.header("🗑️ Ontspullen")
    st.write("""
    Vergeet niet: als u nu iets hebt gekocht, moet u eerst iets wegdoen in huis. Want anders past uw aankoop er niet bij.

    Upload een video van iets wat u daadwerkelijk uit huis gooit, stop het in een gesloten vuilniszak, en laat de camera te allen tijde gericht op de vuilniszak totdat hij in de vuilnisauto verdwijnt.

    **Onze regels:**
    - Video van ten minste **72 uur** in HD
    - Beschrijving van elke gebeurtenis in **foutloos Latijn**
    - **Geen montage**
    - Minimaal **300GB**
    - Mocht er een paar minuten missen van het beeld, dan beschouwen wij dat als verdacht

    Ons team zal elke video twee keer bekijken om er zeker van te zijn dat u niet fraudeert. Hartelijk dank voor uw aandacht, en veel succes met uw video!
    """)

    st.subheader("Na goedkeuring")
    st.write("Als uw video wordt goedgekeurd, beloven wij **zo langzaam mogelijk** niets toe te sturen. Wij streven ernaar dit binnen een redelijke termijn te doen. Maar zoals u van ons gewend bent, kan dat even duren.")

# ============================================================
# TAB 7: BLIND KOPEN
# ============================================================
with tab_blind:
    st.header("🕶️ Blind kopen")
    st.write("""
    U krijgt geen productbeschrijving. Geen foto. Geen idee. Want u krijgt exact wat u wilt: niets.

    Vanaf vorig jaar boden wij een extra dienst aan waarover we nog geen enkele klant hebben ingelicht: **blind kopen!**

    Via een betrouwbare uitpakker van vrachtwagens op parkeerplaatsen hebben wij beslag weten te leggen op een grote partij ontlede ledigheid, en daar kunt u de vruchten van plukken. Vanwege het iets hogere risico zijn deze producten wel iets duurder, maar daar krijgt u dan ook echt helemaal **Niets** voor.

    En Niets hebben we deze keer Niet voor NIets met een hoofdletter geschreven! Tel uit onze winst en uw veel lichtere portemonnee.
    """)

    st.subheader("Waarom Niets met een hoofdletter?")
    st.write("Omdat het belangrijk voor ons is. En omdat het groter klinkt. En omdat wij deze keer Niets Niet voor Niets met een hoofdletter schrijven. Tel uit uw winst.")

st.markdown("---")
st.caption(f"Totaal aantal producten: {len(producten['producten'])} · Allemaal even afwezig.")
