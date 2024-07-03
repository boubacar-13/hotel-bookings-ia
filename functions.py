from sklearn.tree import DecisionTreeClassifier
#import api


# Fonction pour entraîner le modèle à partir des données d'entraînement
#def train_model(training_data: api.TrainingData):
def train_model(training_data):
    # Importation locale pour éviter l'importation globale
    from api import TrainingData  
    # Exemple d'entraînement d'un modèle DecisionTreeClassifier avec cikit-learn
    X_train = [[training_data.feature1, training_data.feature2]]  
    # Format des données d'entraînement
    y_train = [0]  # Exemple de cibles (classes) d'entraînement
    model = DecisionTreeClassifier()  # Initialisation du modèle
    model.fit(X_train, y_train)  # Entraînement du modèle sur les données d'entraînement
    return model

