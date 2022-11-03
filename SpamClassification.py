# Importando librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from googletrans import Translator

# Importar el dataset
datasetInicial = pd.read_csv('spam_ham_dataset.csv')
traductor = Translator()

#print(datasetInicial.head())

# Eliminación de la columna unnamed que no será utilizada
#columnaAux = []
#for i in range(len(datasetInicial)):
#    print(traductor.translate(str(datasetInicial['text'].at[i]), dest='es').text)


dataset = datasetInicial['text'].apply(lambda x: traductor.translate(x, dest='es').text)
#datasetInicial.drop('Unnamed: 0', axis=1, inplace = True)
#datasetInicial.columns = ['label', 'mail', 'class']



print(dataset.head())

# Revisión de datos faltantes y tamaño del dataset
#print(dataset.isna().sum())
#print(dataset.shape)