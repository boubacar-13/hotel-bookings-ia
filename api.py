import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier
import joblib
from joblib import dump, load
import numpy as np
import functions as f
from functions import train_model  

# Définition des métadonnées pour les tags OpenAPI
tags_metadata = [
    {
        "name": "Text",
        "description": "Operations with text data.",
    },
    {
        "name": "Predict",
        "description": "Operations with prediction models.",
    }
]

# Initialisation de l'application FastAPI
app = FastAPI(
    title="API Hotel Reservations",
    openapi_tags=tags_metadata,
    description="""   
    Can you predict if customer is going to cancel the reservation ?
    """,
)


# Définition de la classe pour les données d'entrée
class Data(BaseModel):
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    required_car_parking_space: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int
    avg_price_per_room: int
    no_of_special_requests: int

class TrainingData(BaseModel):
    feature1: int
    feature2: int

# Route de base
@app.get("/", tags=["Text"])
def home():
    return {"message": "Page d'accueil API Hotel Reservation."}

# Endpoint POST pour l'entraînement du modèle
@app.post("/training")
def training_endpoint(training_data: TrainingData):
    try:
        # Entraîner le modèle à partir des données d'entraînement
        trained_model = f.train_model(training_data)
        # Sauvegarder le modèle entraîné dans un fichier
        with open('modele_decision_tree.pkl', 'wb') as file:
            pickle.dump(trained_model, file)
        return {"message": "Model trained successfully"}
    except Exception as e:
        # Capturez les erreurs et renvoyez une réponse d'erreur appropriée
        raise HTTPException(status_code=500, detail=str(e))
    
# Route pour effectuer les prédictions
@app.post("/predict", tags=["Numbers"])
def predict(data: Data):

    # Chargement du modèle pré-entraîné
    model = joblib.load('modele_decision_tree.pkl')

    data = data.dict()
    data = list(data.values())

    pred = model.predict([data]) > 0.5

    return {"Prediction"  : str(pred[0][0])}
