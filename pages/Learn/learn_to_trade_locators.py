from selenium.webdriver.common.by import By


class LearnToTradePageLocator:
    LOCATOR_LEARN_TO_TRADE_TEXT = (By.CSS_SELECTOR, "div.wrap>nav>span")
    LOCATOR_LEARN_TO_TRADE_LOGIN_BUTTON = (By.ID,
                                           "wg_loginBtn")
    LOCATOR_LEARN_TO_TRADE_TRADE_NOW_BUTTON = (By.CSS_SELECTOR,
                                               "div.cc-header__wrap > div#wphWrap a.cc-header__signup")
    LOCATOR_LEARN_TO_TRADE_CREATE_VERIFY_YOUR_ACCOUNT_BUTTON = (By.CSS_SELECTOR,
                                                                'div.regSteps__shape > i.regSteps__item.js_signup')
