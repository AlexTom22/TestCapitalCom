from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
        # self.license = ""
        # self.language = ""
        # self.role = ""
        # self.login = ""
        # self.password = ""

    # Opens a page
    def open_page(self):

        self.browser.get(self.link)

    # Object WebElement is returned in
    # accordance with the specified search criteria
    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    # WebElements list, meeting the search requirements, is returned
    def elements_are_present(self, method, locator):
        try:
            return self.browser.find_elements(method, locator)
        except NoSuchElementException:
            return NoSuchElementException

    # Either returns the element or sets up waiting timeout seconds
    # until the object appears
    # before TimeOutException arises
    # if the element doesn't appear during timeout
    def element_is_visible(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # Either returns the element or sets up waiting timeout seconds
    # until the object is visible and clickable
    # before TimeOutException arises
    # if the element doesn't appear during timeout
    def element_is_clickable(self, loc_or_webelem, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.element_to_be_clickable(loc_or_webelem)
    )

    # Either returns the elements or sets up timeout
    # seconds until the exception TimeoutException is returned
    # if the element doesn't appear during timeout
    #
    def elements_are_located(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    # Either returns the elements or sets up timeout
    #     seconds until the exception TimeoutException is returned
    #     if the element doesn't appear during timeout
    def element_is_located(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    # Checks that the current page meets the requirements
    def should_be_link(self, link):
        assert link in self.browser.current_url, "wrong url"

    # Checks that the texts of page title element meets the requirements
    def should_be_page_title(self, title, method, locator):
        el_title = self.browser.find_element(method, locator)
        # Gets the page title element
        assert el_title, "there is no title"
        # Checks that the page title element meets the requirements
        assert title == el_title.text, "wrong title"

    # Return the elements text that meets
    # the requirements from the specified index i
    def get_text(self, i, method, locator):
        return "".join(self.browser.find_element(method, locator).text.split("\n")[i:])

    def get_text_of_element(self, method, locator):
        return "".join(self.browser.find_element(method, locator).text)

    #  Unpacks the list of elements list into element list
    def flatten(self, mylist):
        return [item for sublist in mylist for item in sublist]

    # The button is pressed on the locator
    def click_button(self, method, locator):
        self.browser.find_element(method, locator).click()

    # Returns the elements src text that meets the requirements from the specified index i
    def get_src(self, i, method, locator):
        return "".join(
            self.browser.find_element(method, locator)
            .get_property("src")
            .split("\n")[i:]
        )

    # Returns the list elements text that meets the requirements from the specified index i
    def get_text_elements(self, i, method, locator):
        try:
            list_prices = self.browser.find_elements(method, locator)
            return list(map(lambda element: element.text[i:], list_prices))
        except NoSuchElementException:
            return NoSuchElementException
