from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from GetFeedback import before_first, after_first, scoop
import pandas

#SETUP webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://squirdle.fireblend.com/")


guessCount =0
def PokeGuess(pokeGuess):
    
    search = driver.find_element(By.ID, "guess")
    search.send_keys(pokeGuess)
    search.send_keys(Keys.RETURN)
    enter  = driver.find_element(By.ID, "guess_submit")
    enter.click()
    UpdateHTML()
    global feedback
    feedback = Feedback(guessHTML())
    global curr
    curr = CurrentGuess(pokeGuess)
    ChooseNew()
    return 

class CurrentGuess:
    def __init__(self, name):
        stringMon = 'name == "'+name+'"'
        dataframe = pokeData.query(stringMon)
        data = dataframe.values[0]
        self.name = data[1]
        self.gen = data[2]
        self.type1 = data[3]
        self.type2 = str(data[4])
        self.height = str(data[5])
        self.weight = str(data[6])

def UpdateHTML():
    global htmlstring 
    htmlstring = str(BeautifulSoup(driver.page_source).prettify())
    return htmlstring


def guessHTML():
    '''Splices string with feedback from guessCount'''
    htmlfinal = scoop(htmlstring, 'id="guess'+str(guessCount), 'class="tooltip">')
    return htmlfinal

class Feedback:
    def __init__(self,s):
        self.gen = genFeedback(s)
        self.type1 = Type1Feedback(s)
        self.type2 = Type2Feedback(s)
        self.height = HeightFeedback(s)
        self.weight = WeightFeedback(s)
    
  
def genFeedback(s):
    return scoop(s, "imgs/",".png")

def Type1Feedback(s):
    splice = after_first(s, ".png")
    return scoop(splice, "imgs/", ".png")

def Type2Feedback(s):
    spliceOne = after_first(s, ".png")
    spliceTwo = after_first(spliceOne, ".png")
    return scoop(spliceTwo, "imgs/",".png")

def HeightFeedback(s):
    spliceOne = after_first(s, ".png")
    spliceTwo = after_first(spliceOne, ".png")
    spliceThree = after_first(spliceTwo, ".png")
    return scoop(spliceThree, "imgs/", ".png")

def WeightFeedback(s):
    spliceOne = after_first(s, ".png")
    spliceTwo = after_first(spliceOne, ".png")
    spliceThree = after_first(spliceTwo, ".png")
    spliceFour = after_first(spliceThree, ".png")
    return scoop(spliceFour, "imgs/", ".png")
    
pandas.set_option('expand_frame_repr', False)
pokeData = pandas.read_csv('pokemonCleaned.csv')

def ChooseNew():
    """returns pokemon name for next guess"""
    #filter by generation
    global newGuessDF
    if feedback.gen=='up':
        newGuessDF = pokeData.query('gen > ' + str(curr.gen))
    elif feedback.gen=='down':
        newGuessDF = pokeData.query('gen < ' + str(curr.gen))
    else:
        newGuessDF = pokeData.query('gen == '+str(curr.gen))
    
    #filter by type1
    if feedback.type1 =='wrong':
        newGuessDF = pokeData.query('type_1 != "'+curr.type1+'"')
    elif feedback.type1 =='correct':
        newGuessDF = pokeData.query('type_1 == "'+curr.type1+'"')
    else:
        newGuessDF = pokeData.query('type_2 == "'+curr.type1+'"')
    
    #filter by type2
    if feedback.type2==None:
        pass
    elif feedback.type2 =='wrong':
        newGuessDF = pokeData.query('type_2 != "'+curr.type2+'"')
    elif feedback.type2 =='correct':
        newGuessDF = pokeData.query('type_2 == "'+curr.type2+'"')
    else:
        newGuessDF = pokeData.query('type_1 == "'+curr.type2+'"')
    
    #filter by height
    if feedback.height == 'up':
        newGuessDF = pokeData.query('height_m > '+str(curr.height))
    if feedback.height == 'down':
        newGuessDF = pokeData.query('height_m < '+str(curr.height))
    
    #filter by weight
    if feedback.weight == 'up':
        newGuessDF = pokeData.query('weight_kg > '+str(curr.weight))
    if feedback.weight == 'down':
        newGuessDF = pokeData.query('weight_kg < '+str(curr.weight))
    
    n = int(len(newGuessDF.values)/2)
    print(newGuessDF.values[n][1])
    return
    
    
    











PokeGuess("Buizel")
