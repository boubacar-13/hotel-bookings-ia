import streamlit as st
import requests

# Configuration de la page
st.set_page_config(
    page_title="Hotel Bookings Status",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Contenu de l'onglet pour l'application web existante
def app_hotel_api():
     # Titre de la page
     st.title("Bienvenue sur l'API Réservations d'Hôtels")

     # Description de l'API
     st.markdown("""
     ### Cette API permet de prédire si un client va annuler sa réservation d'hôtel.

     **Endpoints disponibles :**
     - `/training` : Entraînement du modèle.
     - `/predict` : Prédictions avec le modèle.

     **Exemples de requêtes :**
     - **Training** :
     ```json
     {
          "feature1": 10,
          "feature2": 20
     }
     ```
     - **Predict** :
     ```json
     {
          "no_of_adults": 2,
          "no_of_children": 1,
          "no_of_weekend_nights": 2,
          "no_of_week_nights": 3,
          "required_car_parking_space": 1,
          "lead_time": 100,
          "arrival_year": 2023,
          "arrival_month": 7,
          "arrival_date": 15,
          "repeated_guest": 0,
          "no_of_previous_cancellations": 0,
          "no_of_previous_bookings_not_canceled": 1,
          "avg_price_per_room": 150.0,
          "no_of_special_requests": 2
     }
     ```
     """)

# Contenu de l'onglet pour l'API d'hôtel
def app_web():
    st.header('Votre client va t-il annuler sa réservation ?', divider='rainbow')
    st.subheader('Vérifier le en quelques secondes !')
    # Formulaire
    with st.form(key='mon_formulaire'):

     st.header("Informations sur la réservation")
     # Nombre d'adultes
     no_of_adults = st.number_input('Nombre d\'adultes', min_value=0, max_value=10, value=1)

     # Nombre d'enfants
     no_of_children = st.number_input('Nombre d\'enfants', min_value=0, max_value=10, value=0)

     # Nombre de nuits de week-end
     no_of_weekend_nights = st.number_input('Nombre de nuits de week-end', min_value=0, value=0)

     # Nombre de nuits en semaine
     no_of_week_nights = st.number_input('Nombre de nuits en semaine', min_value=0, value=1)

     st.header("Préférences et historique du client")
     # Place de parking requise
     required_car_parking_space = st.number_input('Place de parking requise', min_value=0, value=0)

     # Délai avant arrivée
     lead_time = st.number_input('Délai avant arrivée (en jours)', min_value=0, value=0)

     # Année d'arrivée
     arrival_year = st.number_input('Année d\'arrivée', min_value=2015, max_value=2025, value=2022)

     # Mois d'arrivée
     arrival_month = st.selectbox('Mois d\'arrivée', options=range(1, 13))

     # Date d'arrivée
     arrival_date = st.number_input('Date d\'arrivée', min_value=1, max_value=31, value=1)

     # Client répété
     repeated_guest = st.selectbox('Client répété', options=['Non', 'Oui'])

     st.header("Historique des réservations")
     # Nombre d'annulations précédentes
     no_of_previous_cancellations = st.number_input('Nombre d\'annulations précédentes', min_value=0, value=0)

     # Nombre de réservations précédentes non annulées
     no_of_previous_bookings_not_canceled = st.number_input('Nombre de réservations précédentes non annulées', min_value=0, value=0)

     # Prix moyen par chambre
     avg_price_per_room = st.number_input('Prix moyen par chambre', min_value=0.0, value=100.0)

     # Nombre de demandes spéciales
     no_of_special_requests = st.number_input('Nombre de demandes spéciales', min_value=0, value=0)

     soumis = st.form_submit_button('Soumettre')

     if soumis:
          # Convertir les données en un format compatible avec la requête
          data = {
               "no_of_adults": no_of_adults,
               "no_of_children": no_of_children,
               "no_of_weekend_nights": no_of_weekend_nights,
               "no_of_week_nights": no_of_week_nights,
               "required_car_parking_space": required_car_parking_space,
               "lead_time": lead_time,
               "arrival_year": arrival_year,
               "arrival_month": arrival_month,
               "arrival_date": arrival_date,
               "repeated_guest": 1 if repeated_guest == 'Oui' else 0,
               "no_of_previous_cancellations": no_of_previous_cancellations,
               "no_of_previous_bookings_not_canceled": no_of_previous_bookings_not_canceled,
               "avg_price_per_room": avg_price_per_room,
               "no_of_special_requests": no_of_special_requests
          }

          # Envoi de la requête
          response = requests.post('http://127.0.0.1:8000/predict', json=data)

          # Vérification de la réponse HTTP
          if response.status_code == 200:
               result = response.json()
               prediction = result['Prediction']

               # Affichage de la phrase finale en fonction de la prédiction
               if prediction == '0':
                    st.success("Le client a de fortes chances de maintenir sa réservation 🎉")
               else:
                    st.error("Il y a des risques que le client annule sa réservation 😢")

          else:
               st.error(f"Erreur lors de la requête!!!!! : {response.status_code} - {response.text}")

# Menu de sélection des onglets
selected_app = st.sidebar.selectbox(
    "Sélectionnez l'application :",
    ("Application Web", "API Hotel Reservations")
)

# Afficher l'onglet sélectionné
if selected_app == "Application Web":
    app_web()
elif selected_app == "API Hotel Reservations":
    app_hotel_api()