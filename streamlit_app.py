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

# Style personnalisé CSS
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
    "🧮 Simulation Directe (Cameroun)"
])

# =========================================================
# TAB 1: PHASES DU CHANTIER
# =========================================================
with tab_phases:
    st.subheader("Phases d'Exécution du Projet")
    phases_data = [
        {"Phase": "Terrassement et implantation", "Type": "Terrassement", "Statut": "Terminé", "Echéance": "20/07/2026", "Progrès": 100},
        {"Phase": "Fondations (semelles et longrines)", "Type": "Fondations", "Statut": "Terminé", "Echéance": "10/09/2026", "Progrès": 100},
        {"Phase": "Élévation du rez-de-chaussée", "Type": "Gros œuvre", "Statut": "En cours", "Echéance": "30/11/2026", "Progrès": 55},
        {"Phase": "Dalle du 1er étage", "Type": "Gros œuvre", "Statut": "En cours", "À faire": "20/12/2026", "Progrès": 0},
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
    fig_prog = px.bar(df_avancement, x="Phase", y=["Réel (%)", "Planifié (%)"], barmode="group", color_discrete_sequence=["#EA580C", "#94A3B8"], height=350)
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
        fig_dechets = px.pie(df_dechets, values="Quantité (t)", names="Type", title="Répartition des Déchets (Tonnes)", color_discrete_sequence=px.colors.sequential.Oranges_r)
        st.plotly_chart(fig_dechets, use_container_width=True)

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
# TAB 4: SIMULATION DIRECTE DU CHANTIER (VALEURS FIXES)
# =========================================================
with tab_simulation:
    st.subheader("🧮 Simulation Directe du Chantier (Yaoundé)")
    st.info("Cette section présente la simulation financière officielle basée sur les paramètres fixes du projet (prix du ciment, intempéries, effectifs et gestion des déchets).")

    # Valeurs figées demandées
    PRIX_CIMENT = 5000
    JOURS_INTEMPERIES = 20
    BUDGET_DECHETS = 700000

    # Effectifs et coûts fixes
    effectifs_data = [
        {"Rôle": "Chef de chantier", "Nombre": 1, "Coût unitaire journalier": 15000},
        {"Rôle": "Ferrailleurs", "Nombre": 4, "Coût unitaire journalier": 7000},
        {"Rôle": "Coffreurs", "Nombre": 6, "Coût unitaire journalier": 6000},
    ]
    df_effectifs = pd.DataFrame(effectifs_data)

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("##### 📌 Paramètres Fixes de la Simulation")
        st.markdown(f"- **Prix unitaire du ciment :** {PRIX_CIMENT:,} FCFA / sac".replace(",", " "))
        st.markdown(f"- **Jours d'arrêt intempéries :** {JOURS_INTEMPERIES} jours")
        st.markdown(f"- **Budget évacuation des déchets :** {BUDGET_DECHETS:,} FCFA".replace(",", " "))
        
        st.markdown("##### 👷 Équipe & Effectifs Fixés sur le Chantier")
        st.dataframe(df_effectifs, use_container_width=True, hide_index=True)

    with col_s2:
        st.markdown("##### 📊 Résultats & Impact Financier")
        
        # Calcul automatique de la masse salariale journalière
        masse_salariale_jour = sum(row["Nombre"] * row["Coût unitaire journalier"] for _, row in df_effectifs.iterrows())
        surcout_meteo = JOURS_INTEMPERIES * masse_salariale_jour
        
        budget_initial = 45000000
        budget_simule = budget_initial + surcout_meteo + BUDGET_DECHETS

        st.metric(label="Masse Salariale Journalière", value=f"{masse_salariale_jour:,} FCFA".replace(",", " "))
        st.metric(label="Surcoût lié aux 20 jours d'intempéries", value=f"{surcout_meteo:,} FCFA".replace(",", " "))
        st.metric(label="Budget Initial", value=f"{budget_initial:,} FCFA".replace(",", " "))
        st.metric(
            label="Budget Révisé Simulé", 
            value=f"{int(budget_simule):,} FCFA".replace(",", " "),
            delta=f"+{int(budget_simule - budget_initial):,} FCFA".replace(",", " "),
            delta_color="inverse"
        )

    st.markdown("---")
    st.markdown("##### 📈 Projection Graphique de la Trajectoire Budgétaire")
    
    x_months = ["Mois 1 (Juil)", "Mois 2 (Août)", "Mois 3 (Sept)", "Mois 4 (Oct)", "Mois 5 (Nov)", "Mois 6 (Déc)", "Mois 7 (Jan)", "Mois 8 (Fév)"]
    cumul_prev = np.linspace(5000000, budget_initial, len(x_months))
    cumul_sim = np.linspace(5000000, budget_simule, len(x_months))

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(x=x_months, y=cumul_prev, mode='lines+markers', name='Budget Initial Prévu', line=dict(color='#94A3B8', dash='dash')))
    fig_sim.add_trace(go.Scatter(x=x_months, y=cumul_sim, mode='lines+markers', name='Budget Simulé (Fixe)', line=dict(color='#EA580C', width=3)))
    fig_sim.update_layout(title="Évolution Comparée du Budget (Simulation Yaoundé)", yaxis_title="FCFA", height=350)
    st.plotly_chart(fig_sim, use_container_width=True)
