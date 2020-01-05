if (!require("dplyr")) 
  install.packages("dplyr")

if (!require("ggplot2")) 
  install.packages("ggplot2")

if (!require("cluster")) 
  install.packages("cluster")

library(ggplot2)
library(dplyr)
library(cluster)

#dataset
df <- read.csv("../african_crises.csv", header=TRUE , sep = ',', dec = '.')

#generic summary of the dataset

#exch_usd
median_exch_usd <- median(df$exch_usd) 
avg_exch_usd <- mean(df$exch_usd)
stand_dev_exch_usd <- sqrt(sum((df$exch_usd - avg_exch_usd)^2/length(df$exch_usd)-1))
total_variance_exch_usd <- sum((df$exch_usd - avg_exch_usd)^2/length(df$exch_usd)-1)

#inflation
median_cpi <- median(df$inflation_annual_cpi)
avg_cpi <- mean(df$inflation_annual_cpi)
stand_dev_cpi <- sqrt(sum((df$inflation_annual_cpi - avg_cpi)^2/length(df$inflation_annual_cpi)-1))
total_variance_cpi <- sum((df$inflation_annual_cpi - avg_cpi)^2/length(df$inflation_annual_cpi)-1)

#countries
algeria <- subset(df, df$cc3 == 'DZA')
angola <- subset(df, df$cc3 == 'AGO')
central_african_republic <- subset(df, df$cc3 == 'CAF')
ivory_coast <- subset(df, df$cc3 == 'CIV')
egypt <- subset(df, df$cc3 == 'EGY')
kenya <- subset(df, df$cc3 == 'KEN')
mauritius <- subset(df, df$cc3 == 'MUS')
morocco <- subset(df, df$cc3 == 'MAR')
nigeria <- subset(df, df$cc3 == 'NGA')
south_africa <- subset(df, df$cc3 == 'ZAF')
tunisia <- subset(df, df$cc3 == 'TUN')
zambia <- subset(df, df$cc3 == 'ZMB')
zimbabwe <- subset(df, df$cc3 == 'ZWE')

#algeria
algeria_stand_dev_exch_usd <- sqrt(sum((algeria$exch_usd - avg_exch_usd)^2/length(algeria$exch_usd)-1))
algeria_stand_dev_cpi <- sqrt(sum((algeria$inflation_annual_cpi - avg_cpi)^2/length(algeria$inflation_annual_cpi)-1))

#angola
angola_stand_dev_exch_usd <- sqrt(sum((angola$exch_usd - avg_exch_usd)^2/length(angola$exch_usd)-1))
angola_stand_dev_cpi <- sqrt(sum((angola$inflation_annual_cpi - avg_cpi)^2/length(angola$inflation_annual_cpi)-1))

#central_african_republic
central_african_republic_stand_dev_exch_usd <- sqrt(sum((central_african_republic$exch_usd - avg_exch_usd)^2/length(central_african_republic$exch_usd)-1))
central_african_republic_stand_dev_cpi <- sqrt(sum((central_african_republic$inflation_annual_cpi - avg_cpi)^2/length(central_african_republic$inflation_annual_cpi)-1))

#ivory_coast
ivory_coast_stand_dev_exch_usd <- sqrt(sum((ivory_coast$exch_usd - avg_exch_usd)^2/length(ivory_coast$exch_usd)-1))
ivory_coast_stand_dev_cpi <- sqrt(sum((ivory_coast$inflation_annual_cpi - avg_cpi)^2/length(ivory_coast$inflation_annual_cpi)-1))

#egypt
egypt_stand_dev_exch_usd <- sqrt(sum((egypt$exch_usd - avg_exch_usd)^2/length(egypt$exch_usd)-1))
egypt_stand_dev_cpi <- sqrt(sum((egypt$inflation_annual_cpi - avg_cpi)^2/length(egypt$inflation_annual_cpi)-1))

#kenya
kenya_stand_dev_exch_usd <- sqrt(sum((kenya$exch_usd - avg_exch_usd)^2/length(kenya$exch_usd)-1))
kenya_stand_dev_cpi <- sqrt(sum((kenya$inflation_annual_cpi - avg_cpi)^2/length(kenya$inflation_annual_cpi)-1))

#mauritius
mauritius_stand_dev_exch_usd <- sqrt(sum((mauritius$exch_usd - avg_exch_usd)^2/length(mauritius$exch_usd)-1))
mauritius_stand_dev_cpi <- sqrt(sum((mauritius$inflation_annual_cpi - avg_cpi)^2/length(mauritius$inflation_annual_cpi)-1))

#morocco
morocco_stand_dev_exch_usd <- sqrt(sum((morocco$exch_usd - avg_exch_usd)^2/length(morocco$exch_usd)-1))
morocco_stand_dev_cpi <- sqrt(sum((morocco$inflation_annual_cpi - avg_cpi)^2/length(morocco$inflation_annual_cpi)-1))

#nigeria
nigeria_stand_dev_exch_usd <- sqrt(sum((nigeria$exch_usd - avg_exch_usd)^2/length(nigeria$exch_usd)-1))
nigeria_stand_dev_cpi <- sqrt(sum((nigeria$inflation_annual_cpi - avg_cpi)^2/length(nigeria$inflation_annual_cpi)-1))

