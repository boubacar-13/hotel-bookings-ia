# Installation des dépendances
pip install -r requirements.txt

# Démarage de l'API
python -m uvicorn api:app --reload

# Démarrage de la web app
streamlit run app_web.py