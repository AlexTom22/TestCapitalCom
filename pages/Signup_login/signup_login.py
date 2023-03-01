import time

import allure
from datetime import datetime
from pages.base_page import BasePage
from pages.Signup_login.signup_login_locators import (
    SignupLoginFormLocators,
    LoginPageLocators,
    SignupPageLocators
)


class SignupLogin(BasePage):

    @allure.step(f"{datetime.now()}.   Check that the 'Sign up' form is open.")
    def should_be_signup_form(self):
        """
        Check there are an elements to on Sign up form
        """
        if self.element_is_visible(SignupLoginFormLocators.SIGNUP_FRAME):
            print("Form 'Sign up' is opened")
            assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_HEADER), \
                "The layout of the 'SignUp' form has changed"
            assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_REF_LOGIN), \
                "Problem with 'Login' reference"
            assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_INPUT_EMAIL), \
                "Problem with 'E-mail' fild"
            assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_INPUT_PASSWORD), \
                "Problem with 'Password' fild"
            assert self.element_is_visible(SignupLoginFormLocators.SIGNUP_SUBMIT_BTN), \
                "Problem with 'Continue' button"
            
            # if self.element_is_visible(SignupLoginFormLocators.SIGNUP_PRIVACY_POLICY):
            #     print("First locator")
            #     assert True
            # elif self.element_is_visible(SignupLoginFormLocators.SIGNUP_PRIVACY_POLICY_DE_ASIC):
            #     print("Second locator")
            #     assert True
            # else:
            #     assert False, "Problem with 'Privacy policy' reference"
            
            return True
        else:
            print("Form 'Sign up' is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Sign up' form.")
    def close_signup_form(self):
        self.element_is_clickable(SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 5)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()
        print("Form 'Sign up' is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Sign up' page is open.")
    def should_be_signup_page(self):
        """
        Check there are an elements to on 'Sign up' page
        """
        time.sleep(2)
        if self.current_page_is("https://capital.com/trading/signup"):
            print("Page 'Sign up' is opened")
            assert self.element_is_present(*SignupPageLocators.SIGNUP_FORM), \
                "The layout of the 'SignUp' page has changed"
            assert self.element_is_visible(SignupPageLocators.REF_LOGIN), \
                "Problem with 'Login' reference"
            assert self.element_is_visible(SignupPageLocators.INPUT_EMAIL), \
                "Problem with 'E-mail' fild"
            assert self.element_is_visible(SignupPageLocators.INPUT_PASS), \
                "Problem with 'Password' fild"
            assert self.element_is_visible(SignupPageLocators.BUTTON_CONTINUE), \
                "Problem with 'Continue' button"
            # assert self.element_is_visible(SignupPageLocators.REF_PRIVACY_POLICY), \
            #     "Problem with 'Privacy policy' reference"
            return True
        else:
            print("Page 'Sign up' is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Sign up' page.")
    def close_signup_page(self):
        self.browser.back()
        print("Page 'Sign up' is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Login' form is open.")
    def should_be_login_form(self):
        """
        Check there are an elements to on Login form
        """
        if self.element_is_visible(SignupLoginFormLocators.LOGIN_FRAME):
            print("Form 'Login' is opened")
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_HEADER), \
                "The layout of the 'Login' form has changed"
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_REF_SIGNUP), \
                "Problem with 'Sign up' reference"
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_INPUT_EMAIL), \
                "Problem with 'Email address' fild"
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_INPUT_PASSWORD), \
                "Problem with 'Password' fild"
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_CHECKBOX), \
                "Problem with 'Log me out after 7 days' check box"
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_CONTINUE), \
                "Problem with 'Continue' button"
            assert self.element_is_visible(SignupLoginFormLocators.LOGIN_PASS_FORGOT), \
                "Problem with 'Forgot password' reference"
            return True
        else:
            print("Form 'Login' is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Login' form.")
    def close_login_form(self):
        self.element_is_clickable(SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM, 5)
        self.browser.find_element(*SignupLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
        print("Form 'Login' is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Login' page is open.")
    def should_be_login_page(self):
        """
        Check there are elements to on SignUp page
        """
        time.sleep(2)
        if self.current_page_is("https://capital.com/trading/login"):
            print("Page 'Login' is opened")
            assert self.element_is_present(*LoginPageLocators.LOGIN_FORM), \
                "The layout of the 'Login' page has changed"
            assert self.element_is_visible(LoginPageLocators.REF_SIGNUP), \
                "Problem with 'Sign up' reference"
            assert self.element_is_visible(LoginPageLocators.INPUT_EMAIL), \
                "Problem with 'E-mail' fild"
            assert self.element_is_visible(LoginPageLocators.INPUT_PASS), \
                "Problem with 'Password' fild"
            assert self.element_is_visible(LoginPageLocators.BUTTON_CONTINUE), \
                "Problem with 'Continue' button"
            assert self.element_is_visible(LoginPageLocators.LOGIN_PASS_FORGOT), \
                "Problem with 'Privacy policy' reference"
            return True
        else:
            print("Page 'Login' is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Login' page.")
    def close_login_page(self):
        self.browser.back()
        print("Page 'Login' is closed")
