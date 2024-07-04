contact : boubacar.timera@efrei.net
date : 03/07/2024

---

# Hotel Reservations Analysis and API

This project focuses on the analysis of hotel reservations data to extract meaningful insights and the development of an API to serve the results of the analysis.

## Project Structure

- `Notebook_Hotel_Reservations.ipynb`: Jupyter notebook containing the data preparation and analysis.
- `api.py`: Contains the FastAPI app with endpoints to interact with the analysis results.
- `app_web.py`: A web application to display the analysis results in a user-friendly manner.
- `Documentation.py`: Provides detailed documentation of the project's functionality and API endpoints.
- `functions.py`: Helper functions used across the project for various tasks like data processing and analysis.
- `requirements.txt`: Lists all the Python packages that need to be installed to run this project.
- `run.sh`: Shell script to install dependencies and start the API server.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running the following command in your terminal:

```shell
./run.sh

---

## Données

Utilisez les données qui sont dans le github. Si jamais vous n'y arrivez pas, vous pouvez récupérer les données en cliquant sur ("https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset").

**Descriptif des données :**
The file contains the different attributes of customers' reservation details. The detailed data dictionary is given below.

Booking_ID: unique identifier of each booking
no_of_adults: Number of adults
no_of_children: Number of Children
no_of_weekend_nights: Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
no_of_week_nights: Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
type_of_meal_plan: Type of meal plan booked by the customer:
required_car_parking_space: Does the customer require a car parking space? (0 - No, 1- Yes)
room_type_reserved: Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.
lead_time: Number of days between the date of booking and the arrival date
arrival_year: Year of arrival date
arrival_month: Month of arrival date
arrival_date: Date of the month
market_segment_type: Market segment designation.
repeated_guest: Is the customer a repeated guest? (0 - No, 1- Yes)
no_of_previous_cancellations: Number of previous bookings that were canceled by the customer prior to the current booking
no_of_previous_bookings_not_canceled: Number of previous bookings not canceled by the customer prior to the current booking
avg_price_per_room: Average price per day of the reservation; prices of the rooms are dynamic. (in euros)
no_of_special_requests: Total number of special requests made by the customer (e.g. high floor, view from the room, etc)
booking_status: Flag indicating if the booking was canceled or not.


## WEB APP
Des professionnels du secteurs de l'hôtellerie pourront utiliser cet outil et prédire le taux de remplissage de leurs hôtels.
P.S : Pour vérifier que l'outil fonctionne, on peut juste modifier le prix. Ex essayer avec 100€ puis avec 300€. Dans le premier cas, le client maintiendrait sa résa, dans le second, il l'annulera.
```
