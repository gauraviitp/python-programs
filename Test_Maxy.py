import unittest
import time
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ChromeTestOjb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            'C:\\Selenium\\chromedriver_win32\\chromedriver.exe')
        #self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(5)

    def clickElementAfterMove(self, elementId):
        actions = ActionChains(self.driver)
        elem = self.driver.find_element_by_id(elementId)
        actions.move_to_element(elem).click().perform()

    def clickElement(self, elementId):
        elem = self.driver.find_element_by_id(elementId)
        elem.click()

    def selectElement(self, elementId, selectOptionText):
        select = Select(self.driver.find_element_by_id(elementId))
        select.select_by_visible_text(selectOptionText)

    def InputTextElement(self, elementId, text):
        elem = self.driver.find_element_by_id(elementId)
        elem.send_keys(text)

    def oneTrust(self):
        try:
            self.clickElement("onetrust-accept-btn-handler")
        except:
            pass

    def preLoginLandingPage(self):
        self.clickElement("book-without-online-account-link")
        self.clickElement("checkbox-label")
        self.clickElement("start-booking-button")

    def titleAndName(self):
        self.selectElement('Titles_Value', 'Mr')
        self.InputTextElement("FirstName", "x")
        self.InputTextElement("LastName", "x")
        self.clickElement("btnSubmitRegForm")

    def accountAndPostCode(self, accountNumber, postCode):
        self.InputTextElement("AccountNumber", accountNumber)
        self.InputTextElement("PostCode", postCode)
        self.clickElement("btnSubmitRegForm")

        time.sleep(2)
        try:
            self.clickElement("btnSubmitRegForm")
        except:
            pass

    def emailAndPhone(self):
        self.InputTextElement("EmailAddress", "test@test.com")
        self.InputTextElement("ConfirmEmailAddress", "test@test.com")
        self.InputTextElement("PhoneNumber", "1234567890")
        self.clickElement("btnSubmitRegForm")

    def confirmAddress(self):
        self.clickElement("continue-booking-button")

    def yourHeating(self):
        try:
            self.clickElement("yesHeating")

            time.sleep(5)
        except:
            pass

        try:
            self.clickElement("modal-button")
        except:
            pass

    def meterReading(self):
        self.clickElement("choose-half-hourly-button")

    def calendar(self):
        elem = self.driver.find_element_by_xpath(
            "//a[@data-am='True'][@data-pm='True']")
        elem.click()

        self.clickElement("select-am-button-calendar")

    def summary(self):
        self.clickElement("book-installation-button")

    def login(self, userName, password):
        self.InputTextElement("UserName", userName)
        self.InputTextElement("Password", password)
        self.clickElementAfterMove("form-control__checkbox--rememberme")
        self.clickElement("login-form-submit")

    def dashboard(self):
        elem = self.driver.find_element_by_xpath(
            "//li[@data-text='Readings & usage']")
        elem.click()

        elem = self.driver.find_element_by_partial_link_text(
            'Get a smart meter')
        elem.click()

    def postLoginLandingPage(self):
        self.clickElement("checkbox-label")
        self.clickElement("start-booking-button")

    def phoneNumber(self):
        self.InputTextElement("PhoneNumber", "1234567890")
        self.clickElement("btnSubmitPhoneNumber")

    ##### tests start #####
    @parameterized.expand([
        ('digitaltest030@stub.com', 'Sse01PreProd'),
        ('digitaltest033@stub.com', 'Sse01PreProd')
    ])
    def test_ojb_postlogin(self, userName, password):
        self.driver.get(
            "https://env06-my-dev.dev.digitalsse.cloud/your-products?mmcore.enc.pr=uDCeEZD3A8UkS1vaNv2FsL%2bHnZPZxTJI0rcXNh3KMOF95c%2fRAhVbsrsebol6pMqLBPpWc4aL4oSYAcpUMjFYHr4IALsgdtG0cA1KrSd1VMmckw%2bep96noyFLIOqEvjQy8dpFB8ThYVhsEDAleP0b8ReCtRGpqY%2fiRFtf6x5%2bKPBTBBFx%2fuHdDW%2f2Jqc2s4MRtTEk65DOp25Cys%2bJQAHZqwpjDbvoeUdm2WQtnqu%2bnv9O2R7izM5%2bML1OeHLKlY5H&mmcore.cfgid=1")

        self.oneTrust()
        self.login(userName, password)
        self.oneTrust()
        # self.dashboard()
        # self.postLoginLandingPage()
        # self.phoneNumber()

        # self.yourHeating()
        # self.meterReading()
        # self.calendar()
        # self.summary()

        # assert on the confirmation page
        # time.sleep(5)
        #assert self.driver.current_url == 'https://env06-my-dev.dev.digitalsse.cloud/smart-meters/confirmation'

    @parameterized.expand([
        ('1000000331', 'PO1 1BC'),
        ('1000000302', 'PO1 1BA')
    ])
    def test_ojb_prelogin(self, accountNumber, postCode):
        self.driver.get(
            "https://env06-my-dev.dev.digitalsse.cloud/smart-meters/get-a-smart-meter/book-your-installation")

        self.oneTrust()
        self.preLoginLandingPage()
        self.titleAndName()
        self.accountAndPostCode(accountNumber, postCode)
        self.emailAndPhone()
        self.confirmAddress()

        self.yourHeating()
        self.meterReading()
        self.calendar()
        self.summary()

        # assert on the confirmation page
        time.sleep(5)
        assert self.driver.current_url == 'https://env06-my-dev.dev.digitalsse.cloud/smart-meters/confirmation'

    ##### tests end #####

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
