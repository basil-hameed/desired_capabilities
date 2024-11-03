"""
Open firefox browser in 640 x 450 configuration
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

class Locators:
    username_locator = 'username'
    password_locator = 'password'
    login_button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

class FirefoxWindowConfiguration(Data, Locators):
    def window_size_automation(self, width, height):
        try:
            firefox_options = Options()
            firefox_options.add_argument(f"--width={width}")
            firefox_options.add_argument(f"--height={height}")
            driver = webdriver.Firefox(options=firefox_options)
            driver.get(self.url)
            sleep(5)
            driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
            sleep(2)
            driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
            sleep(2)
            driver.find_element(by=By.XPATH, value=self.login_button_locator).click()
            sleep(5)
            window_size = driver.get_window_size()
            print("Window Width :", window_size['width'])
            print("Window Height :", window_size['height'])
            print("SUCCESS : Launched browser with desired configuration !")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR : ", error)
        finally:
            driver.quit()

myCapability = FirefoxWindowConfiguration()
myCapability.window_size_automation(640,450)