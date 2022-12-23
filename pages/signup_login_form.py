import allure
from .base_page import BasePage
from .locators import SignupLoginFormLocators
# from .src import HeaderSrc


class SignupLoginForm(BasePage):

    @allure.step
    def should_be_login_form(self):

        assert self.element_is_visible(SignupLoginFormLocators.LOGIN_FORM), \
            "Форма 'Login' не открылась"
        # assert self.element_is_clickable(SignupLoginFormLocators.LOGIN_LOCATOR, 5), f"Форма 'Login' не открылась"

        # assert self.element_is_visible(SignupLoginFormLocators.LOGIN_LOCATOR), \
        #     f"Форма 'Login' не открылась"

    @allure.step
    def should_be_signup_form(self):

        assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_FORM), \
            "Форма 'Sign up' не открылась"

        # assert self.element_is_clickable(SignupLoginFormLocators.SIGNUP_LOCATOR, 5), f"Форма 'SignUp' не открылась"

        # assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_LOCATOR), \
        #     f"Форма 'Sign up' не открылась"

    @allure.step
    def close_login_form(self):
        # self.element_is_present(*SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM) # +
        self.element_is_visible(SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM)

        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()

    @allure.step
    def close_signup_form(self):
        self.element_is_visible(SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()

    @allure.step
    def should_be_login_form(self):

        # Check there's an element to on login form
        # ссылка вверху формы для перехода на SignUp
        # assert self.element_is_present(*SignupLoginFormLocators.LOGIN_REF_SIGNUP_LOCATOR), \
        #     "тест не обнаружил ссылку перехода на форму зарегистрироваться"
        cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_REF_SIGNUP_LOCATOR)
        assert cur_assert, "Login form not open"

        # Check the checkbox "Log me out after 7 days"
        # cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_CHECKBOX_LOCATOR)
        # assert cur_assert, "Login frame not open"
        # Check there's an element to confirm authorization on the current page
        # cur_assert = self.element_is_visible(SignupLoginFormLocators.LOGIN_SUBMIT_BTN_LOCATOR)
        # assert cur_assert, "SignUp frame not opened"

    @allure.step
    def should_be_signup_form(self):
        """
        Check there's an element to on SignUp form
        ссылка вверху формы для перехода на Login
        """
        assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_REF_LOGIN_LOCATOR), "SignUp form not opened"
        # User's first name on the current page
        # assert self.element_is_present(*SignupLoginFormLocators.SIGNUP_INPUT_USERNAME)
        # Check there's an element to input the Password on the current page
        # assert self.element_is_present(*SignupLoginFormLocators.SIGNUP_INPUT_PASSWORD)
        # Check there's an element to confirm authorization on the current page
        # cur_assert = self.element_is_present(*SignupLoginFormLocators.LOGIN_SUBMIT_BTN)
        # Check there's an element to confirm authorization on the current page
        # assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_SUBMIT_BTN_LOCATOR), "SignUp frame not opened"
