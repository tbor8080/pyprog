# WebDriver Bidi APIs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os
import pprint


driver = webdriver.Chrome()
url='localhost:8080'
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# pprint.pprint(__file__)

# print(path)
driver.get(url)

print(driver.title)

