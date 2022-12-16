import logging
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


class Handle_Exc_Element_Decorator(object):
    """A decorator that handles exceptions related to element on a webpage."""

    def __init__(
        self,
        browser="self",
        timeout=0.5,
        title="title",
        value="value",
        property="property",
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
            property (optional): the property of the element. Defaults to 'property'.
            method (optional): used for locating the element on the page. Defaults to 'a'.
            locator (optional): used with the specified method to find the element. Defaults to 'b'.
            index (optional): extract all elements of the list of individual lines of text starting from the
                ith element. Defaults to 0.
        """
        self.browser = browser
        self.timeout = timeout
        self.title = title
        self.value = value
        self.property = property
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
                    f"Could not find element on page: {decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
            except TimeoutException as e:
                logging.error(
                    f"Element not present after {decorator_self.timeout} seconds on page: "
                    f"{decorator_self.browser.current_url}"
                )
                logging.exception(e.msg)
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
                    f"The element is no longer attached to the DOM on page: {decorator_self.self.browser.current_url}"
                )
                logging.exception(e.msg)
            except WebDriverException as e:
                logging.error("Unable to initialize WebDriver")
                logging.exception(e.msg)

        return inner_function


class Handle_Exc_Elements_Decorator(object):
    """A decorator that handles exceptions related to elements on a webpage."""

    def __init__(
        self,
        browser="self",
        timeout=0.5,
        title="title",
        value="value",
        property="property",
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
            property (optional): the property of the element. Defaults to 'property'.
            method (optional): used for locating the element on the page. Defaults to 'a'.
            locator (optional): used with the specified method to find the element. Defaults to 'b'.
            index (optional): extract all elements of the list of individual lines of text starting from the
                ith element. Defaults to 0.
        """
        self.browser = browser
        self.timeout = timeout
        self.title = title
        self.value = value
        self.property = property
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
                    f"Elements not present after {decorator_self.timeout} seconds on page: {decorator_self.browser.current_url}"
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
                    f"The elements are no longer attached to the DOM on page: {decorator_self.self.browser.current_url}"
                )
                logging.exception(e.msg)
            except WebDriverException as e:
                logging.error("Unable to initialize WebDriver")
                logging.exception(e.msg)

        return inner_function


