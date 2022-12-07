from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from time import sleep
import datetime


def pars_link_for_element_with_special_href(dr, link_loc):
    dr.get(link_loc)

    # "Log in"
    css_loc = "#wg_loginBtn"
    test_role1_element_login(dr, link_loc, css_loc)

    # "Trade Now"
    css_loc = ".cc-header__signup"
    test_role1_element_signup(dr, link_loc, css_loc)

    # "#wphWrap > a.cc-header__signup.btn.btn--sm.btn--darkText.hideSm.js_signup",

    # "[href$='?side=sell']",

    # "[href$=?side=buy']",

    # "[data-href$='?side=sell']",
    # "[data-href$='?side=buy']",
    # "[href$='/trading/signup?go=demo']",
    # "[href$='/trading/platform']",


def test_role1_element_login(
        dr, link_cur, css_loc
):
    elements = dr.find_elements(By.CSS_SELECTOR, css_loc)
    print(f"На странице {link_cur} имеется {len(elements)} элемент(ов) с "
          f"css локатором {css_loc}")
    for element in elements:
        print(element.text)
        test_role1_window_login(dr, element)


def test_role1_element_signup(
        dr, link_cur, css_loc
):
    elements = dr.find_elements(By.CSS_SELECTOR, css_loc)
    print(f"На странице {link_cur} имеется {len(elements)} элемент(ов) с "
          f"css локатором {css_loc}")
    for element in elements:
        print(element.text)
        test_role1_window_signup(dr, element)


# Тест на открытие поп-ап окна "Log in" для незарегистрированного пользователя
def test_role1_window_login(
    dr, parent_element
):
    parent_element.click()
    # sleep(1)
    css_loc = "#l_overlay>div.modal>div.form-container-small-content>" \
              "form>div.step0>div.field>#l_f_email>input"
    elements = dr.find_elements(By.CSS_SELECTOR, css_loc)
    if len(elements) != 0:
        name_form = elements[0].text
        print(name_form)
        css_loc = "#l_overlay > div > button"
        dr.find_element(By.CSS_SELECTOR, css_loc).click()
    else:
        assert_message = (
            "Ожидаемое 'Log in' окно не открылось"
        )
        assert len(elements) != 0, assert_message


# Тест на открытие поп-ап окна "Log in" для незарегистрированного пользователя
def test_role1_window_signup(
    dr, parent_element
):
    parent_element.click()
    css_loc = "#s_overlay>div.modal>div.signup-form>" \
              "div.form-container-small-content>form>div.field>#s_overlay-email>input"
    elements = dr.find_elements(By.CSS_SELECTOR, css_loc)
    if len(elements) != 0:
        name_form = elements[0].text
        print(name_form)

        css_loc = "#s_overlay > div.modal > button.s_cancel"
        dr.find_element(By.CSS_SELECTOR, css_loc).click()
    else:
        assert_message = (
            "Ожидаемое 'Sign up' окно не открылось"
        )
        assert len(elements) != 0, assert_message


try:
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,720")
    # options.add_argument("--window-size=1920,1080")
    options.headless = False
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    browser.implicitly_wait(10)
    print(f"{datetime.datetime.now()} - Начало работы скрипта capital2")

    # Исходные данные для тестирования
    date_job = "2022-11-25"
    # Роль - пока устанавливается авторизацией и согласием использовать куку
    # Лицензия
    # licence_job = "https://capital.com/?license=ASIC"
    licence_job = "https://capital.com/?license=FCA"
    # licence_job = "https://capital.com/?license=CYSEC"
    # licence_job = "https://capital.com/?license=NBRB"
    # licence_job = "https://capital.com/?license=CCSTV"
    # licence_job = "https://capital.com/?license=SEY"
    # Локация
    locs_job = ["ar"]

    for loc_shtamp in locs_job:
        name_file = (
            "txt/"
            + date_job
            + "/"
            + loc_shtamp
            + "/"
            + date_job
            + " "
            + loc_shtamp
            + " "
            + "link_of_capital_com.txt"
        )
        links_list = list()
        file = open(name_file, "r")
        for line in file:
            links_list.append(line)
        file.close()

        browser.get(licence_job)
        for link in links_list:
            pars_link_for_element_with_special_href(browser, link)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
