from base_test import BaseTest

class RegistrationTest(BaseTest):
    def test_password_does_not_match(self):
        self.home_page.click_register_link()