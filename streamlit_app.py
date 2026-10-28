import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Configuration de la page Streamlit
# ---------------------------------------------------------
st.set_page_config(
    page_title="Suivi de Chantier - Immeuble R+2 Yaoundé",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style personnalisé CSS (Couleurs & Thème)
st.markdown("""
    <style>
    .main-header { font-size: 28px; font-weight: bold; color: #1E293B; margin-bottom: 5px; }
    .sub-header { font-size: 15px; color: #64748B; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# En-tête du Projet
# ---------------------------------------------------------
st.markdown('<div class="main-header">Immeuble R+2 à Yaoundé (exemple)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">📍 Yaoundé, quartier Bastos | Construction d\'un immeuble résidentiel R+2 : fondations, élévation des murs, dalles béton et finitions.</div>', unsafe_allow_html=True)

# Top Cards Informatives
col_top1, col_top2, col_top3, col_top4 = st.columns(4)
with col_top1:
    st.metric(label="Avancement Global", value="43 %")
with col_top2:
    st.metric(label="Début du Chantier", value="01/07/2026")
with col_top3:
    st.metric(label="Fin Prévue", value="28/02/2027")
with col_top4:
    st.metric(label="Budget Total", value="45 000 000 FCFA")

st.divider()

# ---------------------------------------------------------
# Onglets Principaux (Navigation)
# ---------------------------------------------------------
tab_phases, tab_rapports, tab_journal, tab_simulation = st.tabs([
    "📋 Phases du Chantier", 
    "📊 Suivi & Rapports (Graphiques)", 
    "📓 Journal de Chantier", 
    "🧮 Simulation Directe"
])

# =========================================================
# TAB 1: PHASES DU CHANTIER
# =========================================================
with tab_phases:
    st.subheader("Phases d'Exécution du Projet")
    
    phases_data = [
        {"Phase": "Terrassement et implantation", "Type": "Terrassement", "Statut": "Terminé", "Echéance": "20/07/2026", "Progrès": 100},
        {"Phase": "Fondations (semelles et longrines)", "Type": "Fondations", "Statut": "En cours", "Echéance": "10/09/2026", "Progrès": 90},
        {"Phase": "Élévation du rez-de-chaussée", "Type": "Gros œuvre", "Statut": "En cours", "Echéance": "30/11/2026", "Progrès": 55},
        {"Phase": "Dalle du 1er étage", "Type": "Gros œuvre", "Statut": "En cours", "Echéance": "20/12/2026", "Progrès": 10},
        {"Phase": "Élévation des étages et toiture", "Type": "Gros œuvre", "Statut": "À faire", "Echéance": "10/02/2027", "Progrès": 0},
        {"Phase": "Menuiserie, peinture et finitions", "Type": "Finitions", "Statut": "À faire", "Echéance": "28/02/2027", "Progrès": 0},
    ]

    for item in phases_data:
        col_p1, col_p2 = st.columns([3, 1])
        with col_p1:
            st.markdown(f"**{item['Phase']}** — *{item['Type']}* ({item['Statut']})")
            st.caption(f"Échéance : {item['Echéance']}")
            st.progress(item['Progrès'] / 100)
        with col_p2:
            st.markdown(f"### {item['Progrès']}%")
        st.write("---")

# =========================================================
# TAB 2: SUIVI & RAPPORTS (GRAPHIQUES PYTHON)
# =========================================================
with tab_rapports:
    st.subheader("Analyses d'Études & Indicateurs Clés")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Budget Consommé", "18.9 M FCFA", "Budget Total: 45 M FCFA")
    m2.metric("Retard Accumulé", "6 jours", "Météo / Approvisionnement")
    m3.metric("Taux d'Avancement réel", "43 %", "Prévu: 45 %")
    m4.metric("Sécurité (Jours sans accident)", "74 jours", "Objectif: 100%")

    st.divider()

    st.markdown("#### 1. Avancement Réel vs Planifié par Phase")
    df_avancement = pd.DataFrame({
        "Phase": ["Terrassement", "Fondations", "Rez-de-chaussée", "Dalle 1er étage", "Élévation Étages", "Finitions"],
        "Réel (%)": [100, 90, 55, 10, 0, 0],
        "Planifié (%)": [100, 100, 70, 25, 0, 0]
    })
    
    fig_prog = px.bar(
        df_avancement, x="Phase", y=["Réel (%)", "Planifié (%)"],
        barmode="group",
        color_discrete_sequence=["#EA580C", "#94A3B8"],
        height=350
    )
    fig_prog.update_layout(margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_prog, use_container_width=True)

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("#### 2. Consommation des Fluides")
        df_fluides = pd.DataFrame({
            "Mois": ["Juil", "Août", "Sept", "Oct"],
            "Eau (m³)": [55, 60, 42, 51],
            "Électricité (kWh)": [620, 680, 600, 760],
            "Carburant (L)": [200, 220, 180, 100]
        })
        st.dataframe(df_fluides, use_container_width=True)

    with col_g2:
        st.markdown("#### 3. Gestion des Déchets de Chantier")
        df_dechets = pd.DataFrame({
            "Type": ["Gravois / Béton", "Bois de coffrage", "Ferraille", "Sacs de ciment"],
            "Quantité (t)": [17.5, 3.2, 0.8, 1.2],
            "Filière": ["Remblai", "Réutilisation / Recyclage", "Recyclage", "Décharge publique"]
        })
        fig_dechets = px.pie(
            df_dechets, values="Quantité (t)", names="Type", 
            title="Répartition des Déchets (Tonnes)",
            color_discrete_sequence=px.colors.sequential.Oranges_r
        )
        st.plotly_chart(fig_dechets, use_container_width=True)

    st.divider()

    st.markdown("#### 4. Analyse Statistiques Python - Contrôle Qualité")
    fig_mpl, ax = plt.subplots(figsize=(8, 3))
    categories = ['Qualité', 'Béton', 'Infiltration', 'Thermographie', 'Équipements']
    conformes = [8, 5, 3, 2, 4]
    non_conformes = [1, 0, 1, 1, 0]
    x = np.arange(len(categories))
    width = 0.35

    ax.bar(x - width/2, conformes, width, label='Conformes', color='#10B981')
    ax.bar(x + width/2, non_conformes, width, label='Non Conformes', color='#EF4444')
    ax.set_ylabel('Nombre de Contrôles')
    ax.set_title('Rapport de Synthèse Qualité par Domaine')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig_mpl)

# =========================================================
# TAB 3: JOURNAL DE CHANTIER
# =========================================================
with tab_journal:
    st.subheader("Journal des Activités Récentes")
    journal_items = [
        {"titre": "Coulage des poteaux du RDC", "date": "09/10/2026", "meteo": "☀️ Ensoleillé", "ouvriers": "18 ouvriers", "desc": "Les poteaux du rez-de-chaussée ont été coulés ce matin."},
        {"titre": "Livraison de ciment", "date": "06/10/2026", "meteo": "⛅ Nuageux", "ouvriers": "15 ouvriers", "desc": "Réception de 200 sacs de ciment. Stock sécurisé sous bâche."},
        {"titre": "Ralentissement dû aux pluies", "date": "02/10/2026", "meteo": "🌧️ Pluvieux", "ouvriers": "12 ouvriers", "desc": "Fortes pluies en début de semaine : maçonnerie ralentie."}
    ]
    for j in journal_items:
        with st.container():
            st.markdown(f"### {j['titre']}")
            st.caption(f"🗓️ {j['date']} | {j['meteo']} | 👷 {j['ouvriers']}")
            st.write(j['desc'])
            st.divider()

# =========================================================
# TAB 4: SIMULATION DIRECTE DU CHANTIER
# =========================================================
with tab_simulation:
    st.subheader("🧮 Simulateur de Budget, Météo et Effectifs (Cameroun)")
    st.info("Paramétrez ci-dessous les coûts unitaires, les intempéries et l'équipe dédiée sur le chantier de Yaoundé.")

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("##### ⚙️ Paramètres Généraux & Matériaux")
        cout_ciment = st.slider("Prix du sac de ciment (FCFA)", min_value=4000, max_value=8000, value=5000, step=100)
        retard_pluie = st.slider("Jours d'arrêt dus aux intempéries (jours)", min_value=0, max_value=60, value=20)
        gestion_dechets_cout = st.slider("Budget traitement/évacuation déchets (FCFA)", min_value=100000, max_value=2000000, value=700000, step=50000)

        st.markdown("##### 👷 Gestion des Effectifs & Salaires Journaliers")
        
        col_eff1, col_eff2 = st.columns(2)
        with col_eff1:
            nb_chef = st.number_input("Nombre Chef de chantier", min_value=0, value=1)
            nb_ferrailleur = st.number_input("Nombre de Ferrailleurs", min_value=0, value=4)
            nb_coffreur = st.number_input("Nombre de Coffreurs", min_value=0, value=6)
        with col_eff2:
            cout_chef = st.number_input("Coût/jour Chef (FCFA)", value=15000)
            cout_ferrailleur = st.number_input("Coût/jour Ferrailleur (FCFA)", value=7000)
            cout_coffreur = st.number_input("Coût/jour Coffreur (FCFA)", value=6000)

    with col_s2:
        st.markdown("##### 📊 Résultats de la Simulation")
        
        # Calculs automatiques
        masse_salariale_journaliere = (nb_chef * cout_chef) + (nb_ferrailleur * cout_ferrailleur) + (nb_coffreur * cout_coffreur)
        budget_initial = 45000000
        
        # Surcoût lié aux jours d'arrêt où l'équipe est maintenue ou payée / impact de productivité
        surcout_meteo = retard_pluie * masse_salariale_journaliere
        
        # Variation du coût du ciment (base 10 000 sacs estimés pour le projet)
        total_sacs_estime = 10000
        variation_ciment = (cout_ciment - 5000) * total_sacs_estime

        budget_simule = budget_initial + surcout_meteo + variation_ciment + (gestion_dechets_cout - 350000)

        st.metric(label="Masse Salariale Journalière Globale", value=f"{masse_salariale_journaliere:,} FCFA".replace(",", " "))
        st.metric(label="Surcoût total des 20 jours d'intempéries", value=f"{surcout_meteo:,} FCFA".replace(",", " "))
        st.metric(label="Budget Initial", value=f"{budget_initial:,} FCFA".replace(",", " "))
        st.metric(
            label="Budget Révisé Estimé", 
            value=f"{int(budget_simule):,} FCFA".replace(",", " "),
            delta=f"{int(budget_simule - budget_initial):,} FCFA".replace(",", " "),
            delta_color="inverse"
        )

    st.markdown("---")
    st.markdown("##### 📈 Projection Graphique de la Consommation Budgétaire")
    
    x_months = ["Mois 1 (Juil)", "Mois 2 (Août)", "Mois 3 (Sept)", "Mois 4 (Oct)", "Mois 5 (Nov)", "Mois 6 (Déc)", "Mois 7 (Jan)", "Mois 8 (Fév)"]
    cumul_prev = np.linspace(5000000, budget_initial, len(x_months))
    cumul_sim = np.linspace(5000000, budget_simule, len(x_months))

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(x=x_months, y=cumul_prev, mode='lines+markers', name='Budget Initial Prévu', line=dict(color='#94A3B8', dash='dash')))
    fig_sim.add_trace(go.Scatter(x=x_months, y=cumul_sim, mode='lines+markers', name='Budget Simulé avec Effectifs & Météo', line=dict(color='#EA580C', width=3)))

    fig_sim.update_layout(title="Trajectoire Financière du Projet (Simulateur Yaoundé)", yaxis_title="FCFA", height=350)
    st.plotly_chart(fig_sim, use_container_width=True)
