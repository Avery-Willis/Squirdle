from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from SquirdleSolver import PokeGuess



#html = driver.page_source
#soup = BeautifulSoup(html)
#print(soup.prettify())

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://squirdle.fireblend.com/")

PokeGuess("Squirtle")

    

#this is how to get current HTML
soup = BeautifulSoup(driver.page_source)
htmlstring= str(soup.prettify())



