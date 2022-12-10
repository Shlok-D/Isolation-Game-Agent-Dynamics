import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import multioutput
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR

class Prediction():
    def __init__(self) -> None:
        df = pd.read_csv("Data4x4.csv")
        train1 = df.drop(['CX','CY'],axis=1)
        test1 = df[['CX','CY']] 

        X_train1, X_test1, y_train1, y_test1 = train_test_split(train1, test1, test_size=0.2, random_state=4)

        self.regr2 = MultiOutputRegressor(SVR())
        self.regr2.fit(X_train1.values,y_train1)

    def predict(self,a1,a2,b1,b2,s):
        Xn1 = [[a1,a2,s]]
        pred = self.regr2.predict(Xn1)
        print(round(pred[0][0]),round(pred[0][1]),pred)

i = Prediction()
i.predict(1,1,2,1,1)