import json
import streamlit as st

st.set_page_config(page_title="Het Grote Niets", page_icon="🛒", layout="wide")

if "winkelwagen" not in st.session_state:
    st.session_state.winkelwagen = []
if "bestellingen" not in st.session_state:
    st.session_state.bestellingen = []

@st.cache_data
def laad_producten():
    with open("producten.json", "r", encoding="utf-8") as f:
        return json.load(f)

producten = laad_producten()

st.title("🛒 Het Grote Niets")
st.caption("Heeft u ook alles al? Dan bent u hier in de juiste winkel!")
st.markdown("---")

# --- Tabs ---
tab_winkel, tab_afrekenen, tab_bestellingen, tab_over, tab_innovatie, tab_vacatures, tab_franchise, tab_ontspullen, tab_blind, tab_retour, tab_nieuwsbrief = st.tabs([
    "🛒 Winkel",
    "💰 Afrekenen",
    "📦 Mijn winkelwagen/mandje/mandje op wieletjes",
    "📖 Over ons",
    "💡 Innovatie",
    "💼 Vacatures",
    "📋 Franchise",
    "🗑️ Ontspullen",
    "🕶️ Blind kopen",
    "🔄 Retourneren",
    "📧 Nieuwsbrief"
])

# ============================================================
# TAB 1: WINKEL
# ============================================================
with tab_winkel:
    st.markdown("""
    > **🎁 TIJDELIJKE ACTIE:** ...
    """)
    st.markdown("""
    > **🔥 1 HALEN, 2 BETALEN!** ...
    """)
    st.markdown("---")

    cols = st.columns(3)

    for i, product in enumerate(producten["producten"]):
        with cols[i % 3]:
            st.image(product["afbeelding"])
            st.subheader(product["naam"])
            st.write(f"**{product['prijs']}**")
            st.write(product["beschrijving"])
            st.caption("📦 Op voorraad: **-465 stuks** · 🔥 POPULAIR PRODUCT · ⭐⭐⭐⭐⭐ (0 beoordelingen)")

            # Bestel nu-knop
            if st.button("Bestel nu", key=f"bestel_{product['id']}"):
                st.success(
                    f"Gefeliciteerd! U hebt **{product['naam']}** besteld. "
                    f"Uw bestelling is geplaatst. Uw levering is gepland voor het jaar 3000. "
                    f"Wilt u een snellere levering? Dat kan niet, maar u kunt wel voor de garantielevering betalen. "
                    f"Het product wordt 100% duurder, maar u weet dan 100% zeker dat u echt niets krijgt. Dat is logisch!"
                )

            # In winkelwagentje stoppen
            if st.button("In winkelwagentje stoppen", key=f"wagen_{product['id']}"):
                st.session_state.actieve_flow = product["id"]

            # Toon de flow als deze actief is voor dit product
            if st.session_state.get("actieve_flow") == product["id"]:
                st.warning("De winkelwagentjes zijn helaas allemaal in gebruik. Mag het ook een winkelmandje zijn?")

                keuze_mandje = st.radio(
                    "Mag het ook een winkelmandje zijn?",
                    ["Ja", "Nee"],
                    key=f"mandje_{product['id']}"
                )

                if keuze_mandje == "Ja":
                    keuze_type = st.radio(
                        "En wilt u dan liever een mandje zelf dragen of een model met uitklaphengsel en wieletjes?",
                        ["Zelf dragen", "Met uitklaphengsel en wieletjes"],
                        key=f"type_{product['id']}"
                    )
                    keuze_kleur = st.radio(
                        "Welke kleur wilt u?",
                        ["Groen", "Blauw", "Rood"],
                        key=f"kleur_{product['id']}"
                    )
                    keuze_materiaal = st.radio(
                        "Welk materiaal wilt u?",
                        ["Hout", "Plastic", "IJzer", "Steen", "Gietbeton", "Tweedehands WC-papier (klimaatvriendelijk)"],
                        key=f"materiaal_{product['id']}"
                    )
                    keuze_inpakken = st.radio(
                        "Moeten we het inpakken als een kadootje?",
                        ["Ja", "Nee"],
                        key=f"inpakken_{product['id']}"
                    )
                    keuze_openbare_weg = st.radio(
                        "Wilt u ermee de openbare weg op?",
                        ["Ja", "Nee"],
                        key=f"weg_{product['id']}"
                    )
                    keuze_rijbewijs = st.radio(
                        "Heeft u een rijbewijs W(inkelwagen)?",
                        ["Ja", "Nee"],
                        key=f"rijbewijs_{product['id']}"
                    )

                    # Toevoegen aan winkelwagen
                    if st.button("Toevoegen aan winkelwagen", key=f"toevoegen_{product['id']}"):
                        st.session_state.winkelwagen.append({
                            "product": product["naam"],
                            "prijs": product["prijs"],
                            "keuzes": {
                                "type": keuze_type,
                                "kleur": keuze_kleur,
                                "materiaal": keuze_materiaal,
                                "inpakken": keuze_inpakken,
                                "openbare_weg": keuze_openbare_weg,
                                "rijbewijs": keuze_rijbewijs
                            }
                        })
                        st.session_state.actieve_flow = None  # Reset de flow
                        st.success(
                            f"**{product['naam']}** is toegevoegd aan uw winkelwagen, met al uw keuzes. "
                            f"U kunt verder winkelen of naar de kassa gaan."
                        )
                    st.info(
                        "Ach, een rijbewijs is niet nodig. En we hebben alleen maar neon geel als kleur. "
                        "Maar wees gerust: morgen staat het niet voor uw deur, want het past waarschijnlijk toch niet door uw brievenbus!"
                    )
                else:
                    st.info("Jammer. Dan kunt u helaas niets bestellen. Maar u kunt het altijd later opnieuw proberen.")
                    if st.button("Sluiten", key=f"sluiten_{product['id']}"):
                        st.session_state.actieve_flow = None

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
# TAB: AFREKENEN
# ============================================================
with tab_afrekenen:
    st.header("💰 Afrekenen")

    if not st.session_state.winkelwagen:
        st.info("Uw winkelwagen is leeg. Dat is op zichzelf al een prestatie, want wij verkopen niets. Maar u kunt altijd iets toevoegen.")
    else:
        st.write("Uw winkelwagen:")
        for i, item in enumerate(st.session_state.winkelwagen):
            st.write(f"**{item['product']}** — {item['prijs']}")

        st.markdown("---")

        # ✅ DEZE REGEL MOET INSPRINGEN (4 spaties)
        if st.button("Afrekenen", type="primary"):
            verhalen = []

            for item in st.session_state.winkelwagen:
                keuzes = item["keuzes"]
                verhaal = []

                # Type
                if keuzes.get("type") == "Met uitklaphengsel en wieletjes":
                    verhaal.append("U koos voor een uniek uitklaphengsel met vier degelijke, onverwoestbare wieletjes.")
                elif keuzes.get("type") == "Zelf dragen":
                    verhaal.append("U koos voor zelf dragen—dapper, want er is niets om te dragen.")

                # Kleur
                if keuzes.get("kleur") == "Blauw":
                    verhaal.append("U koos voor blauw, een rustige kleur die helaas niet op voorraad is.")
                elif keuzes.get("kleur") == "Groen":
                    verhaal.append("U koos voor groen, een milieuvriendelijke kleur die wij niet hebben.")
                elif keuzes.get("kleur") == "Rood":
                    verhaal.append("U koos voor rood, de kleur van gevaar. Wij hebben besloten uw keuze te negeren.")

                # Materiaal
                if keuzes.get("materiaal") == "Gietbeton":
                    verhaal.append("Wij zullen eerst een mal timmeren om dit gevaarte in gietbeton te kunnen vervaardigen.")
                elif keuzes.get("materiaal") == "Tweedehands WC-papier (klimaatvriendelijk)":
                    verhaal.append("U koos voor tweedehands WC-papier, klimaatvriendelijk en bijzonder moeilijk te vinden. Wij hebben het dan ook niet.")
                elif keuzes.get("materiaal") == "Steen":
                    verhaal.append("U koos voor steen. Wij hebben geen steen. Wij hebben niets.")
                elif keuzes.get("materiaal") == "Hout":
                    verhaal.append("U koos voor hout. Wij hebben geen hout, maar wij zullen uw keuze respecteren door u niets van hout te sturen.")
                elif keuzes.get("materiaal") == "Plastic":
                    verhaal.append("U koos voor plastic. Dat is slecht voor het milieu, dus wij sturen u niets. Dat is beter voor het milieu.")
                elif keuzes.get("materiaal") == "IJzer":
                    verhaal.append("U koos voor ijzer. Wij hebben geen ijzer, maar wij zullen uw bestelling extra stevig niet verpakken.")

                # Inpakken
                if keuzes.get("inpakken") == "Nee":
                    verhaal.append("Het scheelt enorm dat we het niet in hoeven te pakken.")
                elif keuzes.get("inpakken") == "Ja":
                    verhaal.append("Wij zullen uw niets zorgvuldig inpakken in niets, voorzien van een nietszeggend label.")

                # Openbare weg
                if keuzes.get("openbare_weg") == "Ja":
                    verhaal.append("Omdat u er de openbare weg mee op wilt, zullen we een extra lange levertermijn in acht nemen, om de veiligheid van u en uw omgeving te waarborgen.")

                # Rijbewijs
                if keuzes.get("rijbewijs") == "Nee":
                    verhaal.append("Dat u geen rijbewijs heeft, doet niet ter zake.")
                elif keuzes.get("rijbewijs") == "Ja":
                    verhaal.append("Uw rijbewijs is helaas niet geldig voor onze winkelwagens, want die bestaan niet.")

                verhalen.append(" ".join(verhaal))

            # Algemene afsluiting
            afsluiting = (
                "Op dit moment hebben wij echter alleen neongele opvouwbare winkelwagens van gerecycled WC-papier, "
                "vooral om de stikstofcrisis niet negatief te beïnvloeden. In dat kader zullen we daarom uw bestelling "
                "persoonlijk naar u toe komen duwen, en dat kan even duren, want de fabrikant zit op een van de 17.000 eilanden in Indonesië, "
                "en wij weten nog niet welke."
            )

            # Sla de bestelling op
            st.session_state.bestellingen.append({
                "producten": [item["product"] for item in st.session_state.winkelwagen],
                "totaal": sum(float(item["prijs"].replace("€", "").replace(",", ".").replace("/maand", "")) for item in st.session_state.winkelwagen),
                "status": "Niet verzonden",
                "verhalen": verhalen,
                "afsluiting": afsluiting
            })
            st.session_state.winkelwagen = []

            # Toon de verhalen
            st.success("Gefeliciteerd! U hebt afgerekend. Hier is het verhaal van uw bestelling:")
            for v in verhalen:
                st.info(v)
            st.info(afsluiting)
