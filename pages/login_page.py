from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not presented in current url"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email=None, password=None):
        f = faker.Faker()
        email = f.email()
        password = f.password(length=9)
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
