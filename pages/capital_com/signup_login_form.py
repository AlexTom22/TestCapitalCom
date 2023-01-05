import allure
from ..base_page import BasePage
from .locators import SignupLoginFormLocators
# from .src import HeaderSrc


class SignupLoginForm(BasePage):

    @allure.step("Проверяем, что открылась форма 'Sign Up'")
    def should_be_signup_form(self):
        """
        Check there's an element to on SignUp form
        ссылка вверху формы для перехода на Login
        """
        assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_REF_LOGIN_LOCATOR), "SignUp form not opened"

    @allure.step("Закрываем форму 'SignUp'")
    def close_signup_form(self):
        self.element_is_visible(SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()

    @allure.step("Проверяем, что открылась форма 'LogIn'")
    def should_be_login_form(self):
        # Check there's an element to on login form
        cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_REF_SIGNUP_LOCATOR)
        assert cur_assert, "Login form not open"
        # Check the checkbox "Log me out after 7 days"
        # cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_CHECKBOX_LOCATOR)
        # assert cur_assert, "Login frame not open"

    @allure.step("Закрываем форму 'LogIn'")
    def close_login_form(self):
        self.element_is_visible(SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
