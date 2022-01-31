# -*- coding: utf-8 -*-
"""
@author: William J. Wakefield

Data: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

def main():
    
    wine = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, random_state=1)
    rf = RandomForestRegressor(n_estimators=100)
    rf.fit(X_train, y_train)
    metrics = open("metrics.txt", "w")
    print("Score of RandomForestRegression on Wine Data: {:.3f}".format(rf.score(X_test, y_test)), file=metrics)

    y_pred = rf.predict(X_test)
    rf_MAE = mean_absolute_error(y_test, y_pred)
    print("Mean Absolute Error:", rf_MAE, file=metrics)

    rf_MSE = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", rf_MSE, file=metrics)
    metrics.close()

if __name__ == "challenge-3":
    main()