#south_africa
south_africa_stand_dev_exch_usd <- sqrt(sum((south_africa$exch_usd - avg_exch_usd)^2/length(south_africa$exch_usd)-1))
south_africa_stand_dev_cpi <- sqrt(sum((south_africa$inflation_annual_cpi - avg_cpi)^2/length(south_africa$inflation_annual_cpi)-1))

#tunisia
tunisia_stand_dev_exch_usd <- sqrt(sum((tunisia$exch_usd - avg_exch_usd)^2/length(tunisia$exch_usd)-1))
tunisia_stand_dev_cpi <- sqrt(sum((tunisia$inflation_annual_cpi - avg_cpi)^2/length(tunisia$inflation_annual_cpi)-1))

#zambia
zambia_stand_dev_exch_usd <- sqrt(sum((zambia$exch_usd - avg_exch_usd)^2/length(zambia$exch_usd)-1))
zambia_stand_dev_cpi <- sqrt(sum((zambia$inflation_annual_cpi - avg_cpi)^2/length(zambia$inflation_annual_cpi)-1))

#zimbabwe
zimbabwe_stand_dev_exch_usd <- sqrt(sum((zimbabwe$exch_usd - avg_exch_usd)^2/length(zimbabwe$exch_usd)-1))
zimbabwe_stand_dev_cpi <- sqrt(sum((zimbabwe$inflation_annual_cpi - avg_cpi)^2/length(zimbabwe$inflation_annual_cpi)-1))

# 1st plot
ggplot(data = df, aes(x = systemic_crisis, y = year, colour=banking_crisis)) + geom_point() + scale_color_manual(values=c("no_crisis" = "blue", "crisis" = "red")) + scale_x_continuous(limits=c(0,1))
# 2nd plot
ggplot(data = df, aes(y = inflation_annual_cpi, x = banking_crisis, colour=banking_crisis)) + geom_point() + scale_color_manual(values=c("no_crisis" = "blue", "crisis" = "red")) + ylim(0,5000)
# 3rd plots
ggplot(data = zambia, aes(x = year, y = inflation_annual_cpi, colour=inflation_crises)) + geom_point() + scale_color_gradient()
ggplot(data = angola, aes(x = year, y = inflation_annual_cpi, colour=inflation_crises)) + geom_point() + scale_color_gradient()
#4th plots
ggplot(data.frame(countries=c("algeria","angola","central_african_republic","ivory_coast","egypt","kenya","mauritius","morocco","nigeria","south_africa","tunisia","zambia","zimbabwe"), standard_deviation_exch_usd=c(algeria_stand_dev_exch_usd,angola_stand_dev_exch_usd,central_african_republic_stand_dev_exch_usd,ivory_coast_stand_dev_exch_usd,egypt_stand_dev_exch_usd,kenya_stand_dev_exch_usd,mauritius_stand_dev_exch_usd,morocco_stand_dev_exch_usd,nigeria_stand_dev_exch_usd,south_africa_stand_dev_exch_usd,tunisia_stand_dev_exch_usd,zambia_stand_dev_exch_usd,zimbabwe_stand_dev_exch_usd)), aes(countries, standard_deviation_exch_usd)) + geom_col()
ggplot(data.frame(countries=c("algeria","angola","central_african_republic","ivory_coast","egypt","kenya","mauritius","morocco","nigeria","south_africa","tunisia","zambia","zimbabwe"), standard_deviation_cpi=c(algeria_stand_dev_cpi,angola_stand_dev_cpi,central_african_republic_stand_dev_cpi,ivory_coast_stand_dev_cpi,egypt_stand_dev_cpi,kenya_stand_dev_cpi,mauritius_stand_dev_cpi,morocco_stand_dev_cpi,nigeria_stand_dev_cpi,south_africa_stand_dev_cpi,tunisia_stand_dev_cpi,zambia_stand_dev_cpi,zimbabwe_stand_dev_cpi)), aes(countries, standard_deviation_cpi)) + geom_col()
#5th plots
ggplot(data = df, aes(y = independence, x = year, colour=banking_crisis)) + geom_point() + scale_color_manual(values=c("no_crisis" = "blue", "crisis" = "red"))
ggplot(data = nigeria, aes(y = independence, x = year, colour=banking_crisis)) + geom_point() + scale_color_manual(values=c("no_crisis" = "blue", "crisis" = "red"))
#Cluster
# K-Means Clustering with 2 clusters
parsed_df <- subset(df, select=systemic_crisis:inflation_crises) 
fit <- kmeans(parsed_df, 2)
parsed_df$cluster <- fit$cluster
# Cluster Plot against 1st 2 principal components
#clusplot(parsed_df, fit$cluster, color=TRUE, shade=TRUE, labels=2, lines=0)
ggplot(data = parsed_df, aes(x = inflation_annual_cpi, y = exch_usd, colour=cluster)) + geom_point() + scale_color_gradient()

summary(df)