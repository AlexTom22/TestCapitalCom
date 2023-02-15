from selenium.webdriver.common.by import By


class FinancialDictionary:
    ALPHABET_LIST_EN = (By.CSS_SELECTOR,
                        "glossaryWrapper > div.alphabet-list-container > div > div > span.alphabet-list-item")
    ITEM_LIST_EN = (By.CSS_SELECTOR, "div.alphabet-category-item > div.inner a")
