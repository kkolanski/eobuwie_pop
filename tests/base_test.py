import unittest
from selenium import webdriver
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.eobuwie.com.pl/")
        self.home_page = HomePage(self.driver)
        self.home_page.close_cookies_alert()

    def tearDown(self):
        self.driver.quit()