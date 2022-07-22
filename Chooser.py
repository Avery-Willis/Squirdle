import pandas
import csv


pandas.set_option('expand_frame_repr', False)
pokeData = pandas.read_csv('pokemonCleaned.csv')

def ChooseNew():
    newGuess = pokeData.query('generation > 1')
    print(newGuess)
    
class CurrentGuess:
    def __init__(self, name):
        stringMon = 'name == "'+name+'"'
        dataframe = pokeData.query(stringMon)
        data = dataframe.values[0]
        self.name = data[1]
        self.gen = data[2]
        self.type1 = data[3]
        self.type2 = data[4]
        self.height = data[5]
        self.weight = data[6]

