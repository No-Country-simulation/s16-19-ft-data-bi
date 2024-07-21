# Importa funciones y clases específicas de los submódulos
from .train_model import train_final_model, NutritionalRecommendationModel

# Define qué funciones y clases estarán disponibles al importar el paquete
__all__ = [
    'train_final_model',
    'NutritionalRecommendationModel',
    # Se debería agregar cualquier otra función o clase que se quiera exportar
]
