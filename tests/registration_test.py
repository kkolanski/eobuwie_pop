from base_test import BaseTest

class RegistrationTest(BaseTest):
    def test_password_does_not_match(self):
        self.registration_page = self.home_page.click_register_link()
        self.registration_page.fill_name("Adam")