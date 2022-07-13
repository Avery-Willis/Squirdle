library(tidyr)
library(readr)
library(dplyr)

#clean pokemon database, select for relevant columns: name, generation, types, height, weight
pokemon <- read_csv('pokemon.csv')
pokemon <- pokemon %>%
  select(name, generation,type_1, type_2, height_m, weight_kg) 

#write CSV for use in SquirdleSolver
write.csv(pokemon, 'C:\Users\awill\OneDrive\Desktop\SQUIRDLE Solver')

#find "average pokemon"
#best guess for initial guess

summary(pokemon)

#median gen: 4
#median height: 1m
#median weight: 27.3kg


type1counts<-pokemon %>%
  count(type_1)
type1counts

type2counts<-pokemon %>%
  count(type_2)
type2counts

#best type 1: water, since 134 water
#best type 2: none, since 486 NA

bestpokemon <- pokemon %>%
  filter(generation ==4 & type_1 == 'Water' & weight_kg > 25 & weight_kg<30)
bestpokemon

#Best Pokemon To Start Is Buizel:
#Mean generation, Water, No Type 2, height ~1, weight ~27.3