# ============================================================
# TAB: MIJN WINKELWAGEN / BESTELLINGEN
# ============================================================
with tab_bestellingen:
    st.header("📦 Mijn winkelwagen/mandje/mandje op wieletjes")

    if not st.session_state.bestellingen:
        st.info("U hebt nog niets besteld. En dat is precies de bedoeling.")
    else:
        for i, bestelling in enumerate(st.session_state.bestellingen):
            with st.expander(f"Bestelling #{i+1} — {bestelling['status']}"):
                st.write(f"**Producten:** {', '.join(bestelling['producten'])}")
                st.write(f"**Totaal:** €{bestelling['totaal']:.2f}")
                st.write(f"**Status:** {bestelling['status']}")
                st.write("**Het verhaal van uw bestelling:**")
                for v in bestelling["verhalen"]:
                    st.write(v)
                st.info(bestelling["afsluiting"])

        st.markdown("---")
        st.caption("Al uw bestellingen zijn niet verzonden. Dat is precies wat u van ons kunt verwachten.")

# ============================================================
# TAB 2: OVER ONS
# ============================================================
with tab_over:
    st.header("📖 Over ons")
    st.write("""
    **Wie zijn wij?**
    Wij stellen ons niet voor. Eigenlijk stellen wij zelfs niets voor.

    **Wat doen wij?**
    Wij laten u in de waan dat u iets koopt. En hoe weten wij als geen ander hoe lekker, veilig en cozy die waan kan zijn. Heerlijk lekker even nergens aan denken. Wie wilt dat nou niet? Niemand dus. Je weet dat het waan is, maar toch is het even lekker om je erin te wentelen. Daar zorgen wij dag en nacht voor. Wij staan met onns hele team 24/7 paraat om u te dienen. 

    **Waarom?**
    Omdat u zonder die waan misschien wel zou beseffen dat u niets nodig hebt. En dat kunnen wij niet hebben. De waan is zacht en de waarheid hard en soms stekelig. Dat is niets voor u! En in dit geval: Wij bieden u dat Niets, waar u zo naar verlangt. Want het Niets schet ruimte voor mooie nieuwe toekomstpersectieven, en die willen we allemaal!

    **Waarom wij?**
    Omdat u alles al hebt. En omdat wij het enige schenken, weliswaar tegen een kleine vergoeding, dat u nog niet hebt: niets. Wist u dat het middelpunt van alles eigenlijk niets is? Stelt u zich voor dat u een kleine portie van dat niets kunt bemachtigen! Dan bent u ineens het middelpunt waar alles om draait. Waarom wij dat voor u willen bereiken? Wij hebben van onze hobby ons beroep gemaakt. Het voelt helemaal niet als werken. En dat is het ook niet.  
    """)

    st.markdown("---")
    st.subheader("Ons team")
    st.image("static/teamfoto.jpg")
    st.caption("*Wij stellen ons niet voor. Eigenlijk stellen wij zelfs niets voor. Maar we hebben wel een teamfoto. En daar zijn we trots op.*")
