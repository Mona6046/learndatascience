library(ggplot2)

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

#Plotting the histogram of fuel flow (hourly consumption)
ggplot(data = training_data, aes(training_data['FF'])) +
 geom_histogram(fill=I("blue"), col=I("red"), alpha = I(.2), binwidth = 250)


#Plotting bar chart of mean fuel consumption across different phases of flight
ggplot(data = training_data) +
 geom_bar(aes(as.factor(training_data$PH), training_data$FF, fill = as.factor(training_data$PH)), stat = "summary", fun.y = "mean")

#Creating Box plot of Fuel Flow across different phases of flight
ggplot(data = training_data, aes(x = as.factor(PH), y = FF)) + geom_boxplot()

#Scatter plot between LONG_Max and FF (Fuel Flow)
ggplot(data = training_data, aes(x = LONG_Max, y= FF)) + geom_point(shape = 19, alpha = .10, color = 'darkblue')

