import streamlit as st
import requests

# Configuration de la page
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Form
with st.form(key='my_form'):
    # no_of_adults
    no_of_adults = st.number_input('No of Adults', min_value=0, max_value=10, value=1)

    # no_of_children
    no_of_children = st.number_input('No of Children', min_value=0, max_value=10, value=0)

    # no_of_weekend_nights
    no_of_weekend_nights = st.number_input('No of Weekend Nights', min_value=0, value=0)

    # no_of_week_nights
    no_of_week_nights = st.number_input('No of Week Nights', min_value=0, value=1)

    # required_car_parking_space
    required_car_parking_space = st.number_input('Required Car Parking Space', min_value=0, value=0)

    # lead_time
    lead_time = st.number_input('Lead Time', min_value=0, value=0)

    # arrival_year
    arrival_year = st.number_input('Arrival Year', min_value=2015, max_value=2025, value=2022)

    # arrival_month
    arrival_month = st.selectbox('Arrival Month', options=range(1, 13))

    # arrival_date
    arrival_date = st.number_input('Arrival Date', min_value=1, max_value=31, value=1)

    # repeated_guest
    repeated_guest = st.selectbox('Repeated Guest', options=['No', 'Yes'])

    # no_of_previous_cancellations
    no_of_previous_cancellations = st.number_input('No of Previous Cancellations', min_value=0, value=0)

    # no_of_previous_bookings_not_canceled
    no_of_previous_bookings_not_canceled = st.number_input('No of Previous Bookings Not Canceled', min_value=0, value=0)

    # avg_price_per_room
    avg_price_per_room = st.number_input('Average Price Per Room', min_value=0.0, value=100.0)

    # no_of_special_requests
    no_of_special_requests = st.number_input('No of Special Requests', min_value=0, value=0)

    submitted = st.form_submit_button('Submit')

    if submitted:
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
            "repeated_guest": 1 if repeated_guest == 'Yes' else 0,
            "no_of_previous_cancellations": no_of_previous_cancellations,
            "no_of_previous_bookings_not_canceled": no_of_previous_bookings_not_canceled,
            "avg_price_per_room": avg_price_per_room,
            "no_of_special_requests": no_of_special_requests
        }

        # Envoi de la requête
        response = requests.post('http://127.0.0.1:8000/predict', json=data)

        # Affichage de la réponse
        st.write(response.text)
