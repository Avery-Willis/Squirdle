library(tidyr)
library(readr)
library(dplyr)
library(forcats)

data <- read_csv('pokemonDatacsvwithExtra.csv')
data
View(data)


data <- data %>%
  select(c(2,3,4,5,6,7))
View(data)

data$type_2 <- fct_explicit_na(data$type_2, na_level= "None")


write.csv(data, 'dataFinalized.csv')
