
from features.support.locators.gamesclub import hostemail_locator
from features.support.pages.base_page import BasePage
import utils.seleniumutils as SU
from selenium.webdriver.common.by import By
import time

class HostEmail(BasePage):

    def __init__(self, context):
        super(HostEmail, self).__init__(context)

    def fill_email(self, email):
        self.context.driver.find_element(*hostemail_locator.FIELD_EMAIL).clear()
        self.context.driver.find_element(*hostemail_locator.FIELD_EMAIL).send_keys(email)

    def click_confirm(self):
        self.context.driver.find_element(*hostemail_locator.BTN_CONFIRM).click()
        time.sleep(3)

    def click_email(self):
        self.context.driver.find_element(*hostemail_locator.BTN_EMAIL).click()

    def link_hostemail(self):
        self.context.driver.get("http://www.yopmail.com/en/")

    def view_email(self):
        time.sleep(2)
        self.context.driver.switch_to.frame(self.context.driver.find_element_by_id("ifmail"))
        element = hostemail_locator.VIEW_EMAIL
        SU.wait_for_element_located(self.context.driver, 10, element)







