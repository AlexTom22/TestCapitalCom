from selenium.webdriver.common.by import By

class SignupLoginFormLocators:
	SIGNUP_FORM = (By.CSS_SELECTOR, "#s_overlay > div > button")
	SIGNUP_LOCATOR = (By.CSS_SELECTOR, "#s_overlay .signup-form a.l_btn_signup")
	BUTTON_CLOSE_ON_SIGNUP_FORM = (By.CSS_SELECTOR, "#s_overlay button.s_cancel")
	SIGNUP_FRAME = (By.CSS_SELECTOR, "#s_overlay > div > div.signup-form")
	SIGNUP_HEADER = (By.CSS_SELECTOR, "#s_overlay div.signup-form > div.form-container-small-header.s-between > div")
	SIGNUP_REF_LOGIN = (By.CSS_SELECTOR, "div.signup-form a.l_btn_signup")
	SIGNUP_INPUT_EMAIL = (By.CSS_SELECTOR, "#s_overlay-email > input")
	SIGNUP_INPUT_PASSWORD = (By.CSS_SELECTOR, "#s_overlay-pass > input")
	SIGNUP_SUBMIT_BTN = (By.CSS_SELECTOR, "#s_overlay .signup-form button[type=submit]")
	SIGNUP_PRIVACY_POLICY = (By.CSS_SELECTOR,
	                         "#s_overlay .form-container-small-footer a[href='/privacy-policy']")
	SIGNUP_PRIVACY_POLICY_DE_ASIC = (By.CSS_SELECTOR,
         "#s_overlay .form-container-small-footer a[href='https://capital.com/de/nutzungsbedingungen-und-richtlinien']")
	LOGIN_FRAME = (By.CSS_SELECTOR, "#l_overlay > div.form-container-small")
	LOGIN_HEADER = (By.CSS_SELECTOR, "#l_overlay div.form-container-small-header")
	LOGIN_REF_SIGNUP = (By.CSS_SELECTOR, "#l_overlay a.l_btn_signup")
	LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#l_overlay input[type='email']")
	LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#l_overlay input[type='password']")
	LOGIN_CHECKBOX = (By.CSS_SELECTOR, "#l_overlay .checkbox")
	LOGIN_CONTINUE = (By.CSS_SELECTOR, "#l_overlay button[type=submit]")
	LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay > div > button")
	LOGIN_LOCATOR = (By.CSS_SELECTOR, "#l_overlay > div input[type=checkbox]")
	LOGIN_PASS_FORGOT = (By.CSS_SELECTOR, "#l_overlay > div > div.form-container-small-footer > a.l_btn_forgot")
	BUTTON_CLOSE_ON_LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay > div > button")


class LoginPageLocators:
	LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay")
	REF_SIGNUP = (By.CSS_SELECTOR,
                  "#l_overlay a.l_btn_signup")
	INPUT_EMAIL = (By.CSS_SELECTOR, "#l_overlay input[type='email']")
	INPUT_PASS = (By.CSS_SELECTOR, "#l_overlay input[type='password']")
	LOGIN_CHECKBOX = (By.CSS_SELECTOR, "#l_overlay label.checkbox")
	BUTTON_CONTINUE = (By.CSS_SELECTOR, "#l_overlay button[type='submit']")
	LOGIN_PASS_FORGOT = (By.CSS_SELECTOR, "#l_overlay a.l_btn_forgot")


class SignupPageLocators:
	SIGNUP_FORM = (By.CSS_SELECTOR, "#testwrap > div.signup-form")
	REF_LOGIN = (By.CSS_SELECTOR,
	             "#testwrap > div.signup-form a[href='/trading/login']")
	INPUT_EMAIL = (By.CSS_SELECTOR, "#testwrap > .signup-form input[type='email']")
	INPUT_PASS = (By.CSS_SELECTOR, "#testwrap > .signup-form input[type='password']")
	BUTTON_CONTINUE = (By.CSS_SELECTOR, "#testwrap > .signup-form button[type='submit']")
	REF_PRIVACY_POLICY = (By.CSS_SELECTOR, "#s_overlay .form-container-small-footer a[href='/privacy-policy']")
