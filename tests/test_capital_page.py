import time
import pytest
from pages.header_element import HeaderElement
from pages.capital_page import CapitalPage
from pages.signup_login_form import SignupLoginForm


start_link = "http://capital.com/"
test_link = ""
prev_license = ""
prev_language = ""
page = None


@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("qa.tomelo.an@gmail.com", "???"),
    ], scope="class"
)
@pytest.mark.parametrize(
    "cur_role",
    [
        "NoReg",
        # "Reg_NoAuth",
        # "Auth",
    ], scope="class"
)
@pytest.mark.parametrize(
    "cur_language",
    [
        "",
        "ar",
        "bg",
        # "cn",
        # "cs",
        # "da",
        # "de",
        # "el",
        # "as",
        # "et",
        # "fi",
        # "fr",
        # "hr",
        # "id",
        # "lt",
        # "lv",
        # "nl",
        # "pl",
        # "pt",
        # "ro",
        # "ru",
        # "sk",
        # "sl",
        # "sv",
        # "th",
        # "vi",
        # "zh",
    ], scope="class"
)
@pytest.mark.parametrize(
    "cur_license",
    [
        # "license=ASIC",
        "license=FCA",
        # "license=CYSEC",
        # "license=NBRB",
        # "license=CCSTV",
        # "license=SEY",
    ], scope="class"
)
class TestSample:

    def test_preconditions(self, d, cur_login, cur_password, cur_role, cur_language, cur_license):
        global start_link
        global test_link
        global prev_license
        global prev_language
        global page

        # Настраиваем в соответствии с параметром "Роль"
        if cur_role == "NoReg":
            pass
        elif cur_role == "Reg_NoAuth":
            self.to_do_registration(d, cur_login, cur_password)
        elif cur_role == "Auth":
            self.to_do_authorization(d, cur_login, cur_password)
        else:
            print(f"Задан не существующий параметр роли - '{cur_role}'.\nТест будет выполнять с ролью 'NoReg'")
            cur_role = "NoReg"

        # устанавливаем Лицензию
        # if cur_license != prev_license:
        if True:
            license_url = f"{start_link}?{cur_license}"
            page = CapitalPage(d, license_url)
            page.open_page()
            prev_license = cur_license
            # check установленной лицензии

        # устанавливаем Язык
        # if cur_language != prev_language:
        if True:
            url_language = f"{start_link}{cur_language}"
            test_link = url_language
            page = CapitalPage(d, test_link)
            page.open_page()
            prev_language = cur_language
            # Check установленного языка

        assert True

    def test_header_button_login(self, d, cur_login, cur_password, cur_role, cur_language, cur_license):
        global test_link
        global page
        cur_login = cur_login
        cur_password = cur_password
        cur_cur_role = cur_role
        cur_license = cur_license
        cur_language = cur_language

        # Checks that the current test object has cur parametrs

        page = CapitalPage(d, test_link)
        page.open_page()
        time.sleep(1)
        page.check_that_cur_page_has_header()

        # нажимаем кнопку "Log in"
        page = HeaderElement(d, test_link)
        page.click_button_login_on_header()
        time.sleep(1)

        # проверяем, открылась ли Login форма
        page = SignupLoginForm(d, test_link)
        page.should_be_login_frame()
        page.close_login_frame()

    def test_header_button_trade_now(self, d, cur_login, cur_password, cur_role, cur_language, cur_license):
        global test_link
        global page
        cur_login = cur_login
        cur_password = cur_password
        cur_cur_role = cur_role
        cur_license = cur_license
        cur_language = cur_language

        # Checks that the current page is Capital.com
        page = CapitalPage(d, test_link)
        page.open_page()
        time.sleep(1)
        page.check_that_cur_page_has_header()

        # нажимаем кнопку "Sign up"
        page = HeaderElement(d, test_link)
        page.click_button_signup_on_header()
        time.sleep(1)

        # проверяем, открылась ли "Sign up" форма
        page = SignupLoginForm(d, test_link)
        page.should_be_signup_frame()
        page.close_signup_frame()

    #
    # def test_main_banner_tab1_button_start_trading(self, d):
    #     pass
    #
    # def test_main_banner_tab1_button_practise_for_free(self, d):
    #     pass
    #
    # def test_main_banner_tab2_button_show_me_how(self, d):
    #     pass
    #
    # def test_main_banner_tab3_button_open_accaunt(self, d):
    #     pass
    #
    # def test_main_banner_tab3_button_try_free_demo(self, d):
    #     pass
    #
    # def test_main_banner_tab4_button_explore_features(self, d):
    #     pass

    # Widget “Trading instrument”
    # @pytest.mark.parametrize(
    #     "tab_instrument",
    #     [
    #         "Most",
    #         "Commodities",
    #         "Indices",
    #         "Crypto",
    #         "Shares",
    #         "Forex",
    #         "ETFs",
    #     ],
    # )
    # def test_widget_trading_instrument_button_trade(self, d, tab_instrument):
    #     global link
    #     global page
    #
    #     # проверка табов
    #     page = CapitalPage(d, link)
    #     page.check_buttons_trade_on_select_tab(tab_instrument)

    # авторизация пользователя
    # def to_do_authorization(self, d, test_link, test_login, test_password):
    #     global link
    #     global page
    #     assert test_login != "", "Авторизация невозможна. Не указан e-mail"
    #     assert test_password != "", "Авторизация невозможна. Не указан пароль"
    #     # нажать в хедере на кнопку "Log in"
    #     page = HeaderElement(d, test_link)
    #     # page.open_page()
    #     page.click_button_login_on_header()
    #     # проверить, открылась ли форма "Log in"
    #     # ввести логин, вести пароль, нажать подтвердить

    # регистрация пользователя
    # def to_do_registration(self, d, cur_login, cur_password):
    #     global link
    #     global page
    #     assert cur_login != "", "Регистрация невозможна. Не указан e-mail"
    #     assert cur_password != "", "Регистация невозможна. Не указан пароль"
    #     # нажать в хедере на кнопку "Log in"
    #     # page = HeaderElement(d, test_link)
    #     # page.open_page()
    #     page.click_button_login_on_header()
    #     # проверить, открылась ли форма "Log in"
    #     # перейти на форму "Sigup", нажав кнопку "SignUp"
    #     # проверить, открылась ли форма "SignUp"
    #     # ввести логин, вести пароль, нажать подтвердить
