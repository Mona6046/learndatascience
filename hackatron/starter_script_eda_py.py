import pandas as pd
import numpy as np
import glob
import matplotlib as mpl 
import matplotlib.pyplot as plt 
%matplotlib inline


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

#Plotting the histogram of fuel flow (hourly consumption)
plt.hist(training_data["FF"], normed=True, bins=50,  edgecolor='black', linewidth=1.2); plt.ylabel('Fuel Flow');


#Creating Box plot of Fuel Flow across different phases of flight
training_data[["PH", "FF"]].boxplot( by="PH", return_type='axes')

#Scatter plot between LONG_Max and FF (Fuel Flow)
plt.plot(training_data["LONG_Max"], training_data["FF"], "o")