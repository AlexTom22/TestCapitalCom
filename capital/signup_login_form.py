import allure
from datetime import datetime
from capital.base_page import BasePage
from capital.capital_locators import SignupLoginFormLocators
# from .src import HeaderSrc


class SignupLoginForm(BasePage):

    @allure.step(f"{datetime.now()}.   Check that the 'SignUp' form is open.")
    def should_be_signup_form(self):
        """
        Check there's an element to on SignUp form
        ссылка вверху формы для перехода на Login
        """
        assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_REF_LOGIN_LOCATOR, 15), \
            "'SignUp' form did not open"

    @allure.step(f"{datetime.now()}.   Close the 'Sign Up' form.")
    def close_signup_form(self):
        self.element_is_clickable(SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 10)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()

    @allure.step(f"{datetime.now()}.   Check that the 'Login' form is open.")
    def should_be_login_form(self):
        """
        Check there's an element to on Login form
        ссылка вверху формы для перехода на Signup
        """
        # Check there's an element to on login form
        cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_REF_SIGNUP_LOCATOR, 15)
        assert cur_assert, "'Login' form did not open"
        # Check the checkbox "Log me out after 7 days"
        # cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_CHECKBOX_LOCATOR)
        # assert cur_assert, "Login frame not open"

    @allure.step(f"{datetime.now()}.   Close the 'Login' form.")
    def close_login_form(self):
        self.element_is_clickable(SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM, 10)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
