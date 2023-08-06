# create Macine learning pipeline

import pandas as pd
from sklearn.model_selection import  train_test_split
import math
from sklearn.preprocessing import StandardScaler,MinMaxScaler


# import libraries for regression model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor,BaggingRegressor,ExtraTreesRegressor
from sklearn.linear_model import (Lasso,ElasticNet,Ridge,PassiveAggressiveRegressor,ARDRegression,RANSACRegressor,
TheilSenRegressor,HuberRegressor,Lars,LassoLars,SGDRegressor,BayesianRidge,LinearRegression,OrthogonalMatchingPursuit)
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


class Regressor:
    def __init__(self, X, Y, test_size=0.2, random_state=42,scaler=None):
        self.X=X
        self.Y=Y
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size=test_size, random_state=random_state)
        self.scaler=scaler
        self.model =[LinearRegression(),Ridge(),Lasso(),ElasticNet(),SGDRegressor(),
                    KNeighborsRegressor(),DecisionTreeRegressor(),RandomForestRegressor(),
                    AdaBoostRegressor(),XGBRegressor(),GradientBoostingRegressor(),TheilSenRegressor(),
                    RANSACRegressor(),HuberRegressor(),SVR(),
                    ARDRegression(),BayesianRidge(),BaggingRegressor(),ExtraTreesRegressor()]

        self.model_name=['LinearRegression','Ridge','Lasso','ElasticNet','SGDRegressor','KNeighborsRegressor','decisiontreeregressor',
                        'RandomForestRegressor','AdaBoostRegressor','XGBRegressor','GradientBoostingRegressor','TheilSenRegressor',
                        'RANSACRegressor','HuberRegressor','SVR',
                        'ARDRegression','BayesianRidge','BaggingRegressor','ExtraTreesRegressor']

        self.model_table=[]
        # self.model_score=[]


    def model_accuracy(self,y_test,y_pred,model_name,model_obj):
        mse=mean_squared_error(y_test, y_pred)
        rmse=math.sqrt(mse)
        mae=mean_absolute_error(y_test, y_pred)
        r2=r2_score(y_test, y_pred)
        return {'model':model_name,'MSE':mse,'RMSE':rmse,'MAE':mae,'r2':r2,'model_obj':model_obj}

    def model_training(self):
        if self.scaler =='standard':
            self.scaler=StandardScaler()
            self.scaler.fit(self.X_train)
            self.X_train=self.scaler.transform(self.X_train)
            self.X_test=self.scaler.transform(self.X_test)
        elif self.scaler =='minmax':
            self.scaler=MinMaxScaler()
            self.scaler.fit(self.X_train)
            self.X_train=self.scaler.transform(self.X_train)
            self.X_test=self.scaler.transform(self.X_test)
        else:
            pass

        lst=[]
        for m, m_n in zip(self.model,self.model_name):
            model=m.fit(self.X_train, self.Y_train)
            Y_pred=model.predict(self.X_test)
            lst.append(self.model_accuracy(self.Y_test, Y_pred,m_n,model))
        self.model_table=pd.DataFrame(lst)
        return self.model_table

    def linear_regression(self):
        model=LinearRegression().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'LinearRegression',model)
    
    def ridge_regression(self):
        model=Ridge().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'Ridge',model)
    
    def lasso_regression(self):
        model=Lasso().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'Lasso',model)
    
    def elastic_net_regression(self):
        model=ElasticNet().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'ElasticNet',model)
    
    def sgd_regression(self):
        model=SGDRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'SGDRegressor',model)
    
    def kneighbors_regression(self):
        model=KNeighborsRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'KNeighborsRegressor',model)
    
    def decision_tree_regression(self):
        model=DecisionTreeRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'decisiontreeregressor',model)
    
    def random_forest_regression(self):
        model=RandomForestRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'RandomForestRegressor',model)
    
    def ada_boost_regression(self):
        model=AdaBoostRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'AdaBoostRegressor',model)
    
    def xgboost_regression(self):
        model=XGBRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'XGBRegressor',model)
    
    def gradient_boosting_regression(self):
        model=GradientBoostingRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'GradientBoostingRegressor',model)
    
    def theilsen_regression(self):
        model=TheilSenRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'TheilSenRegressor',model)
    
    def ransac_regression(self):
        model=RANSACRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'RANSACRegressor',model)
    
    def lasso_lars_regression(self):
        model=LassoLars().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'LassoLars',model)
    
    def lars_regression(self):
        model=Lars().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'Lars',model)
    
    def orthogonal_regression(self):
        model=OrthogonalMatchingPursuit().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'OrthogonalMatchingPursuit',model)
    
    def huber_regression(self):
        model=HuberRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'HuberRegressor',model)
    
    def svr(self):
        model=SVR().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'SVR',model)
    
    def passive_aggressive_regression(self):
        model=PassiveAggressiveRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'PassiveAggressiveRegressor',model)
    
    def ard_regression(self):
        model=ARDRegression().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'ARDRegression',model)
    
    def bayesian_ridge_regression(self):
        model=BayesianRidge().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'BayesianRidge',model)
    
    def bagging_regression(self):
        model=BaggingRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'BaggingRegressor',model)
    
    def extra_trees_regression(self):
        model=ExtraTreesRegressor().fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'ExtraTreesRegressor',model)
        
    

            
