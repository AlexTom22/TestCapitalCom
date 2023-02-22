from selenium.webdriver.common.by import By


class FinancialDictionary:
    ALPHABET_LIST_EN = (By.CSS_SELECTOR,
                        "glossaryWrapper > div.alphabet-list-container > div > div > span.alphabet-list-item")
    ITEM_LIST_EN = (By.CSS_SELECTOR, "div.alphabet-category-item > div.inner a")


class ItemFinancialDictionary:
    VIDEO_IN_FRAME = (By.CSS_SELECTOR, "div.side-video.side-video--vertical video")
    BUTTON_IN_FRAME = (By.CSS_SELECTOR,
                       "div.side-video.side-video--vertical a[href='https://capital.com/trading/signup']")

    VER_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")
    HOR_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")


class WidgetStillLookingFor:
    BUT_CREATE_YOUR_ACCOUNT = (By.CSS_SELECTOR, "section.regSteps i.regSteps__item.js_signup")
    BUT_CREATE_YOUR_ACCOUNT_DE = (By.CSS_SELECTOR, "#cc_ab42 div.js_signup")


    