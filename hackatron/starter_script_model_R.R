library(randomForest)
library(caret)
library(Metrics)

load_data <- function(path) {
  setwd(path)
  all_files = list.files(pattern="*.csv")
  df <- data.frame()
  for(i in 1:length(all_files))
    df <- rbind(df, read.csv(all_files[i], header = TRUE))
  return(df)
}
  
#Provide path to directory containing training dataset files.
path = "C:/Users/../training_set/"

#Load the training dataset.  
training_data <- load_data(path)

#Check the dimension of the training dataset. It should be (412020, 219)
dim(training_data)

#Select all feature columns except Aircraft ID column and target Fuel Flow
drops_train = c("FF", 'ACID')
features_train <- !(names(training_data) %in% drops_train)

#Data Pre-Processing
preprocessParams <- preProcess(training_data[,features_train], method=c("scale"))
training_data[,features_train] <- predict(preprocessParams, training_data[,features_train])

#Create Random Forest Model on the training dataset.
rfr <- randomForest(FF ~., data = training_data, ntree = 10, nodesize = 500)

#Compute the RMSE on the training set
print(paste("Train RMSE", rmse(training_data['FF'], predict(rfr, training_data)), sep = " "))

#Import the test set. 
#Provide path to direcotory containing test dataset files.
path = "C:/Users/../test_set/"
test_data = load_data(path)

#Check the dimension of the test dataset. It should be (195140, 219)
dim(test_data)

#Select all feature columns except Aircraft ID column and Record_ID
drops_test = c('ACID', 'Record_ID')
features_test <- !(names(test_data) %in% drops_test)

#Data Pre-Processing
test_data[,features_test] <- predict(preprocessParams, test_data[,features_test])

#Make Predictions on the test set
predictions = predict(rfr, test_data)

#Submit the prediction file
sub_df = data.frame('Record_ID' = test_data$Record_ID, 'Prediction' = predictions)
write.csv(sub_df, "submission.csv", row.names = FALSE)
