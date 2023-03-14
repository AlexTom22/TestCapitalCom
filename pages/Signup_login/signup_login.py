import time

import allure
from datetime import datetime
from pages.base_page import BasePage
from pages.Signup_login.signup_login_locators import (
    SignupFormLocators,
    LoginFormLocators,
    LoginPageLocators,
    SignupPageLocators
)


class SignupLogin(BasePage):

    @allure.step(f"{datetime.now()}.   Check that the 'Sign up' form is open.")
    def should_be_signup_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        if self.element_is_visible(SignupFormLocators.SIGNUP_FRAME):
            print(f"{datetime.now()}   'Sign up' form is opened")

            print(f"{datetime.now()}   SIGNUP_HEADER =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_HEADER), \
                "The layout of the 'SignUp' form has changed"
            
            print(f"{datetime.now()}   SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_REF_LOGIN), \
                "Problem with 'Login' reference"

            print(f"{datetime.now()}   SIGNUP_INPUT_EMAIL =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_INPUT_EMAIL), \
                "Problem with 'E-mail' fild"

            print(f"{datetime.now()}   SIGNUP_INPUT_PASSWORD =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_INPUT_PASSWORD), \
                "Problem with 'Password' fild"

            print(f"{datetime.now()}   SIGNUP_SUBMIT_BTN =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_SUBMIT_BTN), \
                "Problem with 'Continue' button"

            print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_2):
                
                print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_1 =>")
                if not self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                    assert False, f"Problem with 'Privacy policy' reference on '{cur_language}' language!"

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            return True
        else:
            print(f"{datetime.now()}   'Sign up' form is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Sign up' form.")
    def close_signup_form(self):
        self.element_is_clickable(SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 5)
        self.browser.find_element(*SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()
        print(f"{datetime.now()}.   'Sign up' form is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Sign up' page is open.")
    def should_be_signup_page(self, cur_language):
        """
        Check there are an elements to on 'Sign up' page
        """
        time.sleep(2)
        if self.current_page_is("https://capital.com/trading/signup"):
            print(f"{datetime.now()}   'Sign up' page is opened")

            print(f"{datetime.now()}   SIGNUP_SIGNUP_FORM =>")
            assert self.element_is_present(*SignupPageLocators.SIGNUP_FORM), \
                "The layout of the 'SignUp' page has changed"

            print(f"{datetime.now()}   SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(SignupPageLocators.REF_LOGIN), \
                "Problem with 'Login' reference"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(SignupPageLocators.INPUT_EMAIL), \
                "Problem with 'E-mail' fild"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(SignupPageLocators.INPUT_PASS), \
                "Problem with 'Password' fild"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(SignupPageLocators.BUTTON_CONTINUE), \
                "Problem with 'Continue' button"

            print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ALL_2):

                print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_1 =>")
                if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                    # if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_DE_1):
                    #     print(f"{datetime.now()}   SIGNUP_REF_LOGIN")
                    #
                    assert False, f"Problem with 'Privacy policy' reference on '{cur_language}' language!"

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            return True
        else:
            print(f"{datetime.now()}   'Sign up' page is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Sign up' page.")
    def close_signup_page(self):
        self.browser.back()
        print("'Sign up' page is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Login' form is open.")
    def should_be_login_form(self):
        """
        Check there are an elements to on Login form
        """
        if self.element_is_visible(LoginFormLocators.LOGIN_FRAME):
            print("'Login' form is opened")
            assert self.element_is_visible(LoginFormLocators.LOGIN_HEADER), \
                "The layout of the 'Login' form has changed"
            assert self.element_is_visible(LoginFormLocators.LOGIN_REF_SIGNUP), \
                "Problem with 'Sign up' reference"
            assert self.element_is_visible(LoginFormLocators.LOGIN_INPUT_EMAIL), \
                "Problem with 'Email address' fild"
            assert self.element_is_visible(LoginFormLocators.LOGIN_INPUT_PASSWORD), \
                "Problem with 'Password' fild"
            assert self.element_is_visible(LoginFormLocators.LOGIN_CHECKBOX), \
                "Problem with 'Log me out after 7 days' check box"
            assert self.element_is_visible(LoginFormLocators.LOGIN_CONTINUE), \
                "Problem with 'Continue' button"
            assert self.element_is_visible(LoginFormLocators.LOGIN_PASS_FORGOT), \
                "Problem with 'Forgot password' reference"
            return True
        else:
            print("'Login' form is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Login' form.")
    def close_login_form(self):
        self.element_is_clickable(LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM, 5)
        self.browser.find_element(*LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
        print("'Login' form is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Login' page is open.")
    def should_be_login_page(self):
        """
        Check there are elements to on SignUp page
        """
        time.sleep(2)
        if self.current_page_is("https://capital.com/trading/login"):
            print("'Login' page is opened")
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
                "Problem with 'Forgot password' reference"
            return True
        else:
            print("'Login' page is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Login' page.")
    def close_login_page(self):
        self.browser.back()
        print("'Login' page is closed")
