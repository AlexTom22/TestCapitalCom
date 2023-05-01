"""
-*- coding: utf-8 -*-
@Time    : 2023/04/13 18:25
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class HeaderButtonLoginLocators:
    """ Locators for ..."""
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")


class HeaderButtonTradeLocators:
    BUTTON_TRADE = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")


class VideoBannerLocators:
    VIDEO_BANNER = (By.CSS_SELECTOR, "div.side-video.side-video--vertical video")


class ButtonUnderVideoBannerLocators:
    BUTTON_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a[href='https://capital.com/trading/signup']")
    BUTTON_CREATE_ACCOUNT_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a.js_signup")


class VerHorBannerButtonLocators:
    VER_HOR_BANNER_BUTTON = (By.CSS_SELECTOR, ".grid  div.seo-banner a[href='/trading/signup']")

    # VER_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")
    # HOR_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")


class BlockStepTradingLocators:
    BUT_CREATE_YOUR_ACCOUNT = (By.CSS_SELECTOR, "section.regSteps i.regSteps__item.js_signup")
    BUT_CREATE_YOUR_ACCOUNT_DE = (By.CSS_SELECTOR, "#cc_ab42 div.js_signup")


class ButtonInBannerLocators:
    BUTTON_IN_BANNER = (By.CSS_SELECTOR, ".grid .detail__aside .inBanner > a")


class ButtonTradeOnWidgetMostTradedLocators:
    BUTTON_TRADED_1 = ()
    BUTTON_TRADED_2 = ()
    BUTTON_TRADED_3 = ()
    BUTTON_TRADED_4 = ()
    BUTTON_TRADED_5 = ()


class BlockOurCoursesLocators:
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "div [href='https://capital.com/trading/signup']")


class CommoditiesPageElements:
    BUTTONS_COMMODITIES_PAGES = (By.CSS_SELECTOR, "div.side-nav__wrap > div.side-nav > a")
    BUTTON_START_TRADING_IN_ARTICLE = (By.CSS_SELECTOR, "ul > li:nth-child(1) > a.js_signup")
    BUTTON_TRADING_SELL = (By.CSS_SELECTOR, "a.button-main.sell.ln-auto.js_signup")
    BUTTON_TRADING_BUY = (By.CSS_SELECTOR, "a.button-main.buy.ln-auto.js_signup")
    BUTTON_ON_STICKY_BAR = (By.CSS_SELECTOR, "div.encStickyBar > div > a")


class MainBanner:
    BUTTON_START_TRADING = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--darkText.js_signup")
    BUTTON_TRY_DEMO = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--emptyblack.js_signup.hideXs")
