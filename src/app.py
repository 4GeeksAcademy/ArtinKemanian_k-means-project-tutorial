from utils import db_connect
engine = db_connect()

# your code here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from pickle import dump

datos = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/k-means-project-tutorial/main/housing.csv")

datos = datos.drop_duplicates()
datos = datos.dropna()
datos = datos.drop(["HouseAge","AveRooms","AveBedrms","Population","AveOccup","MedHouseVal"],axis=1)

datos_train, datos_test = train_test_split(datos, test_size = 0.2, random_state = 42)

modelo_unsup = KMeans(n_clusters = 6, n_init = "auto", random_state = 42)
modelo_unsup.fit(datos_train)

y_train = list(modelo_unsup.labels_)
datos_train["cluster"] = y_train

y_test = list(modelo_unsup.predict(datos_test))
datos_test["cluster"] = y_test

modelo_sup = DecisionTreeClassifier(random_state = 42)
modelo_sup.fit(datos_train, y_train)

y_pred = modelo_sup.predict(datos_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

dump(modelo_unsup, open("models/k-means_default_42.sav", "wb"))
dump(modelo_sup, open("models/decision_tree_classifier_default_42.sav", "wb"))