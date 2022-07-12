from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

    
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://squirdle.fireblend.com/")



def PokeGuess(pokeGuess):
    search = driver.find_element(By.ID, "guess")
    search.send_keys(pokeGuess)
    search.send_keys(Keys.RETURN)
    enter  = driver.find_element(By.ID, "guess_submit")
    enter.click()
    time.sleep(15)
    driver.quit()
    return

