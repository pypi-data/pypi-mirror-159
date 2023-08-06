# import requered libraries for classifier

import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.linear_model import LogisticRegression,RidgeClassifier,SGDClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier,BaggingClassifier,ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import RandomizedSearchCV


# define classifier class
class Classifier:   
    # define classifier constructor
    def __init__(self, X,Y,test_size=0.2,random_state=20,scaler=None):
        self.X=X
        self.Y=Y
        # split x and y
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X,Y, test_size = test_size,stratify=Y, random_state=random_state)
        self.scaler=scaler
        self.model=[LogisticRegression(),KNeighborsClassifier(),GaussianNB()
                    ,BaggingClassifier(),ExtraTreesClassifier(),
                    RidgeClassifier(),SGDClassifier(),RandomForestClassifier(),
                    xgb.XGBClassifier(),AdaBoostClassifier(),BernoulliNB(),GradientBoostingClassifier(),DecisionTreeClassifier(),SVC()]

        self.model_name=['Logistic Regression','KNeighborsClassifier','GaussianNB',
                'BaggingClassifier','ExtraTreesClassifier','RidgeClassifier','SGDClassifier',
                'RandomForestClassifier','XGBClassifier','AdaBoostClassifier',
                'BernoulliNB','GradientBoostingClassifier','DecisionTreeClassifier','SVC']
        self.model_table=[]
        self.mod=[]
    

    def model_accuracy(self,y_test_f,y_pred_f,model_name,model_obj):
        acc=accuracy_score(y_test_f, y_pred_f)
        confusion=confusion_matrix(y_test_f, y_pred_f)
        roc=roc_auc_score(y_test_f, y_pred_f)
        f1=f1_score(y_test_f, y_pred_f)
        recall=recall_score(y_test_f, y_pred_f)
        precision=precision_score(y_test_f, y_pred_f)
        return {'model name':model_name,'accuracy':acc,'confusion':confusion,'roc':roc,'f1':f1,'recall':recall,'precision':precision,'model object':model_obj}
    
    # define function to model training

    def model_training(self):
        if self.scaler=='standard':
            sc_scaler=StandardScaler()
            sc_scaler.fit(self.X_train)
            self.X_train=sc_scaler.transform(self.X_train)
            self.X_test=sc_scaler.transform(self.X_test)
        elif self.scaler=='minmax':
            m_scaler=MinMaxScaler()
            m_scaler.fit(self.X_train)
            self.X_train=m_scaler.transform(self.X_train)
            self.X_test=m_scaler.transform(self.X_test)
        else:
            pass
        # model
        lst=[]
        for m, m_n in zip(self.model,self.model_name):
            model=m.fit(self.X_train, self.Y_train)
            Y_pred=model.predict(self.X_test)
            lst.append(self.model_accuracy(self.Y_test, Y_pred,m_n,model))
        self.model_table=pd.DataFrame(lst)
        return self.model_table
    
    # function for single model prediction
    def logistic_regression(self):
        model=LogisticRegression()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'logistic regression',model)
    
    def kneighbors_classifier(self):
        model=KNeighborsClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'kneighbors classifier',model)
    
    def gaussian_nb(self):
        model=GaussianNB()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'gaussian nb',model)
    
    def bagging_classifier(self):
        model=BaggingClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'bagging classifier',model)
    
    def extra_trees_classifier(self):
        model=ExtraTreesClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'extra trees classifier',model)
    
    def ridge_classifier(self):
        model=RidgeClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'ridge classifier',model)
    
    def sgd_classifier(self):
        model=SGDClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'sgd classifier',model)
    
    def random_forest_classifier(self):
        model=RandomForestClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'random forest classifier',model)
    
    def xgb_classifier(self):
        model=xgb.XGBClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'xgb classifier',model)
    
    def ada_boost_classifier(self):
        model=AdaBoostClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'ada boost classifier',model)
    
    def bernoulli_nb(self):
        model=BernoulliNB()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'bernoulli nb',model)
    
    def gradient_boosting_classifier(self):
        model=GradientBoostingClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'gradient boosting classifier',model)
    
    def decision_tree_classifier(self):
        model=DecisionTreeClassifier()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'decision tree classifier',model)
        

    def svc(self):
        model=SVC()
        model.fit(self.X_train, self.Y_train)
        Y_pred=model.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'svc',model)

    
    # Hyperparameter tuning
    def hyperparameter_tuning(self):
        # logistic
        model=LogisticRegression()
        param_grid={
            'C':[0.1,1,10,100,1000],
            'penalty':['l2'],
            'tol':[1e-3,1e-4,1e-5,1e-6,1e-7,1e-8,1e-9,1e-10],
            'fit_intercept':[True,False],
            'intercept_scaling':[1,10,100,1000],
            'class_weight':['balanced',None],
            'solver':['newton-cg','lbfgs','sag','saga'],
            'max_iter':[100,200,300,400,500,600,700,800,900,1000],
            'n_jobs':[-1],
            'random_state':[10,11,12,20,30,40,42],
            'warm_start':[True,False],
            'verbose':[0,1,2,3,4,5,6,7,8,9,10],
            'multi_class':['ovr','multinomial','auto'],
            'l1_ratio':[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],

            }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=5,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst=[]
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'logistic regression',grid_search))

        # knn
        model=KNeighborsClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'n_neighbors':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'weights':['uniform','distance'],
            'algorithm':['auto','ball_tree','kd_tree','brute'],
            'leaf_size':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'p':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'metric':['euclidean','manhattan','chebyshev','minkowski'],
            # 'metric_params':[{'p':2},{'p':3},{'p':4},{'p':5}],
            'n_jobs':[-1],
        }            
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'knn',grid_search))   

        # gaussian naive bayes
        model=GaussianNB()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'var_smoothing':[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000],
            'priors':[None,0.25,0.5,0.75,1],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'gaussian naive bayes',grid_search))
        
        # Bernoulli naive bayes
        model=BernoulliNB()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'alpha':[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2],
            'binarize':[0,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000],
            'class_prior':[None,0.25,0.5,0.75,1],
            'fit_prior':[None,True,False],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'bernoulli naive bayes',grid_search))

        # bagging classifier
        # model=BaggingClassifier()
        # cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        # param_grid={
        #     'n_estimators':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        #     'max_samples':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
        #     'max_features':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
        #     'bootstrap':[True,False],
        #     'bootstrap_features':[True,False],
        #     'base_estimator':[None,DecisionTreeClassifier(),RandomForestClassifier(),AdaBoostClassifier(),GradientBoostingClassifier(),ExtraTreesClassifier(),KNeighborsClassifier(),GaussianNB(),BernoulliNB(),LogisticRegression(),SVC(),SGDClassifier(),RidgeClassifier(),SGDClassifier(),BaggingClassifier()],
        #     'obb_score':[True,False],
        #     'warm_start':[True,False],
        #     'n_jobs':[-1],
        #     'random_state':[10,11,12,20,30,40,42],
        #     'verbose':[0,1,2,3,4,5,6,7,8,9,10],
        # }
        # grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        # grid_search.fit(self.X_train, self.Y_train)
        # Y_pred=grid_search.predict(self.X_test)
        # lst.append(self.model_accuracy(self.Y_test, Y_pred,'bagging classifier',grid_search))

        # extra trees classifier
        # model=ExtraTreesClassifier()
        # cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        # param_grid={
        #     'n_estimators':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,100],
        #     'max_depth':[None,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        #     'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        #     'min_weight_fraction_leaf':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'max_features':['sqrt','log2',None],
        #     'max_leaf_nodes':[None,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        #     'min_impurity_decrease':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'bootstrap':[True,False],
        #     'oob_score':[True,False],
        #     'warm_start':[True,False],
        #     'n_jobs':[-1,None],
        #     'random_state':[None,10,11,12,20,30,40,42],
        #     'criterion':['gini','entropy'],
        #     'min_samples_split':[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        #     'verbose':[0,1,2,3,4,5,6,7,8,9,10],
        #     'class_weight':['balanced',None],
        #     'ccp_alpha':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'max_samples':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        # }
        # grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        # grid_search.fit(self.X_train, self.Y_train)
        # Y_pred=grid_search.predict(self.X_test)
        # lst.append(self.model_accuracy(self.Y_test, Y_pred,'extra trees classifier',grid_search))




        # ridge classifier
        model=RidgeClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'alpha':[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2],
            'fit_intercept':[True,False],
            'normalize':['deprecated','scale','center'],
            'copy_X':[True,False],
            'max_iter':[None,10,100,1000,10000,100000,1000000,10000000],
            'tol':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
            'solver':['auto','svd','cholesky','lsqr','sparse_cg','sag','saga'],
            'random_state':[None,10,11,12,20,30,40,42],
            'positive':[True,False],
            'class_weight':['balanced',None],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'ridge classifier',grid_search))

        # sgd classifier
        # class sklearn.linear_model.SGDClassifier(loss='hinge', *, penalty='l2', alpha=0.0001, l1_ratio=0.15, 
        # fit_intercept=True, max_iter=1000, tol=0.001, shuffle=True, verbose=0, epsilon=0.1, n_jobs=None, random_state=None, 
        # learning_rate='optimal', eta0=0.0, power_t=0.5, early_stopping=False, validation_fraction=0.1, n_iter_no_change=5, 
        # class_weight=None, warm_start=False, average=False)
        # model=SGDClassifier()
        # cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        # param_grid={
        #     'loss':['hinge','log','modified_huber','squared_hinge','perceptron'],
        #     'penalty':['l2','l1','elasticnet'],
        #     'alpha':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
        #     'l1_ratio':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95],
        #     'fit_intercept':[True,False],
        #     'max_iter':[None,10,100,1000,10000,100000,1000000,10000000],
        #     'tol':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
        #     'shuffle':[True,False],
        #     'verbose':[0,1,2,3,4,5,6,7,8,9,10],
        #     'epsilon':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
        #     'n_jobs':[-1,None],
        #     'random_state':[None,10,11,12,20,30,40,42],
        #     'learning_rate':['optimal','constant','invscaling','adaptive'],
        #     'eta0':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'power_t':[0.5,0.6,0.7,0.8,0.9,1.0],
        #     'early_stopping':[True,False],
        #     'validation_fraction':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'n_iter_no_change':[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
        #     'class_weight':['balanced',None],
        #     'warm_start':[True,False],
        #     'average':[True,False],
        # }
        # grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        # grid_search.fit(self.X_train, self.Y_train)
        # Y_pred=grid_search.predict(self.X_test)
        # lst.append(self.model_accuracy(self.Y_test, Y_pred,'sgd classifier',grid_search))


        # random forest classifier
        # class sklearn.ensemble.RandomForestClassifier(n_estimators=100, *, criterion='gini', 
        # max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
        # max_features='sqrt', max_leaf_nodes=None, min_impurity_decrease=0.0, bootstrap=True, 
        # oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None)[source]
        # model=RandomForestClassifier()
        # cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        # param_grid={
        #     'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
        #     'criterion':['gini','entropy'],
        #     'max_depth':[None,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
        #     'min_samples_split':[2,3,4,5,6,7,8,9,10],
        #     'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10],
        #     'min_weight_fraction_leaf':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'max_features':['sqrt','log2'],
        #     'max_leaf_nodes':[None,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
        #     'min_impurity_decrease':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'bootstrap':[True,False],
        #     'oob_score':[True,False],
        #     'n_jobs':[-1,None],
        #     'random_state':[None,10,11,12,20,30,40,42],
        #     'verbose':[0,1,2,3,4,5,6,7,8,9,10],
        #     'warm_start':[True,False],
        #     'class_weight':['balanced',None],
        #     'ccp_alpha':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'max_samples':[None,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
        # }
        # grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        # grid_search.fit(self.X_train, self.Y_train)
        # Y_pred=grid_search.predict(self.X_test)
        # lst.append(self.model_accuracy(self.Y_test, Y_pred,'random forest classifier',grid_search))


        # xgboost classifier
        # class xgboost.XGBClassifier(max_depth=3, learning_rate=0.1, n_estimators=100, silent=True,
        # objective='binary:logistic', booster='gbtree', n_jobs=None, n_estimators=100, n_jobs=None,
        # verbose=0, max_delta_step=0, subsample=1, colsample_bytree=1, colsample_bylevel=1,
        # reg_alpha=0, reg_lambda=1, scale_pos_weight=None, base_score=0.5, random_state=0)[source]
        # model=xgb.XGBClassifier()
        # cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        # param_grid={
        #     'max_depth':[3,4,5,6,7,8,9,10],
        #     'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
        #     'silent':[True,False],
        #     'objective':['binary:logistic'],
        #     'booster':['gbtree'],
        #     'n_jobs':[-1,None],
        #     'verbose':[0,1,2,3,4,5,6,7,8,9,10],
        #     'max_delta_step':[0],
        #     'subsample':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'colsample_bytree':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'colsample_bylevel':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'reg_alpha':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'reg_lambda':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        #     'scale_pos_weight':[None],
        #     'base_score':[0.5],
        #     'random_state':[None,10,11,12,20,30,40,42],
        # }
        # grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        # grid_search.fit(self.X_train, self.Y_train)
        # Y_pred=grid_search.predict(self.X_test)
        # lst.append(self.model_accuracy(self.Y_test, Y_pred,'xgboost classifier',grid_search))


        # ada boost classifier
        # class sklearn.ensemble.AdaBoostClassifier(base_estimator=None, *, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
        model=AdaBoostClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
            'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'algorithm':['SAMME.R'],
            'random_state':[None,10,11,12,20,30,40,42],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'ada boost classifier',grid_search))


        # gradient boosting classifier
        # class sklearn.ensemble.GradientBoostingClassifier(*, loss='log_loss', learning_rate=0.1, 
        # n_estimators=100, subsample=1.0, criterion='friedman_mse', min_samples_split=2, 
        # min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, init=None, 
        # random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, warm_start=False, 
        # validation_fraction=0.1, n_iter_no_change=None, tol=0.0001, ccp_alpha=0.0)
        model=GradientBoostingClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'loss':['log_loss'],
            'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
            'subsample':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'criterion':['friedman_mse'],
            'min_samples_split':[2,3,4,5,6,7,8,9,10],
            'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10],
            'min_weight_fraction_leaf':[0.0],
            'max_depth':[3,4,5,6,7,8,9,10],
            'min_impurity_decrease':[0.0],
            'init':[None],
            'random_state':[None,10,11,12,20,30,40,42],
            'max_features':[None],
            'verbose':[0,1,2,3,4,5,6,7,8,9,10],
            'max_leaf_nodes':[None],
            'warm_start':[False],
            'validation_fraction':[0.1],
            'n_iter_no_change':[None],
            'tol':[0.0001],
            'ccp_alpha':[0.0],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'gradient boosting classifier',grid_search))



        # svc
        # class sklearn.svm.SVC(*, C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, 
        # probability=False, tol=0.001, cache_size=200, class_weight=None, 
        # verbose=False, max_iter=- 1, decision_function_shape='ovr', break_ties=False, random_state=None)[source]
        model=SVC()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'C':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'kernel':['rbf'],
            'degree':[3,4,5,6,7,8,9,10],
            'gamma':['scale'],
            'coef0':[0.0],
            'shrinking':[True,False],
            'probability':[True,False],
            'tol':[0.001],
            'cache_size':[200],
            'class_weight':[None],
            'verbose':[True,False],
            'max_iter':[-1],
            'decision_function_shape':['ovr'],
            'break_ties':[True,False],
            'random_state':[None,10,11,12,20,30,40,42],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'svc',grid_search))


        # decision tree classifier
        # class sklearn.tree.DecisionTreeClassifier(*, criterion='gini', splitter='best', max_depth=None, min_samples_split=2, 
        # min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
        # max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0)
        model=DecisionTreeClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'criterion':['gini'],
            'splitter':['best'],
            'max_depth':[None],
            'min_samples_split':[2,3,4,5,6,7,8,9,10],
            'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10],
            'min_weight_fraction_leaf':[0.0],
            'max_features':[None],
            'random_state':[None,10,11,12,20,30,40,42],
            'max_leaf_nodes':[None],
            'min_impurity_decrease':[0.0],
            'class_weight':[None],
            'ccp_alpha':[0.0],
        }
        grid_search=GridSearchCV(model,param_grid,cv=5,n_jobs=-1)
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        lst.append(self.model_accuracy(self.Y_test, Y_pred,'decision tree classifier',grid_search))


    # single hyperparameter tuning for all models
    def logistic_hyperparameter(self):
        model=LogisticRegression()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'C':[0.1,1,10,100,1000],
            'penalty':['l2'],
            'tol':[1e-3,1e-4,1e-5,1e-6,1e-7,1e-8,1e-9,1e-10],
            'fit_intercept':[True,False],
            'intercept_scaling':[1,10,100,1000],
            'class_weight':['balanced',None],
            'solver':['newton-cg','lbfgs','sag','saga'],
            'max_iter':[100,200,300,400,500,600,700,800,900,1000],
            'n_jobs':[-1],
            'random_state':[10,11,12,20,30,40,42],
            'warm_start':[True,False],
            'verbose':[0,1,2,3,4,5,6,7,8,9,10],
            'multi_class':['ovr','multinomial','auto'],
            'l1_ratio':[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],

            }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'logistic regression',grid_search)
    
    # knn hyperparameter
    def knn_hyperparameter(self):
        model=KNeighborsClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'n_neighbors':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'weights':['uniform','distance'],
            'algorithm':['auto','ball_tree','kd_tree','brute'],
            'leaf_size':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'p':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'metric':['euclidean','manhattan','chebyshev','minkowski'],
            # 'metric_params':[{'p':2},{'p':3},{'p':4},{'p':5}],
            'n_jobs':[-1],
        }            
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'knn',grid_search)
    
    # gaussian naive bayes hyperparameter
    def gaussian_nb_hyperparameter(self):
        model=GaussianNB()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'var_smoothing':[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000],
            'priors':[None,0.25,0.5,0.75,1],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'gaussian naive bayes',grid_search)
    
    # bernoulli naive bayes hyperparameter
    def bernoulli_nb_hyperparameter(self):
        model=BernoulliNB()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'alpha':[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2],
            'binarize':[0,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000],
            'class_prior':[None,0.25,0.5,0.75,1],
            'fit_prior':[None,True,False],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'bernoulli naive bayes',grid_search)

    # bagging hyperparameter
    # def bagging_hyperparameter(self):
    #     model=BaggingClassifier()
    #     cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
    #     param_grid={
    #         'n_estimators':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    #         'max_samples':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
    #         'max_features':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
    #         'bootstrap':[True,False],
    #         'bootstrap_features':[True,False],
    #         'base_estimator':[None,DecisionTreeClassifier(),RandomForestClassifier(),AdaBoostClassifier(),GradientBoostingClassifier(),ExtraTreesClassifier(),KNeighborsClassifier(),GaussianNB(),BernoulliNB(),LogisticRegression(),SVC(),SGDClassifier(),RidgeClassifier(),SGDClassifier(),BaggingClassifier()],
    #         # 'obb_score':[True,False],
    #         'warm_start':[True,False],
    #         'n_jobs':[-1],
    #         'random_state':[10,11,12,20,30,40,42],
    #         'verbose':[0,1,2,3,4,5,6,7,8,9,10],
    #     }
    #     grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
    #     grid_search.fit(self.X_train, self.Y_train)
    #     Y_pred=grid_search.predict(self.X_test)
    #     return self.model_accuracy(self.Y_test, Y_pred,'bagging',grid_search)

    # # extra trees hyperparameter
    # def extra_trees_hyperparameter(self):
    #     model=ExtraTreesClassifier()
    #     cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
    #     param_grid={
    #         'n_estimators':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,100],
    #         'max_depth':[None,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    #         'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    #         'min_weight_fraction_leaf':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'max_features':['sqrt','log2',None],
    #         'max_leaf_nodes':[None,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    #         'min_impurity_decrease':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'bootstrap':[True,False],
    #         'oob_score':[True,False],
    #         'warm_start':[True,False],
    #         'n_jobs':[-1,None],
    #         'random_state':[None,10,11,12,20,30,40,42],
    #         'criterion':['gini','entropy'],
    #         'min_samples_split':[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    #         'verbose':[0,1,2,3,4,5,6,7,8,9,10],
    #         'class_weight':['balanced',None],
    #         'ccp_alpha':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'max_samples':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #     }
    #     grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
    #     grid_search.fit(self.X_train, self.Y_train)
    #     Y_pred=grid_search.predict(self.X_test)
    #     return self.model_accuracy(self.Y_test, Y_pred,'extra trees',grid_search)

    # ridge hyperparameter
    def ridge_hyperparameter(self):
        model=RidgeClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'alpha':[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2],
            'fit_intercept':[True,False],
            'normalize':['deprecated','scale','center'],
            'copy_X':[True,False],
            'max_iter':[None,10,100,1000,10000,100000,1000000,10000000],
            'tol':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
            'solver':['auto','svd','cholesky','lsqr','sparse_cg','sag','saga'],
            'random_state':[None,10,11,12,20,30,40,42],
            'positive':[True,False],
            'class_weight':['balanced',None],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'ridge',grid_search)

    # sgd hyperparameter
    # def sgd_hyperparameter(self):
    #     model=SGDClassifier()
    #     cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
    #     param_grid={
    #         'loss':['hinge','log','modified_huber','squared_hinge','perceptron'],
    #         'penalty':['l2','l1','elasticnet'],
    #         'alpha':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
    #         'l1_ratio':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95],
    #         'fit_intercept':[True,False],
    #         'max_iter':[None,10,100,1000,10000,100000,1000000,10000000],
    #         'tol':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
    #         'shuffle':[True,False],
    #         'verbose':[0,1,2,3,4,5,6,7,8,9,10],
    #         'epsilon':[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0],
    #         'n_jobs':[-1,None],
    #         'random_state':[None,10,11,12,20,30,40,42],
    #         'learning_rate':['optimal','constant','invscaling','adaptive'],
    #         'eta0':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'power_t':[0.5,0.6,0.7,0.8,0.9,1.0],
    #         'early_stopping':[True,False],
    #         'validation_fraction':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'n_iter_no_change':[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
    #         'class_weight':['balanced',None],
    #         'warm_start':[True,False],
    #         'average':[True,False],
    #     }
    #     grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
    #     grid_search.fit(self.X_train, self.Y_train)
    #     Y_pred=grid_search.predict(self.X_test)
    #     return self.model_accuracy(self.Y_test, Y_pred,'sgd',grid_search)
    
    # random forest hyperparameter
    # def random_forest_hyperparameter(self):
    #     model=RandomForestClassifier()
    #     cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
    #     param_grid={
    #         'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
    #         'criterion':['gini','entropy'],
    #         'max_depth':[None,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
    #         'min_samples_split':[2,3,4,5,6,7,8,9,10],
    #         'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10],
    #         'min_weight_fraction_leaf':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'max_features':['sqrt','log2'],
    #         'max_leaf_nodes':[None,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
    #         'min_impurity_decrease':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'bootstrap':[True,False],
    #         'oob_score':[True,False],
    #         'n_jobs':[-1,None],
    #         'random_state':[None,10,11,12,20,30,40,42],
    #         'verbose':[0,1,2,3,4,5,6,7,8,9,10],
    #         'warm_start':[True,False],
    #         'class_weight':['balanced',None],
    #         'ccp_alpha':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'max_samples':[None,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
    #     }
    #     grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
    #     grid_search.fit(self.X_train, self.Y_train)
    #     Y_pred=grid_search.predict(self.X_test)
    #     return self.model_accuracy(self.Y_test, Y_pred,'random_forest',grid_search)
    
    # xgboost hyperparameter
    # def xgboost_hyperparameter(self):
    #     model=xgb.XGBClassifier()
    #     cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
    #     param_grid={
    #         'max_depth':[3,4,5,6,7,8,9,10],
    #         'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
    #         # 'silent':[True,False],
    #         # 'objective':['binary:logistic'],
    #         # 'booster':['gbtree'],
    #         # 'n_jobs':[-1,None],
    #         # 'verbose':[0,1,2,3,4,5,6,7,8,9,10],
    #         # 'max_delta_step':[0],
    #         # 'subsample':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         # 'colsample_bytree':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         # 'colsample_bylevel':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'reg_alpha':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         'reg_lambda':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #         # 'scale_pos_weight':[None],
    #         # 'base_score':[0.5],
    #         # 'random_state':[None,10,11,12,20,30,40,42],
    #         'gamma':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    #     }
    #     grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
    #     grid_search.fit(self.X_train, self.Y_train)
    #     Y_pred=grid_search.predict(self.X_test)
    #     return self.model_accuracy(self.Y_test, Y_pred,'xgboost',grid_search)
    
    # adaboost hyperparameter
    def adaboost_hyperparameter(self):
        model=AdaBoostClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
            'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'algorithm':['SAMME.R'],
            'random_state':[None,10,11,12,20,30,40,42],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'adaboost',grid_search)
    
    # gradient boosting hyperparameter
    def gradient_boosting_hyperparameter(self):
        model=GradientBoostingClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'loss':['log_loss'],
            'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000],
            'subsample':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'criterion':['friedman_mse'],
            'min_samples_split':[2,3,4,5,6,7,8,9,10],
            'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10],
            'min_weight_fraction_leaf':[0.0],
            'max_depth':[3,4,5,6,7,8,9,10],
            'min_impurity_decrease':[0.0],
            'init':[None],
            'random_state':[None,10,11,12,20,30,40,42],
            'max_features':[None],
            'verbose':[0,1,2,3,4,5,6,7,8,9,10],
            'max_leaf_nodes':[None],
            'warm_start':[False],
            'validation_fraction':[0.1],
            'n_iter_no_change':[None],
            'tol':[0.0001],
            'ccp_alpha':[0.0],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'gradient_boosting',grid_search)
    
    # svc hyperparameter
    def svc_hyperparameter(self):
        model=SVC()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'C':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
            'kernel':['rbf'],
            'degree':[3,4,5,6,7,8,9,10],
            'gamma':['scale'],
            'coef0':[0.0],
            'shrinking':[True,False],
            'probability':[True,False],
            'tol':[0.001],
            'cache_size':[200],
            'class_weight':[None],
            'verbose':[True,False],
            'max_iter':[-1],
            'decision_function_shape':['ovr'],
            'break_ties':[True,False],
            'random_state':[None,10,11,12,20,30,40,42],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'svc',grid_search)
    
    # decision tree hyperparameter
    def decision_tree_hyperparameter(self):
        model=DecisionTreeClassifier()
        cv_sets=ShuffleSplit(n_splits=5,test_size=0.2,random_state=42)
        param_grid={
            'criterion':['gini'],
            'splitter':['best'],
            'max_depth':[None],
            'min_samples_split':[2,3,4,5,6,7,8,9,10],
            'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10],
            'min_weight_fraction_leaf':[0.0],
            'max_features':[None],
            'random_state':[None,10,11,12,20,30,40,42],
            'max_leaf_nodes':[None],
            'min_impurity_decrease':[0.0],
            'class_weight':[None],
            'ccp_alpha':[0.0],
        }
        grid_search=RandomizedSearchCV(estimator=model,param_distributions=param_grid,n_iter=100,cv=cv_sets,n_jobs=-1,verbose=2,scoring='accuracy')
        grid_search.fit(self.X_train, self.Y_train)
        Y_pred=grid_search.predict(self.X_test)
        return self.model_accuracy(self.Y_test, Y_pred,'decision_tree',grid_search)
        
    

    



