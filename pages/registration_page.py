from base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    """
    Locators for Registration Page
    """
    REGISTER_LINK = (By.XPATH, '//a[@data-testid="header-register-link"]')

class RegistrationPage(BasePage):
    """
    Registration Page
    """
    def click_register_link(self):
        """
        Clicks Register link
        """
        self.driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()