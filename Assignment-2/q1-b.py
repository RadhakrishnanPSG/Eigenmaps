from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix
import pytest


def test():
#load dataset
    iris = load_iris()
    
    #train test split
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2)
    
    
    model = LogisticRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    
    #calculating quality metrics
    accuracy = accuracy_score(y_test,y_pred)
    precision = precision_score(y_test, y_pred,average="weighted")
    recall = recall_score(y_test, y_pred,average="weighted")
    confusion_mat = confusion_matrix(y_test, y_pred)
    assert accuracy>0.9
    assert precision>0.8
    
    
    print("Accuracy of the model : ",accuracy)
    print("Precision of the model : ",precision)
    print("Recall of the model : ",recall)
    print("Confusion matrix : \n",confusion_mat)
    
test()