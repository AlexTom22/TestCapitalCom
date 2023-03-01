"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import pytest
import os
import conf
import allure
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


def pre_go(fixture_value):
    global test_browser
    test_browser = fixture_value
    return None


@pytest.fixture(
    scope="class",
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
    print(request.param)
    # d.get(conf.URL)

    yield d

    d.quit()
    print("\n*** end fixture = teardown ***\n")


@pytest.fixture(scope="class")
def d(browser):
    """WebDriver Initialization"""
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


@pytest.fixture(scope="class")
def browser():
    global test_browser
    return test_browser


def init_remote_driver_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument(conf.CHROME_WINDOW_SIZES)
    options.add_argument(conf.CHROMIUM_HEADLESS)    # если строку раскомментировать, то Chrome отображаться не будет
    options.page_load_strategy = "eager"  # 'normal'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def init_remote_driver_edge():
    options = webdriver.EdgeOptions()
    options.add_argument(conf.CHROMIUM_HEADLESS)    # если строку раскомментировать, то EDGE отображаться не будет
    # options.add_argument(conf.CHROMIUM_WINDOW_WIDTH)
    # options.add_argument(conf.CHROMIUM_WINDOW_HEIGHT)
    options.page_load_strategy = "eager"  # 'normal'
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    # driver.set_window_size(*conf.EDGE_WINDOW_SIZES)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def init_remote_driver_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument(conf.FIREFOX_WINDOW_WIDTH)
    options.add_argument(conf.FIREFOX_WINDOW_HEIGHT)
    options.headless = conf.BROWSER_HEADLESS
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    return driver


def init_remote_driver_safari():
    driver = webdriver.Safari()
    driver.set_window_size(*conf.SAFARI_WINDOW_SIZES)
    driver.implicitly_wait(5)
    # driver.window_handles = conf.BROWSER_HEADLESS
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
                name="Screeshot",
                attachment_type=AttachmentType.PNG,
            )
            if file_name:
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:300px;height:200px" onclick="window.open('
                    'this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        

def pytest_html_report_title(report):
    report.title = "REPORT"
