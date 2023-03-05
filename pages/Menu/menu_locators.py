from selenium.webdriver.common.by import By


class Menu:
    MENU = (By.CSS_SELECTOR, "button.js-burger")


class MenuUS05:
    SUB_MENU_BG_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Как да търгувате']")
    SUB_MENU_BG_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/bg/finansov-rechnik']")

    SUB_MENU_CS_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Naučte se obchodovat']")
    SUB_MENU_CS_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/cs/financni-slovnik']")

    SUB_MENU_DA_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Lær at handle']")
    SUB_MENU_DA_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/da/finansiel-ordbog']")

    SUB_MENU_DE_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Traden lernen']")
    SUB_MENU_DE_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/de/finanzglossar']")

    SUB_MENU_EL_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Μάθετε να επενδύετε']")
    SUB_MENU_EL_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/el/xromatooikonomiko-leksiko']")

    SUB_MENU_EN_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Learn to trade']")
    SUB_MENU_EN_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/financial-dictionary']")

    SUB_MENU_ES_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Aprende a hacer trading']")
    SUB_MENU_ES_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/es/diccionario-financiero']")

    SUB_MENU_ET_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Õpi kauplema']")
    SUB_MENU_ET_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/et/finantssonastik']")
    
    SUB_MENU_FI_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Opi kauppaan']")
    SUB_MENU_FI_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/fi/rahoitusalan-sanasto']")

    SUB_MENU_FR_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Apprendre à trader']")
    SUB_MENU_FR_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/fr/dictionnaire-financier']")

    SUB_MENU_RU_LEARN_TO_TRADE = (By.CSS_SELECTOR, "button[data-target='Курсы и обучение']")
    SUB_MENU_RU_GLOSSARY = (By.CSS_SELECTOR,
                            "div.js-navSide.active>div>a[href='https://capital.com/ru/finansovyy-slovar']")
