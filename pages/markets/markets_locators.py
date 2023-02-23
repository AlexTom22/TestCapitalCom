from selenium.webdriver.common.by import By


class OnTrastLocators:
    BUTTON_ACCEPT_ALL_COOKIE = (By.CSS_SELECTOR, "#onetrust-button-group > #onetrust-accept-btn-handler")


class CapitalPageLocators:
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ".cc-header__wrap #wg_loginBtn")
    BUTTON_TRADE_NOW = (By.CSS_SELECTOR, ".cc-header__wrap [data-type='btn_header']")
    HEADER_OF_CAPITAL_COM = (By.CSS_SELECTOR, ".cc-header__wrap")
    WIDGET_TRADING = (By.CSS_SELECTOR, ".tools > .tab-list")


class HeaderElementLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")
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
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "#l_overlay input[type='email']")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#l_overlay input[type='password']")
    LOGIN_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "label > input[type=checkbox]")
    LOGIN_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, "#l_overlay button[type=submit]")
    SIGNUP_REF_LOGIN_LOCATOR = (By.CSS_SELECTOR, "div.signup-form a.l_btn_signup")
    SIGNUP_INPUT_USERNAME_LOCATOR = (By.CSS_SELECTOR, "")
    SIGNUP_INPUT_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "")
    SIGNUP_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, "#s_overlay .signup-form button[type=submit]")


class MainBanner:
    TAB1 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='0']")
    TAB1_TRADE_NOW = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_trade_cfds']")
    TAB1_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_trade_cfds_demo']")
    TAB1_OPEN_ACCOUNT = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_spread_betting']")
    TAB1_START_TRADING = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_earnings']")
    TAB2 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='1']")
    TAB2_START_TRADING = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB2_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB2_TAKE_ME_THERE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_edu']")
    TAB3 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='2']")
    TAB3_L1_LEARN_MORE_ASIC = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_pro_au']")
    TAB3_L1_START_TRADING_ASIC = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_pro_au_demo']")
    TAB3_L2_START_TRADING_FCA = (By.CSS_SELECTOR,
                                 "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB3_L2_PRACTISE_FOR_FREE_FCA = (By.CSS_SELECTOR,
                                     "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22_demo']")
    TAB3_SHOW_ME_HOW = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_esg']")
    TAB4 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='3']")
    TAB4_EXPLORE_FEATURES = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='banner-tradingview']")


class MainBannerDe:
    BUTTON_LEFT = (By.CSS_SELECTOR, "div.banner--video a.btn[href='/trading/signup']")
    BUTTON_RIGH = (By.CSS_SELECTOR, "div.banner--video a.btn[href='/trading/signup?go=demo']")


class WidgetStillLookingFor:
    BUT_CREATE_YOUR_ACCOUNT_EN = (By.CSS_SELECTOR, "div.regSteps__shape > i.regSteps__item.js_signup")
    BUT_CREATE_YOUR_ACCOUNT_DE = (By.CSS_SELECTOR, "#cc_ab42 div.js_signup")


class WidgetPromoMarket:
    SLIDER_FADE = (By.CSS_SELECTOR, "div.js-sliderFade.cc-sliderFade")
    LIST_SLIDER_FADE_ITEMS = (By.CSS_SELECTOR, "div.cc-sliderFade__item")
    BUTTON_ON_ITEM = (By.CSS_SELECTOR, "div.promoMarket__col[data-type='wdg_singlemarket']")
    LIST_BUTTONS_TRADE_NOW = (By.CSS_SELECTOR, "div.promoMarket__col[data-type='wdg_singlemarket']")
    ACTIVE_BUTTON_TRADE_NOW = (By.CSS_SELECTOR, "div.active div.promoMarket__col[data-type='wdg_singlemarket']")
    LIST_BUTs_TRADE_NOW_2 = (By.CSS_SELECTOR,
                             ".cc-sliderFade__item > .promoMarket > .promoMarket__inner a.btn.js_signup_new")
    BUT_1_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(1) > .promoMarket > .promoMarket__inner a.btn.js_signup_new")
    BUT_2_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(2) > .promoMarket > .promoMarket__inner a.btn.js_signup_new")
    BUT_3_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(3) > .promoMarket > .promoMarket__inner a.btn.js_signup_new")
    BUT_4_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(4) > .promoMarket > .promoMarket__inner a.btn.js_signup_new")


