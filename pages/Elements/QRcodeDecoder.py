"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
# import time
from datetime import datetime
import pytest
import allure

# from pages.Signup_login.signup_login_locators import SignupFormLocators
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import QRCodeLocators
from pages.Signup_login.signup_login import SignupLogin

# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import cv2
from pyzbar.pyzbar import decode
from qreader import QReader
from PIL import Image
import os


# import aspose.barcode as barcode
# import urllib.request


class QRCodeDecode(BasePage):

    def __init__(self, browser, link, qr_code):
        super().__init__(browser, link)
        self.element = None
        self.locator_link = None
        self.locator = None
        self.qr_code = qr_code

    def arrange(self):
        print(f"\n{datetime.now()}   1. Arrange")
        print(f"\n{datetime.now()}   Testing the qr code: {self.qr_code.upper()}")
        if not self.current_page_is(self.link):
            self.open_page()
        match self.qr_code:
            case 'investmate':
                self.locator = QRCodeLocators.QR_CODE_INVESTMATE
                locator_link = QRCodeLocators.QR_CODE_INVESTMATE_LINK
            case 'easy_learning':
                self.locator = QRCodeLocators.QR_CODE_EASY_LEARNING
                locator_link = QRCodeLocators.QR_CODE_EASY_LEARNING_LINK
            case _:
                self.locator = QRCodeLocators.QR_CODE_CAPITAL
                locator_link = QRCodeLocators.QR_CODE_CAPITAL_LINK

        # Checking if [SignUP for is popped up on the page]
        check_popup = SignupLogin(self.browser, self.link)
        check_popup.check_popup_signup_form()
        #
        print(f"{datetime.now()}   QR_CODE is located in the DOM? =>")
        qr_code_img = self.element_is_located(self.locator, 10)
        if qr_code_img:
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                qr_code_img
            )
            print(f"{datetime.now()}   => QR_CODE_{self.qr_code.upper()} is located in the DOM")
        else:
            print(f"{datetime.now()}   => QR_CODE_{self.qr_code.upper()} is not present on the page!")

        print(f"{datetime.now()}   QR_CODE_LINK is visible on the page? =>")
        self.element = self.element_is_visible(locator_link, 5)
        if self.element:
            print(f"{datetime.now()}   => QR_CODE_LINK {self.qr_code.upper()} is on the page!")
            return self
        else:
            print(f"{datetime.now()}   => QR_CODE_LINK {self.qr_code.upper()} is not on the page!")
            pytest.fail(f"Checking element QR_CODE_LINK {self.qr_code.upper()} is not visible on the page")

    @allure.step("Determining the qr code title link")
    def element_decode(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Determining the QR_CODE_TITLE link")
        qr_title_link = self.element.get_attribute('title')
        if qr_title_link:
            print(f"{datetime.now()}   QR_CODE_TITLE link: {qr_title_link}")

            # Checking if [SignUP for is popped up on the page]
            check_popup = SignupLogin(self.browser, self.link)
            check_popup.check_popup_signup_form()

            # Start encoding QR-code image
            qr_img = self.element_is_visible(self.locator, 10)
            qr_img_link = self.check_qrcode_img_link(qr_img)
            print(f"{datetime.now()}   Check QR-code title link equal QR-code image link =>")
            assert qr_img_link == qr_title_link, (f"The QR-code title link: {qr_title_link} NOT"
                                                  f" equal QR-code image link: {qr_img_link} ")

            # Open QR-code image link
            self.link = qr_img_link
            self.open_page()
        else:
            pytest.fail("QR_CODE_LINK_TITLE IS NOT DEFINED")
        #

        # print(f"\n{datetime.now()}   2. Act")
        # print(f"{datetime.now()}   QR_CODE_{self.filename.upper()} is present? =>")
        # code_list = self.browser.find_elements(*self.locator_link)
        # if len(code_list) == 0:x
        #     print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is not present on the page!")
        #     return False
        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is present on the page!")
        #
        # print(f"{datetime.now()}   QR_CODE_{self.filename.upper()} scroll =>")
        #
        # self.browser.execute_script(
        #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #     code_list[0]
        # )

        # try:
        # qr_code_locator = self.browser.find_element(*self.locator)
        # link = qr_code_locator.get_attribute
        # link = self.get_attribute("title", *self.locator_link)
        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} found")
        # print(f"{datetime.now()}   => Opening link from QR_CODE")
        # self.link = link
        # self.open_page()
        # self.browser.get(link)
        # self.wait_for_target_url('apps.apple.com', 10)

        # time.sleep(5)
        # ########### Не удалять ############
        # qr_code = self.browser.find_element(*self.locator)
        # src = qr_code.get_attribute('src')
        # # Download the image
        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} download started.")
        # urllib.request.urlretrieve(src, f"test_data/{self.filename}.png")
        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} downloaded.")
        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} scanning started.")
        #
        # # Load QR code image
        # reader = barcode.barcoderecognition.BarCodeReader(f"test_data/{self.filename}.png")
        #
        # # Read QR codes
        # recognized_results = reader.read_bar_codes()
        #
        # for x in recognized_results:
        #     url_end = x.code_text.find(" ")
        #     url_2 = x.code_text[0:url_end]
        # self.browser.get(url_2)
        # os.remove(f"test_data/{self.filename}.png")

        # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} scanned!")
        ####################################
        # except ElementClickInterceptedException:
        #     print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} NOT CLICKED")
        #
        # return True

    def check_qrcode_img_link(self, qr_img):
        """
        Checking QR-code image using some decoded ways:
            - CV2 - for simple, easy reading qr-code
            - PYZBAR - for medium encoding qr-code
            - QReader - for hard encoding and bad reading qr-code
        """
        qr_code_image = 'qr_image.png'
        qr_img.screenshot(qr_code_image)
        # qr_code_image = 'qr_image10.png'
        # считывание qr-coda CV2-decoder
        qr_link = decoder_cv2(qr_code_image)
        if qr_link:
            print(f"{datetime.now()}   QR_CODE_LINK_CV2= ", qr_link)
        else:
            # assert False, ("The QR-code has a complex encryption method and is NOT"
            #                " readable by almost all types of mobile devices.")

            qr_link = decoder_pyzbar(qr_code_image)
            if qr_link:
                # считывание qr-coda PYZBAR-decoder
                print(f"{datetime.now()}   QR_CODE_LINK_PYZBAR= ", qr_link)
            else:
                # assert False, ("QR-code has a complex encryption method and is virtually "
                #                   "unreadable by mobile devices.")
                # считывание qr-coda QReader-decoder
                qr_link = decoder_qreader(qr_code_image)
                if qr_link:
                    print(f"{datetime.now()}   QR_CODE_LINK_QREADER= ", qr_link)
                else:
                    print("The QR-code is unreadable.")
                    os.remove(qr_code_image)
                    assert False, "Bug! The QR-code is unreadable or absent."

        # Сделать скриншот
        allure.attach(self.browser.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        # Удаляем временный файл qr_image.png
        os.remove(qr_code_image)
        return qr_link


def decoder_cv2(qr_image):
    # Декодируем информацию из изображения qr-кода cv2
    qr_code_data_cv2 = None
    try:
        print(f"{datetime.now()}   Start QR-code decryption with CV2-method =>")
        img_qrcode = cv2.imread(qr_image)
        detector = cv2.QRCodeDetector()
        # Сохраняем информацию из qr-кода в переменную
        qr_code_data_cv2, bbox, qr_clear = detector.detectAndDecode(img_qrcode)
        if qr_code_data_cv2:
            print(f"{datetime.now()}   The QR-code has a simple encryption method and is readable by almost "
                  "all types of mobile devices.")
            return qr_code_data_cv2
        else:
            qr_code_data_cv2 = None
            print(f"{datetime.now()}   The QR-code has a medium encryption method and is NOT "
                  "readable by some types of mobile devices.")
    except FileNotFoundError:
        return qr_code_data_cv2


def decoder_pyzbar(qr_image):
    # Декодируем информацию из изображения qr-кода pyzbar
    qr_code_data_pyzbar = None
    try:
        print(f"{datetime.now()}   Start QR-code decryption with PYZBAR-method =>")
        qr_image = Image.open(qr_image)
        qr_info = decode(qr_image)
        if qr_info:
            # Сохраняем информацию из qr-кода в переменную
            qr_code_data_pyzbar = qr_info[0].data.decode('utf-8')
            print(f"{datetime.now()}   The QR-code has a medium encryption method and is readable by limited types of "
                  "mobile devices.")

            return qr_code_data_pyzbar
        else:
            print(f"{datetime.now()}   The QR-code has a complex encryption method and is NOT "
                  f"readable by almost all types of mobile devices.")
            qr_code_data_pyzbar = None

    except FileNotFoundError:
        return qr_code_data_pyzbar
    #


def decoder_qreader(qr_image):
    # Декодируем информацию из изображения qr-кода QReader
    qreader = QReader()
    try:
        print(f"{datetime.now()}   Start QR-code decryption with QREADER-method =>")
        image = cv2.cvtColor(cv2.imread(qr_image), cv2.COLOR_BGR2RGB)
        # Сохраняем информацию из qr-кода в переменную
        (qr_code_data_qreader,) = qreader.detect_and_decode(image=image)
        if qr_code_data_qreader:
            print(f"{datetime.now()}   The QR-code has a complex encryption method and is virtually "
                  "unreadable by mobile devices.")

            return qr_code_data_qreader
        else:
            print("The QR-code is unreadable.")

    except ValueError:
        print(f"{datetime.now()}   The QR-code is unreadable or absent.")
