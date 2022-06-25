from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By

class HomePageLocators:
    """
    Locators for Registration Page
    """
    ACCEPT_COOKIES_BTN = (By.XPATH, '//div[@class="e-consents-alert__actions"]/button[1]')
    REGISTER_LINK = (By.XPATH, '//a[@data-testid="header-register-link"]')


class HomePage(BasePage):
    """
    Registration Page
    """
    def close_cookies_alert(self):
        self.driver.find_element(*HomePageLocators.ACCEPT_COOKIES_BTN).click()

    def click_register_link(self):
        """
        Clicks Register link
        """
        self.driver.find_element(*HomePageLocators.REGISTER_LINK).click()
        # Zwróć instancję nowej strony (Strona Rejestracji)
        return RegistrationPage(self.driver)
