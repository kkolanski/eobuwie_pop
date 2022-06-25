from base_test import BaseTest
from time import sleep

class RegistrationTest(BaseTest):
    def test_password_does_not_match(self):
        self.registration_page = self.home_page.click_register_link()
        self.registration_page.fill_name(self.data.customer_first_name)
        self.registration_page.fill_surname(self.data.customer_last_name)
