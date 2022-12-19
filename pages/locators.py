from selenium.webdriver.common.by import By


class OnTrastLocators:
    BUTTON_ACCEPT_ALL_COOKIE = (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")


class CapitalPageLocators:
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ".cc-header__wrap #wg_loginBtn")
    BUTTON_TRADE_NOW = (By.CSS_SELECTOR, ".cc-header__wrap [data-type='btn_header']")
    HEADER_OF_CAPITAL_COM = (By.CSS_SELECTOR, ".cc-header__wrap")
    WIDGET_TRADING = (By.CSS_SELECTOR, ".tools > .tab-list")


class HeaderElementLocators:
    BUTTON_LOGIN_LOCATOR = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")
    # BUTTON_LOGIN = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_login")
    BUTTON_SIGNUP_LOCATOR = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")
    BUTTON_SIGNUP = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")


class FooterElementLocators:
    pass


class SignupLoginFormLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay > div > button")
    SIGNUP_FORM = (By.CSS_SELECTOR, "#s_overlay > div > button")
    LOGIN_LOCATOR = (By.CSS_SELECTOR, "#l_overlay > div input[type=checkbox]")
    SIGNUP_LOCATOR = (By.CSS_SELECTOR, "#s_overlay .signup-form a.l_btn_signup")
    BUTTON_CLOSE_ON_LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay > div > button")
    BUTTON_CLOSE_ON_SIGNUP_FORM = (By.CSS_SELECTOR, "button.s_cancel")

    LOGIN_REF_SIGNUP_LOCATOR = (By.CSS_SELECTOR, "#l_overlay a.l_btn_signup")
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "")
    LOGIN_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "label > input[type=checkbox]")
    LOGIN_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, "#l_overlay form > button[type=submit]")
    SIGNUP_REF_LOGIN_LOCATOR = (By.CSS_SELECTOR, "div.signup-form a.l_btn_signup")
    SIGNUP_INPUT_USERNAME_LOCATOR = (By.CSS_SELECTOR, "")
    SIGNUP_INPUT_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "")
    SIGNUP_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, "#s_overlay .signup-form button[type=submit]")


class MainBaner:
    TAB_0 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='0']")
    TAB_1 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='1']")
    TAB_2 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='2']")
    TAB_3 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='3']")
    TAB_0_TRADE_NOW = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_cfd']")
    TAB_0_OPEN_ACCOUNT = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_spread_betting']")
    TAB_0_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_cfd_demo']")
    TAB_1_START_TRADING = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB_1_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB_2_SHOW_ME_HOW = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_esg']")
    TAB_3_EXPLORE_FEATURES = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='banner-tradingview']")


class WidgetStillLookingFor:
    BUT_CREATE_YOUR_ACCOUNT = (By.CSS_SELECTOR, "div.regSteps__shape > i.regSteps__item.js_signup")


class WidgetPromoMarket:
    SLIDER_FADE = (By.CSS_SELECTOR, "div.js-sliderFade.cc-sliderFade")
    BUTTON_TRADE_NOW = (By.CSS_SELECTOR, "div.promoMarket__col[data-type='wdg_singlemarket']")

    