class BasePage:
    """This class used as a base class for other page classes that represent specific pages on a website"""

    def __init__(self, browser, link):
        """Initializes the object.

        Args:
            browser: WebDriver
            link: URL
        """
        self.browser = browser
        self.link = link

    def open_page(self):
        """Navigates to a page given by the URL."""
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        """Find an element given a By method and locator.

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
        try:
            self.browser.find_element(method, locator)
        except InvalidElementStateException as e:
            logging.error(
                f"The element is in an invalid state on page: {self.browser.current_url}"
            )
            logging.exception(e.msg)
            return False
        except NoSuchElementException as e:
            logging.error(f"Could not find element on page: {self.browser.current_url}")
            logging.exception(e.msg)
            return False
        except WebDriverException as e:
            logging.error("Unable to initialize WebDriver")
            logging.exception(e.msg)
            return False
        return True

    def elements_are_present(self, method, locator):
        """Find elements given a By method and locator.

        Args:
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: list of found WebElement or empty if
                elements are not found
        """
        return self.browser.find_elements(method, locator)

    @Handle_Exc_Element_Decorator()
    def send_keys(self, value, method, locator):
        """Sends keys to an element given a By method and locator.

        Args:
            value: the value to send to the element
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        """
        self.browser.find_element(method, locator).send_keys(value)

    @Handle_Exc_Element_Decorator()
    def get_property(self, property, method, locator):
        """Gets the given property of the element.

        Args:
            property: name of the property to retrieve
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            str | bool | WebElement | dict: the value of a property with the given name or None if there's no property
                with that name
        """
        return self.browser.find_element(method, locator).get_property(property)

    @Handle_Exc_Element_Decorator()
    def element_is_visible(self, locator, timeout=5):
        """Check that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width that is greater than 0.

        Args:
            locator: used to find the element; a tuple of 'by' and 'path'
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: it is located and visible
        """
        return Wait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @Handle_Exc_Elements_Decorator()
    def elements_are_located(self, locator, timeout=5):
        """Check that there is at least one element, located by the locator, present on a web page.

        Args:
            locator: used to find the element; a tuple of 'by' and 'path'
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.

        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: the list of all matched WebElements
        """
        return Wait(self.browser, timeout).until(
            EC.presence_of_all_elements_located((locator))
        )

    @Handle_Exc_Element_Decorator()
    def element_is_located(self, locator, timeout=5):
        """Check that an element is present on the DOM of a page.

        Args:
            locator: used to find the element; a tuple of 'by' and 'path'
            timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: returns the WebElement located
        """
        return Wait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def should_be_link(self, link):
        """Check that the link provided is in the current URL of the browser.

        Args:
            link: link browser
        """
        assert (
            link in self.browser.current_url
        ), f"Expected link {link} not found in URL {self.browser.current_url}"

    @Handle_Exc_Element_Decorator()
    def should_be_page_title(self, title, method, locator):
        """Check that the page has the expected title given a By method and locator.

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

    @Handle_Exc_Element_Decorator()
    def get_text(self, i, method, locator):
        """Extract a specific part of the text from the element given a By method and locator.

        Args:
            i: extract all elements of the list of individual lines of text starting from the ith element
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            str: the text of the element
        """
        return "".join(self.browser.find_element(method, locator).text.split("\n")[i:])

    def flatten(self, mylist):
        """Unpacks list of lists of elements into a single, flat list of elements

        Args:
            mylist: the list of the lists of WebElements.

        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: the list of WebElements.
        """
        return [item for sublist in mylist for item in sublist]

    @Handle_Exc_Element_Decorator()
    def click_button(self, method, locator):
        """Clicks the element given a By method and locator.

        Args:
            method: used for locating the element on the page
            locator: used with the specified method to find the element
        """
        self.browser.find_element(method, locator).click()

    @Handle_Exc_Element_Decorator()
    def get_src(self, i, method, locator):
        """Extract the src attribute of an element given a By method and locator.
        The src attribute specifies the URL of an image or other media file.

        Args:
            i: extract all elements of the list of individual lines of text starting from the ith element
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            str: the src of the element
        """
        return "".join(
            self.browser.find_element(method, locator)
            .get_property("src")
            .split("\n")[i:]
        )

    @Handle_Exc_Elements_Decorator()
    def get_text_elements(self, i, method, locator):
        """Extract the substrings of the text from the elements given a By method and locator.
        Args:
            i: substring starts at the i-th character and continues to the end of the text
            method: used for locating the element on the page
            locator: used with the specified method to find the element

        Returns:
            list[str]: the list of substring of the element's text
        """
        list_prices = self.browser.find_elements(method, locator)
        return list(map(lambda element: element.text[i:], list_prices))