# ============================================================
# TAB 3: INNOVATIE
# ============================================================
with tab_innovatie:
    st.header("💡 Innovatie")
    st.write("""
    Heeft u ooit wel eens gehoord van een lege zak waar u niets in kan doen? Wij wel.
    
    Onze productenlijn bezit expres geen handleiding, omdat ze allemaal intuïtief niet te bedienen zijn. R&D heeft letterlijk 40 jaar onderzoek gedaan naar hoe elk product geen handeiding behoeft. Ze kwamen er eigenlijk niet uit. Ze werden er hopeloos van. Het ziekteverzuim was in die tijd erg hoog, tegen de 100%. Soms zelfs daar een klein beetje overheen. Maar een net aangenomen stagaire die even tijdelijk in een inrichting was opgenomen na haar eerste werkdag, kwam met de briljante spontane uitspraak: Niets is leuk! En wij dachten gelijk: Gelijk heeft ze, niets is het allerleukst! En dat verkoopt nog niemand! Dus wij aan de slag, en we hebben haar uiteraard een leuk bedankkaartje gestuurd ook. Waarop ze uitschreeuwde: ik heb om niets gevraagd. En toen was de cirkel rond. Ee hebben haar niets gegeven, en eindelijk was ze tevreden! Dit was een keerpunt in ons denken. En wat we voor haar hebben gedaan willen we nu graag voor iedereen doen die het nodig heeft. Want: het kan gewoon wel! Niets is wel degelijk mogelijk!

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

    st.markdown("---")

    st.subheader("🚀 Toekomstplannen: Het Mondiale Buizensysteem")
    st.write("""
    Momenteel richten wij al onze aandacht op het verbeteren van de service, en het leveren van bestellingen zonder daarvoor chauffeurs en bijbehorende voertuigen in te zetten.

    We leggen nu een mondiaal netwerk aan van een buissysteem, waarbij elk huis zal worden aangesloten. Het pakketdienstprincipe gebruikt geen energie, maar maakt gebruik van de draaiing van de aarde om haar as. Deze draait aan het aardoppervlak en vlak daaronder ongeveer 200 kilometer per seconde, en in de buis is een ontmagnetiseerd vacuüm, waardoor het product blijft stilstaan, terwijl het in feite zoef—in een seconde 200 kilometer verder is door het intelligente buizensysteem, wat uitkomt bij uw brievenbus.

    Wanneer we de gehele globe hebben omspannen, is onze roll-out compleet en zult u daarvan bericht krijgen, zodat uw bestelling nog accurater niet wordt geleverd, maar de echte aandacht wordt gegeven die het verdient.
    """)

    st.info("Let op: dit buizensysteem is nog in ontwikkeling. De verwachte opleverdatum is het jaar 3000. Tot die tijd blijven wij uw bestellingen op de oude, vertrouwde manier niet leveren.")

    st.markdown("---")
    st.subheader("⏳ Gisteren bestellen, en onbezorgd blijven")

    st.write("""
    Momenteel voeren we een poll uit met een nieuw systeem om gisteren al te kunnen bestellen. 
    Deze geavanceerde techniek houdt in dat u gisteren een bestelling had kunnen doen, die automatisch 
    verwerkt wordt tot een order. Deze orders worden dan geplaatst tussen de orders van morgen en die 
    van eergisteren. En de orders van vandaag verplaatsen we dan ook naar gisteren. Op die manier is 
    gisteren vandaag geworden.

    Juridisch gezien is dat beter en ook voor de klant geeft het meer transparantie, doorzichtelijkheid 
    en helderheid omtrent de status 'onbezorgd' zijn. Maakt u dus geen zorgen! Wij denken overal aan.

    Maar nu is aan u de vraag: bent u voor of tegen? Stemt u ook even mee? U bent waarschijnlijk de eerste!
    """)

    # Poll logica
    if "poll_stem" not in st.session_state:
        st.session_state.poll_stem = None
    if "genegeerde_stemmen" not in st.session_state:
        st.session_state.genegeerde_stemmen = 0
    if "uitgebrachte_stemmen" not in st.session_state:
        st.session_state.uitgebrachte_stemmen = 0

    keuze = st.radio(
        "Bent u voor of tegen het nieuwe 'gisteren bestellen'-systeem?",
        ["Voor", "Tegen", "Onthouding"],
        key="poll_keuze"
    )

    if st.button("Stem", key="poll_stem_knop"):
        st.session_state.poll_stem = keuze
        st.session_state.uitgebrachte_stemmen += 1
        
        # Elke stem wordt genegeerd, dus de teller gaat omhoog
        st.session_state.genegeerde_stemmen += 1
        
        st.success(
            f"U hebt gestemd: **{keuze}**. Bedankt voor uw stem! "
            f"U bent de eerste stemmer. En waarschijnlijk ook de laatste. "
            f"Wij zullen uw stem meenemen in onze overwegingen, die wij gisteren al hebben afgerond."
        )

    # Toon de statistieken
    st.markdown("---")
    st.subheader("📊 Poll resultaten")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Uitgebrachte stemmen", value=st.session_state.uitgebrachte_stemmen)
    with col2:
        st.metric(label="Genegeerde stemmen", value=st.session_state.genegeerde_stemmen)
        
    if st.session_state.uitgebrachte_stemmen > 0:
        st.caption("100% van de stemmen is genegeerd. Dat noemen wij transparantie.")
    else:
        st.caption("Er zijn nog geen stemmen genegeerd. Wees de eerste!")
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
    Vergeet niet: als u nu iets hebt gekocht, moet u eerst iets wegdoen in huis. Want anders past uw aankoop er niet bij. En het staat in onze algemene voorwaarden. We moeten dit streng controleren en handhaven, anders komt er nooit wat van terecht. We behandelen daaro iedere klant als een fraudeur in de dop. Om te bewijzen dat u geen fraudeur bent, en daadwerkelijk aan de voorwaarde vodoet om niets te ontvangen, vragen wij u het volgende: 

    1. Upload een video van iets wat u daadwerkelijk uit huis gooit, 
    2. Stop het weggeooide spul in een gesloten vuilniszak, 
    3. Laat de camera te allen tijde gericht op de vuilniszak totdat hij in de vuilnisauto verdwijnt.
    4. Gebruik geen accu's maar stroom uit een stopcontact, of gebruik uw aggregaat.
    5. Laat een tijdcode meelopen in het beeld.
    6. Zet de camera niet te dicht naast de aggrgaat (het geluid wordt niet gebruikt maar een aggrgaat overstemt alle gesprekken die u in huis voert, en soms is het wel graig om even mee te luisteren).
    7. Zeg tegen uw huisgeoten om niet ontbloot voor de camera langs te lopen, want dat zien we als een afleidingsmanouvre, waardoor u sowieso al niet aan de voorwaarden voldoet om de aankoop door te laten gaan.
    8. Wees er zeker van dat er geen honden tegen de vuilnisak aan plassen. Dit is verder geen voorwaarde met consekwenties, maar meer een tip onzerzijds naar uw kant.   

    **Onze regels:**
    - Video van ten minste **72 uur** in HD
    - Beschrijving van elke gebeurtenis in **foutloos Latijn**
    - **Geen montage**
    - Minimaal **300GB**
    - Mocht er een paar minuten missen van het beeld, dan beschouwen wij dat als verdacht, en kan de aankoo niet doorgaan

    Ons team zal elke video twee keer bekijken om er zeker van te zijn dat u niet fraudeert. Hartelijk dank voor uw aandacht, en veel succes met uw video!
    """)

    st.subheader("Na goedkeuring")
    st.write("Als uw video wordt goedgekeurd, beloven wij **zo langzaam mogelijk** niets toe te sturen. Wij streven ernaar dit binnen een redelijke termijn te doen. Maar zoals u van ons gewend bent, kan dat even duren. Als uw ongeduld te groot wordt, en u stelt allerlei vragen, dan wordt u beslist en definitief overgelagen.")

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

