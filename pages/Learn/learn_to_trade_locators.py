from selenium.webdriver.common.by import By


class LearnToTradePageLocator:
    LOCATOR_LEARN_TO_TRADE_TEXT = (By.CSS_SELECTOR, "div.wrap>nav>span")
    LOCATOR_LEARN_TO_TRADE_LOGIN_BUTTON = (By.ID,
                                           "wg_loginBtn")
    LOCATOR_LEARN_TO_TRADE_TRADE_NOW_BUTTON = (By.CLASS_NAME,
                                               "cc-header__signup btn btn--sm btn--darkText hideSm js_signup")
    LOCATOR_LEARN_TO_TRADE_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON = (By.CLASS_NAME, 'regSteps__item js_signup')
