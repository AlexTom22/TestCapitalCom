import logging
import time

import allure
from datetime import datetime

import pytest
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
    NoSuchAttributeException,
    ElementNotInteractableException,
    InvalidElementStateException,
    StaleElementReferenceException,
)
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from pages.Capital.capital_locators import OnTrustLocators, Captcha
# from src.src import (
#     CapitalComPageSrc,
# )


class HandleExcElementDecorator(object):
    """A decorator that handles exceptions related to element on a webpage."""

    def __init__(
        self,
        browser="self",
        timeout=0.5,
        title="title",
        value="value",
        propety="property",
        method="a",
        locator="b",
        index=0,
    ):
        """Initializes the object.

        Args:
            browser: WebDriver. Defaults to 'self'.
            timeout (optional): the time to wait for an element to be present on the
            page before throwing a TimeoutException. Defaults to 0.5.
            title (optional): the title of the page. Defaults to 'title'.
            value (optional): the value to send to the element. Defaults to 'value'.
            'property' (optional): the property of the element. Defaults to 'property'.
            method (optional): used for locating the element on the page. Defaults to 'a'.
            locator (optional): used with the specified method to find the element. Defaults to 'b'.
            index (optional): extract all elements of the list of individual lines of text starting from the
                ith element. Defaults to 0.
        """
        self.browser = browser
        self.timeout = timeout
        self.title = title
        self.value = value
        self.propety = propety
        self.method = method
        self.locator = locator
        self.index = index

    def __call__(self, func):
        """Define an inner function that wraps the original function or method.

        Args:
            func (function): the original function or method to be decorated.

        Raises:
            NoSuchElementException: if the element cannot be found on the page
            TimeoutException: when there is no match with at least one element even after wait time
            NoSuchAttributeException: if the attribute of the element is not found
            ElementNotInteractableException: if the element is not currently interactable
            InvalidElementStateException: if the element is in an invalid state
            StaleElementReferenceException: if the element is no longer attached to the DOM
            WebDriverException:  if an error occurs while initializing the WebDriver
        """
        decorator_self = self

        def inner_function(*args, **kwargs):
            self.browser = args[0].browser
            try:
                return func(*args, **kwargs)
            except NoSuchElementException as e:
                logging.error(
                    # f"Could not find element on page: {decorator_self.browser.current_url}"
                    f"Could not find element on page: {self.browser.current_url}"
                )
                logging.exception(e.msg)
            # except TimeoutException as e:
            #     logging.error(
            #         f"Element not present after {decorator_self.timeout} seconds on page: "
            #         f"{decorator_self.browser.current_url}"
            #     )
            #     logging.exception(e.msg)
            except NoSuchAttributeException as e:
                logging.error(
                    f"The attribute of element could not be found on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except ElementNotInteractableException as e:
                logging.error(
                    f"The element is not currently interactable on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except InvalidElementStateException as e:
                logging.error(
                    f"The element is in an invalid state on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except StaleElementReferenceException as e:
                logging.error(
                    f"The element is no longer attached to the DOM on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except WebDriverException as e:
                logging.error("Unable to initialize WebDriver")
                logging.exception(e.msg)

        return inner_function


class HandleExcElementsDecorator(object):
    """A decorator that handles exceptions related to elements on a webpage."""

    def __init__(
        self,
        browser="self",
        timeout=0.5,
        title="title",
        value="value",
        propety="property",
        method="a",
        locator="b",
        index=0,
    ):
        """Initializes the object.

        Args:
            browser: WebDriver. Defaults to 'self'.
            timeout (optional): the time to wait for an element to be present on the
            page before throwing a TimeoutException. Defaults to 0.5.
            title (optional): the title of the page. Defaults to 'title'.
            value (optional): the value to send to the element. Defaults to 'value'.
            'property' (optional): the property of the element. Defaults to 'property'.
            method (optional): used for locating the element on the page. Defaults to 'a'.
            locator (optional): used with the specified method to find the element. Defaults to 'b'.
            index (optional): extract all elements of the list of individual lines of text starting from the
                ith element. Defaults to 0.
        """
        self.browser = browser
        self.timeout = timeout
        self.title = title
        self.value = value
        self.propety = propety
        self.method = method
        self.locator = locator
        self.index = index

    def __call__(self, func):
        """Define an inner function that wraps the original function or method.

        Args:
            func (function): the original function or method to be decorated.

        Raises:
            NoSuchElementException: if the elements are not found on the page
            TimeoutException: when there is no match with at least one element even after wait time
            NoSuchAttributeException: if the attribute of the elements is not found
            ElementNotInteractableException: if the elements are not currently interactable
            InvalidElementStateException: if the element are in an invalid state
            StaleElementReferenceException: if the elements are no longer attached to the DOM
            WebDriverException:  if an error occurs while initializing the WebDriver
        """
        decorator_self = self

        def inner_function(*args, **kwargs):
            self.browser = args[0].browser
            try:
                return func(*args, **kwargs)
            except NoSuchElementException as e:
                logging.error(
                    f"Could not find elements on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except TimeoutException as e:
                logging.error(
                    f"Elements not present after {decorator_self.timeout} "
                    f"seconds on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except NoSuchAttributeException as e:
                logging.error(
                    f"The attribute of elements could not be found on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except ElementNotInteractableException as e:
                logging.error(
                    f"The element is not currently interactable on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except InvalidElementStateException as e:
                logging.error(
                    f"The element is in an invalid state on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except StaleElementReferenceException as e:
                logging.error(
                    f"The elements are no longer attached to the DOM on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except WebDriverException as e:
                logging.error("Unable to initialize WebDriver")
                logging.exception(e.msg)

        return inner_function


class BasePage:
    """This class used as a base class for other page classes that represent specific pages on a website"""

    def __init__(self, browser, link=""):
        """
        Initializes the object.

        Args:
            browser: WebDriver
            link: URL
        """
        self.browser = browser
        self.link = link

    # @allure.step(f"Load page {self.link}")
    def open_page(self):
        """
        Navigates to a page given by the URL.
        """
        self.browser.get(self.link)
        # time.sleep(1)
        print(f"{datetime.now()}   Load page {self.link}")

    @allure.step("Accept all cookies")
    def button_accept_all_cookies_click(self):
        print(f"\n"
              f"{datetime.now()}   Click button [Accept all cookies]")
        print(f"{datetime.now()}   Is Visible BUTTON_ACCEPT_ALL_COOKIE? =>")
        self.element_is_visible(OnTrustLocators.BUTTON_ACCEPT_ALL_COOKIE, 30)
        print(f"{datetime.now()}   Find BUTTON_ACCEPT_ALL_COOKIE =>")
        buttons = self.browser.find_elements(*OnTrustLocators.BUTTON_ACCEPT_ALL_COOKIE)

        if len(buttons) == 0:
            print(f"{datetime.now()}   => BUTTON_ACCEPT_ALL_COOKIE not presented")
            print(f"{datetime.now()}   => Возможно, всплыла ReCaptcha. Проверим и если проверка на робота, подтвердим, "
                  f"что я не робот")
            check_box_i_am_not_robot = self.browser.find_elements(
                "By.CSS", "#recaptcha-anchor > .recaptcha-checkbox-border")
            if len(check_box_i_am_not_robot) == 0:
                print(f"{datetime.now()}   =>  Это не Check Box ReCaptcha. Прекращаем выполнение теста")
                assert False, f"{datetime.now()}   =>  Это не Check Box ReCaptcha. Прекращаем выполнение теста"
            print(f"{datetime.now()}   => Это Check Box ReCaptcha 'I am not robot'")
            print(f"{datetime.now()}   Чекаем Check Box ReCaptcha 'I am not robot'")
            check_box_i_am_not_robot[0].click()
            time.sleep(1)
            self.element_is_visible(OnTrustLocators.BUTTON_ACCEPT_ALL_COOKIE, 30)
            print(f"{datetime.now()}   Find BUTTON_ACCEPT_ALL_COOKIE =>")
            buttons = self.browser.find_elements(*OnTrustLocators.BUTTON_ACCEPT_ALL_COOKIE)
        else:
            print(f"{datetime.now()}   => BUTTON_ACCEPT_ALL_COOKIE presented")

        print(f"{datetime.now()}   Is clickable BUTTON_ACCEPT_ALL_COOKIE? =>")
        button = buttons[0]
        self.element_is_clickable(button, 30)
        print(f"{datetime.now()}   Click BUTTON_ACCEPT_ALL_COOKIE =>")
        time.sleep(1)
        button.click()
        print(f"{datetime.now()}   => BUTTON_ACCEPT_ALL_COOKIE is clicked")
        print(f"{datetime.now()}   => Accepted All Cookies")

    @allure.step("Reject all cookies")
    def button_reject_all_cookies_click(self):
        print(f"\n"
              f"{datetime.now()}   Is visible BUTTON_REJECT_ALL_COOKIE? =>")
        self.element_is_visible(OnTrustLocators.BUTTON_REJECT_ALL_COOKIE, 30)
        print(f"{datetime.now()}   Find BUTTON_REJECT_ALL_COOKIE =>")
        button = self.browser.find_element(*OnTrustLocators.BUTTON_REJECT_ALL_COOKIE)
        print(f"{datetime.now()}   Is clickable BUTTON_REJECT_ALL_COOKIE? =>")
        self.element_is_clickable(button, 30)
        time.sleep(1)
        print(f"{datetime.now()}   Click BUTTON_REJECT_ALL_COOKIE =>")
        button.click()
        print(f"{datetime.now()}   => Rejected All Cookies")

    @HandleExcElementsDecorator()
    def element_is_present(self, method, locator):
        """
        Find an element given a By method and locator.

        Args:
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            bool: True if the element is located in a page. False if the element could not be found
        Raises:
            InvalidElementStateException: if the element is in an invalid state
            NoSuchElementException: if the element cannot be found on the page
            WebDriverException:  if an error occurs while initializing the WebDriver
        """
        return self.browser.find_element(method, locator)

    @HandleExcElementsDecorator()
    def elements_are_present(self, method, locator):
        """
        Find elements given a By method and locator.

        Args:
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]:
                list of found WebElement or empty if elements are not found
        Raises:
            NoSuchElementException: if the elements are not found on the page
            StaleElementReferenceException: if the elements are no longer attached to the DOM
            WebDriverException: if an error occurs while initializing the WebDriver
        """
        return self.browser.find_elements(method, locator)

    @HandleExcElementDecorator()
    def send_keys(self, value, method, locator):
        """
        Sends keys to an element given a By method and locator.

        Args:
            value: the value to send to the element
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        """
        list_of_elements = self.browser.find_elements(method, locator)
        if len(list_of_elements) == 0:
            print(f"{datetime.now()}   => TextBox with '{locator}' locator is not present")
            return False
        list_of_elements[0].send_keys(value)
        return True

    @HandleExcElementDecorator()
    def get_attribute(self, attribute, method, locator):
        """
        Gets the given property of the element.

        Args:
            attribute: name of the attribute to retrieve
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        Returns:
            str | bool | WebElement | dict: the value of the attribute with the given name or None,
                if there's no attribute
                with that name
        """
        return self.browser.find_element(method, locator).get_attribute(attribute)

    @HandleExcElementDecorator()
    def get_property(self, propety, method, locator):
        """
        Gets the given property of the element.

        Args:
            propety: name of the property to retrieve
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        Returns:
            str | bool | WebElement | dict: the value of a property with the given name or None if there's no property
                with that name
        """
        return self.browser.find_element(method, locator).get_property(propety)

    @HandleExcElementDecorator()
    def element_is_visible(self, locator, timeout=1):
        """
        Check that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width that is greater than 0.

        Args:
            locator: used to find the element; a tuple of 'by' and 'path'
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 1.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: it is located and visible
        """
        return Wait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @HandleExcElementDecorator()
    def element_is_clickable(self, loc_or_elem, timeout=1):
        """
        Check that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width that is greater than 0.

        Args:
            loc_or_elem: used to find the element; a tuple of 'by' and 'path' or webelement
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 1.
        Returns:
            selenium.webdriver.remote.webelement.WebElement: it is located and visible
            False: not clickable
        """
        return Wait(self.browser, timeout).until(
            EC.element_to_be_clickable(loc_or_elem)
        )

    @HandleExcElementsDecorator()
    def elements_are_located(self, locator, timeout=5):
        """
        Check that there is at least one element, located by the locator, present on a web page.

        Args:
            locator: used to find the element; a tuple of 'by' and 'path'
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.
        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: the list of all matched WebElements
        """
        return Wait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @HandleExcElementDecorator()
    def element_is_located(self, locator, timeout=1):
        """
        Check that an element is present on the DOM of a page.

        Args:
            locator: used to find the element; a tuple of 'by' and 'path'
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 1.
        Returns:
            selenium.webdriver.remote.webelement.WebElement: returns the WebElement located
        """
        return Wait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @HandleExcElementDecorator()
    def current_page_is(self, link):
        return link == self.browser.current_url

    @HandleExcElementDecorator()
    def current_page_url_contain_the(self, host):
        cur_url = self.browser.current_url
        result = host in cur_url
        return result

    @HandleExcElementDecorator()
    @allure.step("Check the current page has URL: '{link}'")
    def check_current_page_is(self, link):
        print(f"{datetime.now()}   Cur page is {link}? =>")
        assert (self.browser.current_url == link), f"Expected page: {link}. Actual page: {self.browser.current_url}"
        print(f"{datetime.now()}   => Cur page is {link}")

    @HandleExcElementDecorator()
    @allure.step("Check, that the link provided is in the current URL of the browser")
    def should_be_link(self, link):
        """
        Check that the link provided is in the current URL of the browser.

        Args:
            link: link browser
        """
        assert (
            link == self.browser.current_url
        ), f"Expected link {link} not found in URL {self.browser.current_url}"

    @HandleExcElementDecorator()
    def should_be_page_title(self, title, method, locator):
        """
        Check that the page has the expected title given a By method and locator.

        Args:
            title: page's title
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        """
        el_title = self.browser.find_element(method, locator)
        # Gets the page title element
        assert el_title, f"Title element not found on page: {self.browser.current_url}"
        # Checks that the page title element meets the requirements
        assert (
            el_title.text == title
        ), f"Expected title {title} but got {el_title.text} on page: {self.browser.current_url}"

    @HandleExcElementDecorator()
    @allure.step("Check that the page has the expected title - ver 2")
    def should_be_page_title_v2(self, title):
        """
        Check that the page has the expected title.

        Args:
            title: expected page's title
        """
        el_title = self.browser.title
        print(f"{datetime.now()}   => Current page title: {el_title}")
        # Checks that the page title meets the requirements
        if title not in el_title:
            pytest.fail(f"Bug! Expected title '{title}' but got '{el_title}' on page: {self.browser.current_url}")

    @HandleExcElementDecorator()
    def get_text(self, i, method, locator):
        """
        Extract a specific part of the text from the element given a By method and locator.

        Args:
            i: extract all elements of the list of individual lines of text starting from the ith element
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        Returns:
            str: the text of the element
        """
        return "".join(self.browser.find_element(method, locator).text.split("\n")[i:])

    def flatten(self, mylist):
        """
        Unpacks list of lists of elements into a single, flat list of elements

        Args:
            mylist: the list of the lists of WebElements.
        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: the list of WebElements.
        """
        return [item for sublist in mylist for item in sublist]

    @HandleExcElementDecorator()
    def click_button(self, method, locator):
        """
        Clicks the element given a By method and locator.

        Args:
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        """
        self.browser.find_element(method, locator).click()

    @HandleExcElementDecorator()
    def get_src(self, i, method, locator):
        """
        Extract the src attribute of an element given a By method and locator.
        The src attribute specifies the URL of an image or other media file.

        Args:
            i: extract all elements of the list of individual lines of text starting from the ith element
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        Returns:
            str: the src of the element
        Raises:
            NoSuchElementException: if the element cannot be found on the page
            NoSuchAttributeException: if the attribute of the element is not found
            StaleElementReferenceException: if the elements are no longer attached to the DOM
            InvalidElementStateException: if the element is in an invalid state
            WebDriverException: if an error occurs while initializing the WebDriver
        """
        return "".join(
            self.browser.find_element(method, locator)
            .get_property("src")
            .split("\n")[i:]
        )

    @HandleExcElementsDecorator()
    def get_text_elements(self, i, method, locator):
        """
        Extract the substrings of the text from the elements given a By method and locator.
        Args:
            i: substring starts at the i-th character and continues to the end of the text
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        Returns:
            list[str]: the list of substring of the element's text
        Raises:
            NoSuchElementException: if the elements are not found on the page
            StaleElementReferenceException: if the elements are no longer attached to the DOM
            WebDriverException:  If an error occurs while initializing the WebDriver
        """
        list_prices = self.browser.find_elements(method, locator)
        return list(map(lambda element: element.text[i:], list_prices))

    @HandleExcElementDecorator()
    def wait_for_change_url(self, cur_link, timeout=1):
        """
        Waiting for url change
        Args:
            cur_link: the current url that needs to change
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 1.

        """
        return Wait(self.browser, timeout).until(
            EC.url_changes(cur_link)
        )

    @HandleExcElementDecorator()
    def wait_for_target_url(self, link, timeout=1):
        """
        Waiting for target url
        Args:
            link: the target url that we are waiting for
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 1.

        """
        return Wait(self.browser, timeout).until(
            EC.url_contains(link)
        )

    @HandleExcElementDecorator()
    def is_captcha(self):
        if self.elements_are_present(*Captcha.CAPTCHA_IFRAME):
            pytest.fail("Captcha on the page")
