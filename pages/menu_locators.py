from selenium.webdriver.common.by import By


class Menu:
    MENU = (By.CSS_SELECTOR, "button.js-burger")

    SUB_MENU_EN_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Learn to trade']")
    SUB_MENU_EN_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/financial-dictionary']")

    SUB_MENU_DE_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Traden lernen']")
    SUB_MENU_DE_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/de/finanzglossar']")

    SUB_MENU_RU_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Курсы и обучение']")
    SUB_MENU_RU_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/ru/finansovyy-slovar']")

    # SUB_MENU = (By.CSS_SELECTOR, "")
    # SUB_MENU = (By.CSS_SELECTOR, "")
    # SUB_MENU = (By.CSS_SELECTOR, "")
    # SUB_MENU = (By.CSS_SELECTOR, "")
