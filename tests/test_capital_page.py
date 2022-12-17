import pytest
# from pyautogui import alert
from pages.header_element import HeaderElement
from pages.capital_page import CapitalPage
from pages.signup_login_form import SignupLoginForm
from src.src import (
    TradingViewPageSrc,
    ESGPageSrc,
)


start_link = "http://capital.com/"
test_link = "?"
prev_role = "?"
prev_license = "?"
prev_language = "?"
page = None
accept_all_cookies = False


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
        # "ar",
        # "bg",
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

    def preconditions(self, d, cur_login, cur_password, cur_role, cur_language, cur_license):
        global start_link
        global test_link
        global prev_role
        global prev_license
        global prev_language
        global page
        global accept_all_cookies

        # Настраиваем в соответствии с параметром "Роль"
        if cur_role != prev_role:
            if cur_role == "NoReg":
                pass
            elif cur_role == "Reg_NoAuth":
                self.to_do_registration(d, cur_login, cur_password)
            elif cur_role == "Auth":
                self.to_do_authorization(d, cur_login, cur_password)
            else:
                print(f"Задан не существующий параметр роли - '{cur_role}'.\nТест будет выполнять с ролью 'NoReg'")
                prev_role = "NoReg"

        # устанавливаем Лицензию
        if cur_license != prev_license:
            license_url = f"{start_link}?{cur_license}"
            page = CapitalPage(d, license_url)
            page.open_page()
            prev_license = cur_license
            # check установленной лицензии

        # устанавливаем Язык
        if cur_language != prev_language:
            url_language = f"{start_link}{cur_language}"
            test_link = url_language
            page = CapitalPage(d, test_link)
            page.open_page()
            prev_language = cur_language
            # Check установленного языка

        # # Accept All Cookies if not accepted
        # if not accept_all_cookies:
        #     page.click_button_accept_all_cookies()
        #     accept_all_cookies = True
        #
    def test_header_button_login(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        global test_link
        global page

        self.preconditions(d, cur_login, cur_password, cur_role, cur_language, cur_license)

        page = CapitalPage(d, test_link)
        page.open_page()
        # page.check_that_cur_page_has_header()

        page = HeaderElement(d, test_link)
        page.click_button_login_on_header()

        if cur_role == "NoReg":
            page = SignupLoginForm(d, test_link)
            page.should_be_login_frame()
            page.close_login_frame()

    def test_header_button_trade_now(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        global test_link
        global page

        print(cur_license, cur_language, cur_role, cur_login, cur_password)

        page = HeaderElement(d, test_link)
        page.click_button_signup_on_header()

        if cur_role == "NoReg":
            page = SignupLoginForm(d, test_link)
            page.should_be_signup_frame()
            page.close_signup_frame()

    def test_main_banner_tab_0_button_open_accaunt(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Spread betting" -> button "Open account"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(cur_license, cur_language, cur_role, cur_login, cur_password)
        page = CapitalPage(d, test_link)
        page.open_page()

        page.click_tab_0_on_main_banner()
        page.click_tab_0_button_open_account()

        if cur_role == "NoReg":
            # Проверяем, что открылась форма SignUP
            page = SignupLoginForm(d, test_link)
            page.should_be_signup_frame()
            page.close_signup_frame()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            pass

    def test_main_banner_tab_1_button_start_trading(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading ..." -> button "Start trading"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(cur_license, cur_language, cur_role, cur_login, cur_password)
        page = CapitalPage(d, test_link)
        page.open_page()

        page.click_tab_1_on_main_banner()
        page.click_tab_1_button_start_trading()

        if cur_role == "NoReg":
            # Проверяем, что открылась форма SignUP
            page = SignupLoginForm(d, test_link)
            page.should_be_signup_frame()
            page.close_signup_frame()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            pass

    def test_main_banner_tab_1_button_practise_for_free(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Industry-leading ..." -> button "Practice for free"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(cur_license, cur_language, cur_role, cur_login, cur_password)
        page = CapitalPage(d, test_link)
        page.open_page()

        page.click_tab_1_on_main_banner()
        page.click_tab_1_button_practise_for_free()

        if cur_role == "NoReg":
            page = SignupLoginForm(d, test_link)
            page.should_be_signup_frame()
            page.close_signup_frame()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            pass

    def test_main_banner_tab_2_button_show_me_how(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Don't "trade off" your values." -> button "Show me how"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(cur_license, cur_language, cur_role, cur_login, cur_password)
        page = CapitalPage(d, test_link)
        page.open_page()

        page.click_tab_2_on_main_banner()
        page.click_tab_2_button_show_me_how()

        if cur_role == "NoReg":
            # Проверяем, что открылась page ESG
            page = CapitalPage(d, ESGPageSrc.URL)
            page.open_page()
            page.check_open_esg_page()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            pass

    def test_main_banner_tab_3_button_explore_features(
            self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    ):
        """
        Check: tab "Find us on ..." -> button "Explore features"
        Licence: FCA. Language - EN.
        """
        global test_link
        global page

        print(cur_license, cur_language, cur_role, cur_login, cur_password)
        page = CapitalPage(d, test_link)
        page.open_page()

        page.click_tab_3_on_main_banner()
        page.click_tab_3_button_explore_features()

        if cur_role == "NoReg":
            # Проверяем, что открылась страница https://www.tradingview.com/broker/Capitalcom/
            page = CapitalPage(d, TradingViewPageSrc.URL)
            page.open_page()
            page.check_open_tradingview_page()
        elif cur_role == "Reg_NoAuth":
            pass
        elif cur_role == "Auth":
            pass

    # def test_main_banner_tab_0_button_trade_now(
    #         self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    # ):
    #     """Check tab "Get Involved.": button "Trade Now" """
    #     global test_link
    #     global page
    #     cur_login = cur_login
    #     cur_password = cur_password
    #     cur_license = cur_license
    #     cur_language = cur_language
    #
    #     page = CapitalPage(d, test_link)
    #     # Click on Tab_0
    #     page.click_tab_0_on_main_banner()
    #     # Click button "Trade Now"
    #     page.click_trade_now_on_tab_0()
    #
    #     if cur_role == "NoReg":
    #         # Проверяем, что открылась форма SignUP
    #         page = SignupLoginForm(d, test_link)
    #         page.should_be_signup_frame()
    #         page.close_signup_frame()
    #     elif cur_role == "Reg_NoAuth":
    #         pass
    #     elif cur_role == "Auth":
    #         pass
    #
    # def test_main_banner_tab_0_button_practise_for_free(
    #         self, d, cur_login, cur_password, cur_role, cur_language, cur_license
    # ):
    #     """Check tab "Get Involved.": button "Practise for free" """
    #     global test_link
    #     global page
    #     cur_login = cur_login
    #     cur_password = cur_password
    #     cur_license = cur_license
    #     cur_language = cur_language
    #
    #     page = CapitalPage(d, test_link)
    #     # Click Tab_0
    #     page.click_tab_0_on_main_banner()
    #     # Click button "Practise for free"
    #     page.click_practise_for_free_on_tab_0()
    #
    #     if cur_role == "NoReg":
    #         # Проверяем, что открылась форма SignUP
    #         page = SignupLoginForm(d, test_link)
    #         page.should_be_signup_frame()
    #         page.close_signup_frame()
    #     elif cur_role == "Reg_NoAuth":
    #         pass
    #     elif cur_role == "Auth":
    #         pass

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
