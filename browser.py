from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Slow Roads
driver.get('https://slowroads.io/')

# Wait for the game to load
time.sleep(10)

# Focus on the game canvas
body = driver.find_element_by_tag_name('body')

