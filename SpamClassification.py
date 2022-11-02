# Importando librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('spam_ham_dataset.csv')

print(dataset.head())

# Eliminación de la columna unnamed que no será utilizada
dataset.drop('Unnamed: 0', axis=1, inplace = True)
dataset.columns = ['label', 'email', 'class']

print(dataset.head())

# Revisión de datos faltantes y tamaño del dataset
print(dataset.isna().sum())
print(dataset.shape)