class WidgetTradingInstrument:
    TABS_NAVIGATOR = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] > div.tabs__nav")
    FLAG_LAYOUT = (By.CSS_SELECTOR, "div.tools > div.tools__item--head > span:nth-child(3)")
    LIST_TABS_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-type='wdg_markets_tab']")
    BUT_MOST_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='mtr']")
    BUT_COMMOD_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='com']")
    BUT_CRYPTO_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='cryp']")
    BUT_INDICES_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='ind']")
    BUT_SHARES_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='shar']")
    BUT_FOREX_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='fx']")
    BUT_ETFS_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-tab-control='etf']")
    LIST_BUTTONS_TRADE_FOR_MTR_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='mtr'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_COM_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='com'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_IND_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='ind'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_CRY_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='cryp'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_SHAR_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='shar'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_FX_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='fx'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_ETF_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='etf'] td > a.js_signup_new")
    LIST_TABS_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item")
    BUT_MOST_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='Most']")
    BUT_COMMOD_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='Commodities']")
    BUT_CRYPTO_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='Crypto']")
    BUT_INDICES_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='Indices']")
    BUT_SHARES_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='Shares']")
    BUT_FOREX_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='Forex']")
    BUT_ETFS_2 = (By.CSS_SELECTOR, "div.tools > div.tab-list > a.tab-list__item[data-type='ETFs']")
    LIST_BUTTONS_TRADE_FOR_MTR_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Most a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_COM_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Commodities a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_IND_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Indices a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_CRY_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Crypto a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_SHAR_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Shares a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_FX_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Forex a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_ETF_2 = (By.CSS_SELECTOR, "div.tools div.ihome-ETFs a.js_signup_new")


class WidgetExploreOurPlatform:
    BUTTON_TRY_NOW_EN = (By.CSS_SELECTOR, ".js-analyticsVisible > a.btn.js_signup:nth-child(2)")
    BUTTON_TRY_NOW_DE = (By.CSS_SELECTOR, "div.explore a.button-main.js_signup")


class WidgetNewToTrading:
    SECTION_NEW_TO_TRADING_EN = (By.CSS_SELECTOR, "main > section.newToTrading")
    BUTTON_PRACTISE_FOR_FREE_EN = (By.CSS_SELECTOR, "section.newToTrading a.btn.js_signup")
    BUTTON_PRACTISE_FOR_FREE_DE = (By.CSS_SELECTOR, "div.newToTrade a.js_signup")


class WidgetTradingCalculator:
    BUTTON_START_TRADING = (By.CSS_SELECTOR, "#calcWrap div.tradingCalc__footer a.btn.js_signup_new")


class WidgetTradersDashboard:
    LIST_BUTTONS_TRADE = (By.CSS_SELECTOR, ".tradersDashboard button.js_signup")


class BannerOfCounters:
    BUTTON_1 = (By.CSS_SELECTOR, ".cc-counter__body > .btn.js_signup")
    BUTTON_2 = (By.CSS_SELECTOR, ".section--counter a.js_signup")


class WhyCapitalDe:
    BUTTON_TRADE_NOW_DE = (By.CSS_SELECTOR, "a.js_signup[data-type='hp_choose_capital']")


class BannerNewToTradingDe:
    BUTTON_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.side-video a.button-main")


class UserPanel:
    LOGOUT = (By.CSS_SELECTOR, "#userPanel div.logout-user")
    TRADING_PLATFORM = (By.CSS_SELECTOR, "#userPanel button.tradingPlatformBtn")
    CLOSE = (By.CSS_SELECTOR, "#userPanel span.user-panel-close")
