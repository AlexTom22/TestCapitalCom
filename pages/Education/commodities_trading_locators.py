from selenium.webdriver.common.by import By


class CommoditiesTradingPageLocator:
    # Pages
    # LOCATOR_COMMODITIES_TRADING_GUIDE = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(1)")
    #
    # LOCATOR_COMMODITIES_BRENT_CRUDE_OIL = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(2)")
    # LOCATOR_COMMODITIES_COFFEE = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(3)")
    # LOCATOR_COMMODITIES_COPPER = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(4)")
    # LOCATOR_COMMODITIES_CRUDE_OIL = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(5)")
    # LOCATOR_COMMODITIES_GOLD = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(6)")
    # LOCATOR_COMMODITIES_PALLADIUM = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(7)")
    # LOCATOR_COMMODITIES_PLATINUM = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(8)")
    # LOCATOR_COMMODITIES_SILVER = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(9)")
    # LOCATOR_COMMODITIES_US_NATURAL_GAS_SPOT = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a:nth-child(10)")
    # Or pages via find ELEMENT(S)
    # LOCATOR_COMMODITIES_PAGES = (By.CSS_SELECTOR, "sidebar-right > div.side-nav__wrap.js-sidenav > div.side-nav > a") # old
    LOCATOR_COMMODITIES_PAGES = (By.CSS_SELECTOR, "div.side-nav__wrap > div.side-nav > a") # new


    LOCATOR_COMMODITIES_TRADING_MAINBANNER_START_TRADING = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--darkText.js_signup")
    LOCATOR_COMMODITIES_TRADING_MAINBANNER_TRY_DEMO = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--emptyblack.js_signup.hideXs")
    # LOCATOR_COMMODITIES_TRADING_START_TRADING_IN_ARTICLE1 = (By.CSS_SELECTOR, "ul:nth-child(10) > li:nth-child(1) > a")
    # LOCATOR_COMMODITIES_TRADING_START_TRADING_IN_ARTICLE2 = (By.CSS_SELECTOR, "ul.list-row > li:nth-child(1) > a")
    # LOCATOR_COMMODITIES_TRADING_START_TRADING_IN_ARTICLE = (By.CSS_SELECTOR, "ul.list-row > li:nth-child(1) > a") # old
    LOCATOR_COMMODITIES_TRADING_START_TRADING_IN_ARTICLE = (By.CSS_SELECTOR, "ul > li:nth-child(1) > a") # new
    LOCATOR_COMMODITIES_TRADING_MOST_TRADED_1 = (By.CSS_SELECTOR, "div:nth-child(1) > div.mostTraded__market > a")
    LOCATOR_COMMODITIES_TRADING_MOST_TRADED_2 = (By.CSS_SELECTOR, "div:nth-child(2) > div.mostTraded__market > a")
    LOCATOR_COMMODITIES_TRADING_MOST_TRADED_3 = (By.CSS_SELECTOR, "div:nth-child(3) > div.mostTraded__market > a")
    LOCATOR_COMMODITIES_TRADING_MOST_TRADED_4 = (By.CSS_SELECTOR, "div:nth-child(4) > div.mostTraded__market > a")
    LOCATOR_COMMODITIES_TRADING_MOST_TRADED_5 = (By.CSS_SELECTOR, "div:nth-child(5) > div.mostTraded__market > a")
    LOCATOR_COMMODITIES_TRADING_STILL_LOOKING = (By.CSS_SELECTOR, "i.regSteps__item.js_signup")
    LOCATOR_COMMODITIES_TRADING_SELL = (By.CSS_SELECTOR, "a.button-main.sell.ln-auto.js_signup")
    LOCATOR_COMMODITIES_TRADING_BUY = (By.CSS_SELECTOR, "a.button-main.buy.ln-auto.js_signup")
    LOCATOR_COMMODITIES_STICKY_BAR = (By.CSS_SELECTOR, "div.encStickyBar > div > a")


# div.category.category--without-padding > div.inner-content-container.page-content-area > div > div.col-xs-12.col-sm-12.col-md-9.col-lg-9 > ul.list-row > li:nth-child(1) > a # Home page
# body > div.wrap > div.category > div.inner-content-container.page-content-area > div > div.col-xs-12.col-sm-12.col-md-9.col-lg-9 > ul.list-row > li:nth-child(1) > a # Brent Crude oil
# div.category > div.inner-content-container.page-content-area > div > div.col-xs-12.col-sm-12.col-md-9.col-lg-9 > ul.list-row > li:nth-child(1) > a # US natural gas spot
#
# div.category > div.inner-content-container.page-content-area > div > div.col-xs-12.col-sm-12.col-md-9.col-lg-9 > ul:nth-child(10) > li:nth-child(1) > a # Copper
# div.category > div.inner-content-container.page-content-area > div > div.col-xs-12.col-sm-12.col-md-9.col-lg-9 > ul:nth-child(38) > li:nth-child(1) > a # Copper




# ul.list-row > li:nth-child(1) > a # Brent Crude oil

# ul:nth-child(10) > li:nth-child(1) > a # Copper
# ul:nth-child(38) > li:nth-child(1) > a # Copper