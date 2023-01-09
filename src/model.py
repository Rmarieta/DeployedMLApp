import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.linear_model import LinearRegression


if __name__=="__main__" :

    boston=load_boston()

    dataset=pd.DataFrame(boston.data,columns=boston.feature_names)

    dataset['price']=boston.target
    X=dataset.iloc[:,:-1]
    y=dataset.iloc[:,-1]

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

    std_scaler=StandardScaler()

    X_train=std_scaler.fit_transform(X_train)

    X_test=std_scaler.transform(X_test)

    pickle.dump(std_scaler,open('scaling.pkl','wb'))

    reg=LinearRegression()
    reg.fit(X_train,y_train)
    reg_pred=reg.predict(X_test)
    residuals=y_test-reg_pred

    pickle.dump(reg,open('model.pkl','wb'))
    # to load the model 
    model=pickle.load(open('model.pkl','rb'))