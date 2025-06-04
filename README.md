Modelos de Regresión (50%)

1. Uso de Librerías (10%)

Importar y utilizar correctamente:

import pandas as pd
import numpy as np
from sklearn import model_selection, metrics, linear_model, svm, tree

2. División del Dataset (10%)

Usar train_test_split con una partición estándar (ej: 80/20 o 70/30):

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

3. Entrenamiento de Modelos (10%)

Entrenar y comparar al menos 3 modelos de regresión:

Regresión Lineal (LinearRegression)

Árbol de Decisión (DecisionTreeRegressor)

Support Vector Regression (SVR)

4. Evaluación de Métricas (10%)

Calcular para cada modelo:

R² (Coef. de determinación)

MAE

MSE

RMSE

Mostrar resultados en texto y gráfico.

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

Seleccionar el mejor modelo justificando la elección.

🔍 Modelos de Clasificación (50%)

5. Entrenamiento de Modelos (10%)

Entrenar y comparar al menos 3 modelos de clasificación:

Regresión Logística (LogisticRegression)

Support Vector Machine (SVC)

Árbol de Decisión (DecisionTreeClassifier)

Ajustar hiperparámetros usando GridSearchCV o RandomizedSearchCV.

6. Evaluación de Métricas (10%)

Evaluar los modelos usando:

Accuracy

F1 Score

Matriz de confusión (texto y gráfico)

from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

Seleccionar el mejor modelo según métricas e interpretación.

📃 Variables y Agrupaciones Sugeridas

Datos de entrada:

X1: contiene todas las columnas para regresión.

Y1: variable continua (target para regresión).

X2, Y2: datos para clasificación. Y2 es categórica.

Posibles agrupaciones de variables:

Kills, Plata, Equipo, Valor

Armas → agrupadas por funciones (ej: letalidad)

Hipótesis (Opcional pero Recomendado)

Evaluar 3 configuraciones distintas de entrada o agrupación de datos.

💡 Tips Adicionales

Documentar cada paso con comentarios.

Usar visualizaciones para interpretar resultados.

Mostrar gráficos comparativos entre modelos.

Justificar siempre la selección del mejor modelo.