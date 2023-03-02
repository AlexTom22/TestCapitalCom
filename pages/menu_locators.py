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

    SUB_MENU_BG_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Как да търгувате']")
    SUB_MENU_BG_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/bg/finansov-rechnik']")

    SUB_MENU_CS_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Naučte se obchodovat']")
    SUB_MENU_CS_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/cs/financni-slovnik']")

    SUB_MENU_FR_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Apprendre à trader']")
    SUB_MENU_FR_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/fr/dictionnaire-financier']")


class MenuUS03:

    SUB_MENU_EN_ITEM_LEARN_TO_TRADE = (By.XPATH, "/html/body/header/div[4]/div[2]/nav/div[1]/div[4]/a")
    SUB_MENU_DE_ITEM_LEARN_TO_TRADE = (By.XPATH, "/html/body/header/div[4]/div[2]/nav/div[1]/div[4]/a")
    SUB_MENU_RU_ITEM_LEARN_TO_TRADE = (By.XPATH, "/html/body/header/div[4]/div[2]/nav/div[1]/div[4]/a")
    SUB_MENU_BG_ITEM_LEARN_TO_TRADE = (By.XPATH, "/html/body/header/div[4]/div[2]/nav/div[1]/div[4]/a")
    SUB_MENU_CS_ITEM_LEARN_TO_TRADE = (By.XPATH, "/html/body/header/div[4]/div[2]/nav/div[1]/div[4]/a")
    SUB_MENU_FR_ITEM_LEARN_TO_TRADE = (By.XPATH, "/html/body/header/div[4]/div[2]/nav/div[1]/div[4]/a")
