# WebDriver Bidi APIs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

with  driver.log.mutation_events() as event:
    pages.load("dynamic.html")
    driver.find_element(By.ID, "reveal").click()
    WebDriverWait(driver, 5)\
        .until(EC.visibility_of(driver.find_element(By.ID, "revealed")))

assert event["attribute_name"] == "style"
assert event["current_value"] == ""
assert event["old_value"] == "display:none;"
