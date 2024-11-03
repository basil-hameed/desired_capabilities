"""
Automating Chrome Browser in Incognito Mode
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

# Create Data Class to store all the data like username, password, url
class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

# Create Locators Class to store all the locators like xpath, id, class
class Locators:
    username_locator = 'username'
    password_locator = 'password'
    login_button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

# Create IncognitoChrome Class and define the methods
class IncognitoChrome(Data, Locators):
    def incognito_window(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window()
            driver.get(self.url)
            sleep(5)
            driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
            sleep(2)
            driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
            sleep(2)
            driver.find_element(by=By.XPATH, value=self.login_button_locator).click()
            sleep(5)
            print("SUCCESS: Chrome launched in incognito mode !")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)


myChromeIncognito = IncognitoChrome()
myChromeIncognito.incognito_window()

