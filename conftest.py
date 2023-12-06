"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import pytest
import os
import random
import conf
import allure
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

test_browser = ""

# def pytest_addoption(parser):
#     # parser.addoption("--cur_language", action="store_true", default="", help="run with language parameter")
#     language = metafunc.config.getoption("--cur_language")


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        "Auth",
        "Reg/NoAuth",
    ],
)
def cur_role(request):
    """Fixture"""
    print(f"\n\n\nCurrent test role - {request.param}")
    return request.param


# Language parameter
@pytest.fixture(
    scope="class",
    params=[
        # "",  # "en"
        # "ar",
        "de",
        # "el",
        # "es",
        # "fr",
        # "it",
        # "hu", # Magyar
        # "nl",
        # "pl",
        # "ro",
        # "ru",
        # "zh",
        # "cn",  # Education to trade present, financial glossary not present
    ],
)
def cur_language(request):
    """Fixture"""
    # language = request.config.getoption("--cur_language")
    language = request.param
    print(f"Current test language - {language}")
    return language


# Country/License parameter
@pytest.fixture(
    scope="class",
    params=[
        "gb",  # United Kingdom - "FCA"
        # "de",  # Germany - "CYSEC"
        # "ae",  # United Arab Emirates - "SCB"
        # "au",  # Australia - "ASIC"

        # "gr",  # Greece - "CYSEC"
        # "es",  # Spain - "CYSEC"
        # "fr",  # France - "CYSEC"
        # "it",  # Italy - "CYSEC"
        # "hu",  # Hungary - "CYSEC"
        # "nl",  # Netherlands - "CYSEC"
        # "pl",  # Poland - "CYSEC"
        # "ro",  # Romania - "CYSEC"
        # "tw",  # Taiwan - "SCB"
        # "hk",  # Hong Kong - "SCB"

        # # "ru" - not support
        # "NBRB" - not support
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    """Fixture"""
    print(f"Current country of trading - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "aqa.tomelo.an@gmail.com",
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "iT9Vgqi6d$fiZ*Z",
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture()
def prob_run_tc():
    """
    Fixture for реализации вероятности выполнения теста
    """
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


def pre_go(fixture_value):
    global test_browser
    test_browser = fixture_value
    return None


@pytest.fixture(
    scope="module",
    params=[
        "chrome",
        # "edge",
        # "firefox",
        # "safari",
    ],
    autouse=True,
    ids=pre_go,
)
def go(request, d):
    """Start execution program"""
    print(f'autouse fixture {request.param}')
    # d.get(conf.URL)

    yield d

    d.quit()
    print("\n*** end fixture = teardown ***\n")


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.fixture(scope="module")
# def d(browser):
def d():
    """WebDriver Initialization"""
    global test_browser
    browser = test_browser
    driver = None
    if browser == "chrome":
        driver = init_remote_driver_chrome()
    elif browser == "edge":
        driver = init_remote_driver_edge()
    elif browser == "firefox":
        driver = init_remote_driver_firefox()
    elif browser == "safari":
        driver = init_remote_driver_safari()
    elif browser == "opera":
        pass
    else:
        print('Please pass the correct browser name: {}'.format(browser))
        raise Exception('driver is not found')
    return driver


def init_remote_driver_chrome():
    # chrome_version = "114.0.5735.90"
    # chrome_version = "115.0.5790.102" - версия chromium CFT
    # chrome_version = "115.0.5790.114"
    # chrome_version = "116.0.5845.96"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = "eager"
    # chrome_options.page_load_strategy = "normal"
    chrome_options.add_argument(conf.CHROME_WINDOW_SIZES)
    # chrome_options.add_argument(conf.CHROME_WINDOW_SIZES_4k)

    # Код, отмены информационного сообщения "USB: usb_device_handle_win.cc"
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--accept-lang=en")

    # !!!
    # безголовый режим задается переменной headless в самом начале текущего модуля
    if conf.HEADLESS:
        chrome_options.add_argument(conf.CHROMIUM_HEADLESS)

    # driver = webdriver.Chrome(executable_path='/home/trendsen/virtualenv/GoogleTrendsBOT/3.8/bin/chromedriver',
    #                           options=options)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager(version=chrome_version).install()), options=chrome_options
    # )

    print(driver.get_window_size())
    driver.implicitly_wait(4)
    return driver


def init_remote_driver_edge():
    edge_options = webdriver.EdgeOptions()
    edge_options.page_load_strategy = "eager"  # 'normal'
    # edge_options.add_argument(conf.WINDOW_SIZES)
    edge_options.add_argument(conf.CHROMIUM_WINDOW_WIDTH)
    edge_options.add_argument(conf.CHROMIUM_WINDOW_HEIGHT)

    # !!!
    # безголовый режим браузера задается переменной headless, задаваемой в самом начале
    if conf.HEADLESS:
        edge_options.add_argument(conf.CHROMIUM_HEADLESS)

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

    print(driver.get_window_size())
    driver.implicitly_wait(5)
    return driver


def init_remote_driver_firefox():

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.page_load_strategy = "eager"  # 'normal'
    firefox_options.add_argument(conf.FIREFOX_WINDOW_WIDTH)
    firefox_options.add_argument(conf.FIREFOX_WINDOW_HEIGHT)

    # !!!
    # безголовый режим браузера задается переменной headless
    if conf.HEADLESS:
        firefox_options.add_argument("--headless")  # ?похоже, не работает на MacOS

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    print(driver.get_window_size())
    driver.implicitly_wait(5)
    return driver


def init_remote_driver_safari():
    # !!!
    # Safari не поддерживает Headless

    driver = webdriver.Safari()
    driver.set_window_size(*conf.SAFARI_WINDOW_SIZES)
    driver.implicitly_wait(5)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs["request"]
        driver = feature_request.getfixturevalue("d")
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_dir = os.path.dirname(item.config.option.htmlpath)
            len_dir = len(os.path.dirname(item.nodeid))
            file_name = report.nodeid[len_dir:].replace("::", "_")[1:] + ".png"
            destination_file = os.path.join(report_dir, file_name)

            def s(x):
                return driver.execute_script(
                    "return document.body.parentNode.scroll" + x)

            driver.set_window_size(s("Width"), s("Height"))
            driver.find_element(By.TAG_NAME, "body").screenshot(destination_file)
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=AttachmentType.PNG,
            )
            if file_name:
                html = \
                    ('<div><img src="%s" alt="screenshot" style="width:300px;height:200px" '
                     'onclick="window.open(this.src)" align="right"/></div>' % file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "REPORT"