# ============================================================
# TAB 8: RETOURNEREN
# ============================================================
with tab_retour:
    st.header("🔄 Retourneren")
    st.write("**Wij nemen geen retour in ontvangst, of u moet niets hebben geretourneerd.** In dat geval maken wij daar geen probleem van.")

    st.write("Mocht u toch iets willen retourneren, dan geven wij hierbij **niet** ons adres. Zet linksboven in de hoek **niet** ter attentie van wie u het wilt sturen.")

    st.write("Ons team bepaalt zelf of het retourpakket iets is waar ze iets mee moeten, maar waarschijnlijk hoort u nooit meer van ons.")

# ============================================================
# TAB 9: NIEUWSBRIEF
# ============================================================
with tab_nieuwsbrief:
    st.header("📧 Nieuwsbrief")
    st.write("""
    Heeft u daar ook zo last van? Abonnementen op nieuwsbrieven die eindeloos veel aandacht vragen?

    Abonneer dan nu gelijk op onze nieuwsbrief, en wij sturen u helemaal niets op, zelfs geen lege mail. Hoewel sommige lieden binnen ons bedrijf een lege mail veel correcter vinden, zullen we ons voorlopig behoeden om een vermoeiende nieuwsbrief neer te pennen.

    En om het nou aan AI te vragen, dat is slecht voor het milieu. Dus nee: u krijgt geen nieuwsbrief, maar kunt zich er wel op abonneren.
    """)

    if st.button("Abonneer u op de nieuwsbrief"):
        st.success("Gefeliciteerd! U bent abonnee. U ontvangt niets. U kunt zich op elk moment afmelden, maar dat hoeft niet, want u ontvangt toch niets.")

st.markdown("---")
st.caption(f"Totaal aantal producten: {len(producten['producten'])} · Allemaal even afwezig.")
