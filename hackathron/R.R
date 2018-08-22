library(ggplot2) 
setwd("C:/Users/212592487/MyFolder/Personal/hackathron/train_OwBvO8W")
getwd()
demographics <- read.csv("demographics.csv")
event_calendar <- read.csv("event_calendar.csv")
historical_volume <- read.csv("historical_volume.csv")
industry_soda_sales <- read.csv("industry_soda_sales.csv")
industry_volume <- read.csv("industry_volume.csv")
price_sales_promotion <- read.csv("price_sales_promotion.csv")
weather <- read.csv("weather.csv")
historical_volume2=cbind(historical_volume,as.Date( paste(historical_volume$YearMonth,"01",sep=""),"%Y%m%d"))


test=historical_volume[historical_volume$Agency=="Agency_12",]

qplot(test$YearMonth,test$Agency)