from selenium.webdriver.common.by import By

class OnTrastLocators:
	BUTTON_ACCEPT_ALL_COOKIE = (By.CSS_SELECTOR, "#onetrust-button-group > #onetrust-accept-btn-handler")
	BUTTON_REJECT_ALL_COOKIE = (By.CSS_SELECTOR, "#onetrust-button-group > #onetrust-reject-all-handler")


class LearnToTradePageLocator:
    HEADER_OF_LEARN_TO_TRADE_CURL = ()
    LOCATOR_LEARN_TO_TRADE_TEXT = (By.CLASS_NAME, 'cc-breadcrumbs')
    LOCATOR_LEARN_TO_TRADE_LOGIN_BUTTON = (By.CLASS_NAME,
                                           'cc-header__login btn btn--sm btn--emptyblack hideSm js-login ln-auto')
    LOCATOR_LEARN_TO_TRADE_TRADE_NOW_BUTTON = (By.CLASS_NAME, 'cc-header__signup btn btn--sm'
                                                              ' btn--darkText hideSm js_signup ')
    LOCATOR_LEARN_TO_TRADE_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON = (By.CLASS_NAME, 'regSteps__item js_signup')
