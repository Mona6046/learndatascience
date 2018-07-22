setwd("C:/Users/212592487/MyFolder/GE/datascienc")
library(dplyr)
library("corrplot")
library("coefplot")
library(ggplot2)
library(stringr)
library(tidyr)



auto=read.csv("auto-mpg.data", header = FALSE, sep = "", quote = "\"",
         dec = ".", fill = TRUE )
colnames(auto) <- c("mpg","cylinders","displacement","horsepower","weight","acceleration","year","origin","name")
auto$country_name=auto$origin %>%str_replace_all(c("1" = "American", "2" = "European", "3" = "Japanese"))
auto$country_name = as.factor(auto$country_name)
auto$car_name = as.factor(auto$name)
auto=auto %>% separate(name,   c("car_company", "rest"))
auto=select(auto,mpg,cylinders,displacement,horsepower,weight,acceleration,year,origin,car_name,car_company)
str(auto)
dim(auto)
summary(auto)
auto$horsepower = as.integer(auto$horsepower)
auto$car_company = as.factor(auto$car_company)
summary(auto)

auto$car_company[ auto$car_company=='vokswagen'|auto$car_company=='vw']<-'volkswagen'
auto$car_company[ auto$car_company=='maxda']<-'mazda'
auto$car_company[ auto$car_company=='toyouta']<-'toyota'
auto$car_company[ auto$car_company=='mercedes-benz']<-'mercedes'
auto$car_company[ auto$car_company=='nissan']<-'datsun'
auto$car_company[ auto$car_company=='capri']<-'ford'
auto$car_company[ auto$car_company=='chevroelt'|auto$car_company=='chevy']<-'chevrolet'

plot(auto)
correlations = cor(auto1)
plot(correlations)
corrplot(correlations)

ggplot(auto1, aes(x = displacement, y =cylinders)) + geom_point()

ggplot(auto1, aes(x = displacement, y =cylinders)) + geom_point()
ggplot(auto, aes(x = mpg, y = acceleration)) + geom_point(aes(color = cylinders))
autoModel1 = lm(mpg ~ cylinders + horsepower + weight + displacement + year + acceleration, data = auto)
summary(autoModel1)
coefplot(autoModel1)



autoModel3 = lm(mpg ~  weight  + year , data = auto)
summary(autoModel3)



boxplot(mpg~country_name,data=auto,col=(c("red","green","blue")), main="Car Milage Data", 
        xlab="Country", ylab="Miles Per Gallon")



boxplot(mpg~car_company,data=auto,col=ifelse(levels(auto$country_name)=="American" , rgb(0.1,0.1,0.7,0.5) , 
                                             ifelse(levels(auto$country_name)=="European",rgb(0.8,0.1,0.3,0.6),"grey90" ) ) , main="Car Milage Data", 
        xlab="car_company", ylab="Miles Per Gallon")
