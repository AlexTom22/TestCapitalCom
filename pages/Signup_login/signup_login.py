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
            print("Form 'Sign up' is opened")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_HEADER), \
                "The layout of the 'SignUp' form has changed"
            assert self.element_is_visible(SignupFormLocators.SIGNUP_REF_LOGIN), \
                "Problem with 'Login' reference"
            assert self.element_is_visible(SignupFormLocators.SIGNUP_INPUT_EMAIL), \
                "Problem with 'E-mail' fild"
            assert self.element_is_visible(SignupFormLocators.SIGNUP_INPUT_PASSWORD), \
                "Problem with 'Password' fild"
            assert self.element_is_visible(SignupFormLocators.SIGNUP_SUBMIT_BTN), \
                "Problem with 'Continue' button"

            if cur_language == "ar":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_AR), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "bg":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_BG), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "cn":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_CN), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "cs":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_CS), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "da":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_DA), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "de":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_DE), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "el":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_EL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_EN), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "es":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ES), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "et":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ET), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "fi":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_FI), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "fr":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_FR), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "hr":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_HR), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "hu":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_HU), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "id":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ID), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "it":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_IT), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "lt":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_LT), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "lv":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_LV), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "nl":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_NL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "pl":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_PL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "pt":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_PT), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "ro":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_RO), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "ru":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_RU), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "sk":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_SK), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "sl":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_SL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "sv":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_SV), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "th":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_TH), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "vi":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_VI), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "zh":
                assert self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ZH), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"

            return True
        else:
            print("Form 'Sign up' is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Sign up' form.")
    def close_signup_form(self):
        self.element_is_clickable(SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 5)
        self.browser.find_element(*SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()
        print("Form 'Sign up' is closed")

    @allure.step(f"{datetime.now()}.   Check that the 'Sign up' page is open.")
    def should_be_signup_page(self, cur_language):
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

            if cur_language == "ar":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_AR), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "bg":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_BG), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "cn":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_CN), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "cs":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_CS), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "da":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_DA), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "de":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_DE), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "el":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_EL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_EN), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "es":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ES), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "et":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ET), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "fi":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_FI), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "fr":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_FR), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "hr":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_HR), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "hu":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_HU), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "id":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ID), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "it":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_IT), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "lt":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_LT), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "lv":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_LV), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "nl":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_NL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "pl":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_PL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "pt":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_PT), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "ro":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_RO), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "ru":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_RU), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "sk":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_SK), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "sl":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_SL), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "sv":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_SV), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "th":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_TH), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "vi":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_VI), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
            elif cur_language == "zh":
                assert self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ZH), \
                    f"Problem with 'Privacy policy' reference on '{cur_language}' language!"
           
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
        if self.element_is_visible(LoginFormLocators.LOGIN_FRAME):
            print("Form 'Login' is opened")
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
            print("Form 'Login' is not opened")
            return False

    @allure.step(f"{datetime.now()}.   Close the 'Login' form.")
    def close_login_form(self):
        self.element_is_clickable(LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM, 5)
        self.browser.find_element(*LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
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
