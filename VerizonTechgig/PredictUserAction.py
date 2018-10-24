import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve,auc
import os
cwd = os.getcwd()
print(cwd)
train=pd.read_csv(cwd+'\\training_data.csv')
test=pd.read_csv(cwd+'\\test_data.csv')
train['Type']='Train'
test['Type']='Test'
fullData = pd.concat([train,test],axis=0,sort=False)
fullData2= fullData
fullData=fullData[fullData['id']!= 'session************']
fullData['timestamp']=pd.to_datetime(fullData['timestamp'], format='%Y-%m-%dT%H:%M:%S.%f')+ pd.Timedelta('-04:00:00')
fullData['hour'] = fullData['timestamp'].dt.hour
fullData.head(10)
#0 for lower, 1 for middle, 2 for upper
# creating a dict   
Funnel_level = {'lower': 0,'middle': 2,'upper': 2} 
fullData['funnel_level'] = [Funnel_level[item] for item in fullData['funnel_level'] ] 
fullData.info()
fullData.isnull().any()
fullData.describe()
fullData.describe(include=['O'])
fullData[['link', 'order_placed']].groupby(['link'], as_index=False).mean().sort_values(by='link', ascending=True)
ID_col = ['id']
target_col = ['order_placed'] 
cat_cols = ['ad','link','hour','grp']
other_col=['Type','timestamp','checkout','ad']
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col)-set(other_col))
num_cat_cols = num_cols+cat_cols
for var in num_cat_cols:
    if fullData[var].isnull().any()==True:
        fullData[var+'_NA']=fullData[var].isnull()*1 
fullData[cat_cols] = fullData[cat_cols].fillna(value = -9999)
for var in cat_cols:
 number = LabelEncoder()
 fullData[var] = number.fit_transform(fullData[var].astype('str'))
train=fullData[fullData['Type']=='Train']
test=fullData[fullData['Type']=='Test']
train['is_train'] = np.random.uniform(0, 1, len(train)) <= .75
Train, Validate = train[train['is_train']==True], train[train['is_train']==False]
features=list(set(list(fullData.columns))-set(ID_col)-set(target_col)-set(other_col))
x_train = Train[list(features)].values
y_train = Train["order_placed"].values
x_validate = Validate[list(features)].values
y_validate = Validate["order_placed"].values
x_test=test[list(features)].values
x_train
random.seed(100)
rf = GradientBoostingClassifier(n_estimators=1000)
rf.fit(x_train, y_train)
features
status = rf.predict_proba(x_validate)
fpr, tpr, _ = roc_curve(y_validate, status[:,1])
roc_auc = auc(fpr, tpr)
print (roc_auc)
final_status = rf.predict_proba(x_test)
test["order_placed"]=final_status[:,1]
test.to_csv(cwd+'\\gbc_model_output.csv',columns=['id','order_placed'])
