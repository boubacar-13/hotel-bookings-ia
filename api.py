import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np
import functions as f

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
    title="API Réservations d'Hôtels",
    openapi_tags=tags_metadata,
    description="""   
    Pouvez-vous prédire si le client va annuler la réservation ?
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
    avg_price_per_room: float
    no_of_special_requests: int

class TrainingData(BaseModel):
    feature1: int
    feature2: int

# Route de base
@app.get("/", tags=["Text"])
def home():
    return {
        "message": "Bienvenue sur l'API Réservations d'Hôtels",
        "description": "Cette API permet de prédire si un client va annuler sa réservation d'hôtel.",
        "endpoints": {
            "/training": "Endpoint POST pour l'entraînement du modèle.",
            "/predict": "Endpoint POST pour faire des prédictions avec le modèle.",
            "/docs": "Accédez à la documentation complète de l'API."
        },
        "examples": {
            "training": {
                "method": "POST",
                "url": "/training",
                "body": {
                    "feature1": 10,
                    "feature2": 20
                }
            },
            "predict": {
                "method": "POST",
                "url": "/predict",
                "body": {
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
            }
        }
    }

# Endpoint POST pour l'entraînement du modèle
@app.post("/training")
def training_endpoint(training_data: TrainingData):
    try:
        # Entraîner le modèle à partir des données d'entraînement
        trained_model = f.train_model(training_data)
        # Sauvegarder le modèle entraîné dans un fichier
        with open('modele_decision_tree.pkl', 'wb') as file:
            pickle.dump(trained_model, file)
        return {"message": "Modèle entraîné avec succès"}
    except Exception as e:
        # Capturez les erreurs et renvoyez une réponse d'erreur appropriée
        raise HTTPException(status_code=500, detail=str(e))

# Route pour effectuer les prédictions
@app.post("/predict", tags=["Predict"])
def predict(data: Data):
    try:
        # Chargement du modèle pré-entraîné
        model = joblib.load('modele_decision_tree.pkl')

        # Conversion des données d'entrée en format approprié pour le modèle
        input_data = np.array([[
            data.no_of_adults,
            data.no_of_children,
            data.no_of_weekend_nights,
            data.no_of_week_nights,
            data.required_car_parking_space,
            data.lead_time,
            data.arrival_year,
            data.arrival_month,
            data.arrival_date,
            data.repeated_guest,
            data.no_of_previous_cancellations,
            data.no_of_previous_bookings_not_canceled,
            data.avg_price_per_room,
            data.no_of_special_requests
        ]])

        # Prédiction à l'aide du modèle chargé
        pred = model.predict(input_data)

        return {"Prediction": str(pred[0])}
    except Exception as e:
        # Capturez les erreurs et renvoyez une réponse d'erreur appropriée
        raise HTTPException(status_code=500, detail=str(e))
