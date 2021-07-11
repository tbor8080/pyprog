
#Simple assignment
from selenium.webdriver import Chrome

driver = Chrome()
Chrome(executable_path='/path/to/chromedriver')

#Or use the context manager
from selenium.webdriver import Chrome

with Chrome() as driver:
    #your code inside this indent
    print("hello")