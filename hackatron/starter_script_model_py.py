import pandas as pd
import numpy as np
import glob
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def load_data(path):
    all_files = glob.glob(path + "/*.csv")
    list = []
    for file in all_files:
        df = pd.read_csv(file, index_col = None, header = 0)
        list.append(df)
    return pd.concat(list)
	
	
#Provide path to direcotory containing training dataset files.
path = r"C:\Users\..\training_set"

#Load the training dataset.
training_data = load_data(path)

#Check the dimension of the training dataset. It should be (412020, 219)
training_data.shape

#Select all feature columns except Aircraft ID column and target Fuel Flow
feature_columns = [col for col in training_data.columns if not (col=='FF' or  col=='ACID')]

#Data Pre-processing
y = training_data['FF']
X = training_data[feature_columns]
std_scale = StandardScaler().fit(X)
X = std_scale.transform(X)

#Create Random Forest Model on the training dataset.
rfr = RandomForestRegressor(n_estimators=10, min_samples_leaf = 500)
rfr.fit(X,y)

#Compute the RMSE on the training set
print "Train RMSE", sqrt(mean_squared_error(y, rfr.predict(X)))

#Import the test set. 
#Provide path to direcotory containing test dataset files.
path = r"C:\Users\..\test_set"
test_data = load_data(path)

#Check the dimension of the test dataset. It should be (195140, 219)
test_data.shape

#Select all feature columns except Aircraft ID column and Record_ID
feature_columns = [col for col in test_data.columns if not (col=='ACID' or col == 'Record_ID')]
X_test = test_data[feature_columns]
X_test = std_scale.transform(X_test)
#Make Predictions on the test set
predictions = rfr.predict(X_test)

#Submit the prediction file
df = pd.DataFrame({'Record_ID' : test_data.Record_ID.astype(int), 'Prediction' : predictions})
pd.DataFrame.to_csv(df, "submission.csv", index = False)