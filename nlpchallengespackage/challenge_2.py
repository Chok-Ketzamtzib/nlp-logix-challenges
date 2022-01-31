# -*- coding: utf-8 -*-
"""
@author: William J. Wakefield

Data: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris

def main():
    
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=1)

    forest = RandomForestClassifier(n_estimators=5, random_state=0)
    forest.fit(X_train, y_train)

    accuracy_train = forest.score(X_train, y_train)
    accuracy_test = forest.score(X_test, y_test)

    metrics = open("metrics.txt", "w")

    print("Accuracy on training set: {:.3f}".format(accuracy_train), file=metrics)
    print("Accuracy on test set: {:.3f}".format(accuracy_test), file=metrics)

    pred_randforest = forest.predict(X_test)

    confusion = confusion_matrix(y_test, pred_randforest)
    print("Confusion Matrix:\n{}".format(confusion), file=metrics)
    metrics.close()
    
if __name__ == "challenge-2":
    main()