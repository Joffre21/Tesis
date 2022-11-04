# Importando librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from googletrans import Translator

# Importar el dataset
datasetInicial = pd.read_csv('spam_ham_dataset.csv')
traductor = Translator()

print(datasetInicial.head())


transMail = datasetInicial['text'].apply(lambda x: traductor.translate(x, dest='es').text)
dataset = datasetInicial
dataset.insert(1, 'correo', transMail)
dataset.drop('Unnamed: 0', axis=1, inplace = True)
dataset.columns = ['correoES', 'label', 'mailEN', 'class']

print(dataset.head())

# Revisión de datos faltantes y tamaño del dataset
print(dataset.isna().sum())
print(dataset.shape)

# For Text processing 
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

# Cleaning the texts

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('spanish')) 

dataset['correoES'] = dataset['correoES'].apply(lambda x: ' '.join([ word for word in word_tokenize(x)  if not word in stop_words]))

X = dataset.loc[:, 'correoES']
y =dataset.loc[:, 'class'].values

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()

X=cv.fit_transform(X).toarray()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm1 = confusion_matrix(y_test, y_pred)

print('Accuracy: ', accuracy_score(y_test, y_pred) * 100)

import seaborn as sns
plt.figure(figsize = (10, 10))
sns.heatmap(cm1,annot = True, fmt="n", xticklabels=['Not Spam', 'Spam'], yticklabels=['Not Spam', 'Spam'])

from sklearn.ensemble import RandomForestClassifier
cl=RandomForestClassifier()
cl.fit(X_train, y_train)

# Predicting the Test set results
y_pred = cl.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm2 = confusion_matrix(y_test, y_pred)
print('Accuracy: ', accuracy_score(y_test, y_pred) * 100)