# class BasePage:
#     """This class used as a base class for other page classes that represent specific pages on a website"""
#
#     def __init__(self, browser, link):
#         """Initializes the object.
#
#         Args:
#             browser: WebDriver
#             link: URL
#         """
#         self.browser = browser
#         self.link = link
#
#     def open_page(self):
#         """Navigates to a page given by the URL."""
#         self.browser.get(self.link)
#
#     def element_is_present(self, method, locator):
#         """Find an element given a By method and locator.
#
#         Args:
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Returns:
#             bool: True if the element is located in a page. False if the element could not be found
#         Raises:
#             InvalidElementStateException: if the element is in an invalid state
#             NoSuchElementException: if the element cannot be found on the page
#             WebDriverException:  if an error occurs while initializing the WebDriver
#         """
#         try:
#             self.browser.find_element(method, locator)
#         except InvalidElementStateException as e:
#             logging.error(
#                 f"The element is in an invalid state on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#             return False
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#             return False
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#             return False
#         return True
#
#     def elements_are_present(self, method, locator):
#         """Find elements given a By method and locator.
#
#         Args:
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Returns:
#             list[selenium.webdriver.remote.webelement.WebElement]:
#                 list of found WebElement or empty if elements are not found
#         Raises:
#             NoSuchElementException: if the elements are not found on the page
#             StaleElementReferenceException: if the elements are no longer attached to the DOM
#             WebDriverException: if an error occurs while initializing the WebDriver
#
#         """
#         try:
#             return self.browser.find_elements(method, locator)
#         except NoSuchElementException as e:
#             logging.error(
#                 f"Could not find elements on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The elements is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def send_keys(self, value, method, locator):
#         """Sends keys to an element given a By method and locator.
#
#         Args:
#             value: the value to send to the element
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#         Raises:
#             NoSuchElementException: if the element cannot be found on the page
#             ElementNotInteractableException: if the element is not currently interactable
#             InvalidElementStateException: if the element is in an invalid state
#             StaleElementReferenceException: if the element is no longer attached to the DOM
#             WebDriverException:  if an error occurs while initializing the WebDriver
#         """
#         try:
#             self.browser.find_element(method, locator).send_keys(value)
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#         except ElementNotInteractableException as e:
#             logging.error(
#                 f"The element is not currently interactable on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except InvalidElementStateException as e:
#             logging.error(
#                 f"The element is in an invalid state on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The element is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def get_property(self, property, method, locator):
#         """Gets the given property of the element.
#
#         Args:
#             property: name of the property to retrieve
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Returns:
#             str | bool | WebElement | dict: the value of a property with the given name or None
#                 if there's no property with that name
#
#         Raises:
#             NoSuchElementException: if the element cannot be found on the page
#             NoSuchAttributeException: if the attribute of the element is not found
#             StaleElementReferenceException: if the elements are no longer attached to the DOM
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             return self.browser.find_element(method, locator).get_property(property)
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#         except NoSuchAttributeException as e:
#             logging.error(
#                 f"The attribute of element could not be found on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The element is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def element_is_visible(self, locator, timeout=10):
#         """Check that an element is present on the DOM of a page and visible.
#         Visibility means that the element is not only displayed but also has a height and width
#             that is greater than 0.
#
#         Args:
#             locator: used to find the element; a tuple of 'by' and 'path'
#             timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.
#
#         Returns:
#             selenium.webdriver.remote.webelement.WebElement: it is located and visible
#
#         Raises:
#             TimeoutException: when there is no match with at least one element even after wait time
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
#         except TimeoutException as e:
#             logging.exception(
#                 f"Element not present after {timeout} seconds on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def elements_are_located(self, locator, timeout=5):
#         """Check that there is at least one element, located by the locator, present on a web page.
#
#         Args:
#             locator: used to find the element; a tuple of 'by' and 'path'
#             timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.
#
#         Returns:
#             list[selenium.webdriver.remote.webelement.WebElement]: the list of all matched WebElements
#
#         Raises:
#             TimeoutException: when there is no match with at least one element even after wait time
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             return Wait(self.browser, timeout).until(
#                 EC.presence_of_all_elements_located(locator)
#             )
#         except TimeoutException as e:
#             logging.exception(
#                 f"Elements not present after {timeout} seconds on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def element_is_located(self, locator, timeout=5):
#         """Check that an element is present on the DOM of a page.
#
#         Args:
#             locator: used to find the element; a tuple of 'by' and 'path'
#             timeout (optional): specified time duration before throwing a TimeoutException. Defaults to 5.
#
#         Returns:
#             selenium.webdriver.remote.webelement.WebElement: returns the WebElement located
#
#         Raises:
#             TimeoutException: when there is no match with at least one element even after wait time
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             return Wait(self.browser, timeout).until(
#                 EC.presence_of_element_located((locator))
#             )
#         except TimeoutException as e:
#             logging.exception(
#                 f"Element not present after {timeout} seconds on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def should_be_link(self, link):
#         """Check that the link provided is in the current URL of the browser.
#
#         Args:
#             link: link browser
#         """
#         assert (
#             link in self.browser.current_url
#         ), f"Expected link {link} not found in URL {self.browser.current_url}"
#
#     def should_be_page_title(self, title, method, locator):
#         """Check that the page has the expected title given a By method and locator.
#
#         Args:
#             title: page's title
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Raises:
#             NoSuchElementException: if the element cannot be found on the page
#             StaleElementReferenceException: if the elements are no longer attached to the DOM
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             el_title = self.browser.find_element(method, locator)
#             # Gets the page title element
#             assert (
#                 el_title
#             ), f"Title element not found on page: {self.browser.current_url}"
#             # Checks that the page title element meets the requirements
#             assert (
#                 el_title.text == title
#             ), f"Expected title {title} but got {el_title.text} on page: {self.browser.current_url}"
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The element is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#
#     def get_text(self, i, method, locator):
#         """Extract a specific part of the text from the element given a By method and locator.
#
#         Args:
#             i: extract all elements of the list of individual lines of text starting from the ith element
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Returns:
#             str: the text of the element
#
#         Raises:
#             NoSuchElementException: if the element cannot be found on the page
#             StaleElementReferenceException: if the elements are no longer attached to the DOM
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             return "".join(
#                 self.browser.find_element(method, locator).text.split("\n")[i:]
#             )
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The element is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def flatten(self, mylist):
#         """Unpacks list of lists of elements into a single, flat list of elements
#
#         Args:
#             mylist: the list of the lists of WebElements.
#
#         Returns:
#             list[selenium.webdriver.remote.webelement.WebElement]: the list of WebElements.
#         """
#         return [item for sublist in mylist for item in sublist]
#
#     def click_button(self, method, locator):
#         """Clicks the element given a By method and locator.
#
#         Args:
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Raises:
#             InvalidElementStateException: if the element is in an invalid state
#             NoSuchElementException: if the element cannot be found on the page
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             self.browser.find_element(method, locator).click()
#         except InvalidElementStateException as e:
#             logging.error(
#                 f"The element is in an invalid state on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def get_src(self, i, method, locator):
#         """Extract the src attribute of an element given a By method and locator.
#         The src attribute specifies the URL of an image or other media file.
#
#         Args:
#             i: extract all elements of the list of individual lines of text starting from the ith element
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Returns:
#             str: the src of the element
#
#         Raises:
#             NoSuchElementException: if the element cannot be found on the page
#             NoSuchAttributeException: if the attribute of the element is not found
#             StaleElementReferenceException: if the elements are no longer attached to the DOM
#             InvalidElementStateException: if the element is in an invalid state
#             WebDriverException: if an error occurs while initializing the WebDriver
#         """
#         try:
#             return "".join(
#                 self.browser.find_element(method, locator)
#                 .get_property("src")
#                 .split("\n")[i:]
#             )
#         except NoSuchElementException as e:
#             logging.error(f"Could not find element on page: {self.browser.current_url}")
#             logging.exception(e.msg)
#         except NoSuchAttributeException as e:
#             logging.error(
#                 f"The attribute of element could not be found on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The element is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except InvalidElementStateException as e:
#             logging.error(
#                 f"The element is in an invalid state on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
#
#     def get_text_elements(self, i, method, locator):
#         """Extract the substrings of the text from the elements given a By method and locator.
#         Args:
#             i: substring starts at the i-th character and continues to the end of the text
#             method: used for locating the element on the page
#             locator: used with the specified method to find the element
#
#         Returns:
#             list[str]: the list of substring of the element's text
#
#         Raises:
#             NoSuchElementException: if the elements are not found on the page
#             StaleElementReferenceException: if the elements are no longer attached to the DOM
#             WebDriverException:  If an error occurs while initializing the WebDriver
#         """
#         try:
#             list_prices = self.browser.find_elements(method, locator)
#             return list(map(lambda element: element.text[i:], list_prices))
#         except NoSuchElementException as e:
#             logging.error(
#                 f"Could not find elements on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except StaleElementReferenceException as e:
#             logging.error(
#                 f"The elements is no longer attached to the DOM on page: {self.browser.current_url}"
#             )
#             logging.exception(e.msg)
#         except WebDriverException as e:
#             logging.error("Unable to initialize WebDriver")
#             logging.exception(e.msg)
