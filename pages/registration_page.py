from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPageLocators:
    NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")

class RegistrationPage(BasePage):
    def fill_name(self, name):
        el = self.driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        el.send_keys(name)

    def fill_surname(self, surname):
        el = self.driver.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        el.send_keys(surname)