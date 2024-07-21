import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
import optuna
from utils import load_datasets, preprocess_data

# Definición del modelo
class NutritionalRecommendationModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NutritionalRecommendationModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Función objetivo para Optuna
def objective(trial):
    # Carga y preprocesamiento de datos
    datasets = load_datasets()
    df = pd.concat([datasets['dataset1'], datasets['dataset2'], datasets['dataset3'], datasets['dataset4']])
    df = preprocess_data(df)

    # Preparar datos para entrenamiento
    X = df.drop(columns=['target_column'])  # Reemplaza 'target_column' con la columna de tu objetivo
    y = df['target_column']  # Reemplaza 'target_column' con la columna de tu objetivo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Sugerir hiperparámetros
    input_size = X_train.shape[1]
    hidden_size = trial.suggest_int('hidden_size', 32, 128)
    output_size = 1  # Ajusta según sea necesario
    num_epochs = trial.suggest_int('num_epochs', 50, 200)
    learning_rate = trial.suggest_loguniform('learning_rate', 1e-4, 1e-2)

    # Crear el modelo, definir la función de pérdida y el optimizador
    model = NutritionalRecommendationModel(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Entrenamiento del modelo
    for epoch in range(num_epochs):
        model.train()
        outputs = model(torch.FloatTensor(X_train.values))
        loss = criterion(outputs, torch.FloatTensor(y_train.values).view(-1, 1))
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Evaluación del modelo
    model.eval()
    with torch.no_grad():
        outputs = model(torch.FloatTensor(X_test.values))
        loss = criterion(outputs, torch.FloatTensor(y_test.values).view(-1, 1))

    return loss.item()

# Optimización de hiperparámetros con Optuna
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)

# Imprimir mejores hiperparámetros
print('Best hyperparameters: ', study.best_params)

# Entrenar el modelo final con los mejores hiperparámetros
def train_final_model():
    best_params = study.best_params
    hidden_size = best_params['hidden_size']
    num_epochs = best_params['num_epochs']
    learning_rate = best_params['learning_rate']
    
    datasets = load_datasets()
    df = pd.concat([datasets['dataset1'], datasets['dataset2'], datasets['dataset3'], datasets['dataset4']])
    df = preprocess_data(df)

    X = df.drop(columns=['target_column'])  # Reemplaza 'target_column' con la columna de tu objetivo
    y = df['target_column']  # Reemplaza 'target_column' con la columna de tu objetivo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    input_size = X_train.shape[1]
    output_size = 1  # Ajusta según sea necesario

    model = NutritionalRecommendationModel(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        model.train()
        outputs = model(torch.FloatTensor(X_train.values))
        loss = criterion(outputs, torch.FloatTensor(y_train.values).view(-1, 1))
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    torch.save(model.state_dict(), 'saved_model/nutritional_recommendation_model.pth')

if __name__ == '__main__':
    train_final_model()
