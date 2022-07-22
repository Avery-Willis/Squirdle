import pandas
from SquirdleSolver import feedback

pandas.set_option('expand_frame_repr', False)
pokeData = pandas.read_csv('pokemonCleaned.csv')

def ChooseNew(lastGuess):
    """returns pokemon name for next guess"""
    #filter by generation
    global newGuessDF
    if feedback.gen=='up':
        newGuessDF = pokeData.query('generation > "' + feedback.gen+'"')
    elif feedback.gen=='down':
        newGuessDF = pokeData.query('generation > "' + feedback.gen+'"')
    else:
        newGuessDF = pokeData.query('generation == "'+feedback.gen+'"')
    
    #filter by type1
    if feedback.type1 =='wrong':
        newGuessDF = pokeData.query('type_1 != "'+feedback.type1+'"')
    elif feedback.type1 =='correct':
        newGuessDF = pokeData.query('type_1 == "'+feedback.type1+'"')
    else:
        newGuessDF = pokeData.query('type_2 == "'+feedback.type1+'"')
    
    #filter by type2
    if feedback.type2==None:
        pass
    elif feedback.type2 =='wrong':
        newGuessDF = pokeData.query('type_2 != "'+feedback.type2+'"')
    elif feedback.type2 =='correct':
        newGuessDF = pokeData.query('type_2 == "'+feedback.type2+'"')
    else:
        newGuessDF = pokeData.query('type_1 == "'+feedback.type2+'"')
    
    #filter by height
    if feedback.height == 'up':
        newGuessDF = pokeData.query('height > "'+feedback.height+'"')
    if feedback.height == 'down':
        newGuessDF = pokeData.query('height < "'+feedback.height+'"')
    
    #filter by weight
    if feedback.weight == 'up':
        newGuessDF = pokeData.query('weight > "'+feedback.weight+'"')
    if feedback.weight == 'down':
        newGuessDF = pokeData.query('weight < "'+feedback.weight+'"')
        
    print(newGuessDF.values[0][1])
    return
    
    
    
    
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

