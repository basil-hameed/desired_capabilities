"""
Open the chrome browser in 640 x 450 configuration
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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

# Create the WindowConfiguration Class to define the methods
class WindowConfiguration(Data, Locators):

    def window_size_automation(self, width, height):
        try:
            chrome_options = Options()
            chrome_options.add_argument(f"--window-size={width},{height}")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            sleep(5)
            driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
            sleep(2)
            driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
            sleep(2)
            driver.find_element(by=By.XPATH, value=self.login_button_locator).click()
            sleep(5)
            window_size = driver.get_window_size()
            print("Window Width", window_size['width'])
            print("Window Height", window_size['height'])
            print("SUCCESS, Window launched with the specified configuration !")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

# create an object and call the methods
myCapability = WindowConfiguration()
myCapability.window_size_automation(640, 450)