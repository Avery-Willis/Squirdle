from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from GetFeedback import before_first, after_first, scoop
    
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
    return 



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
    

PokeGuess("Buizel")
