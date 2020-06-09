import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_selection import SelectFromModel
dataset=pd.read_csv(r'/content/dataset.csv')
x=dataset.iloc[:,1:4].values
y=dataset.iloc[:,4:].values
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
x[:,0]=lb.fit_transform(x[:,0])
feat_labels=['week','checkout_price','base_price']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
from joblib import dump
dump(sc,"scalar.save")
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='entropy',random_state=0)
dt.fit(x_train,y_train)
import pickle
pickle.dump(dt,open('model.pkl','wb'))