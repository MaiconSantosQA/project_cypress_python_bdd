
from features.support.locators.gamesclub import home_locator
from features.support.pages.base_page import BasePage
import utils.seleniumutils as SU

class HomePage(BasePage):

    def __init__(self, context):
        super(HomePage, self).__init__(context)

    def click_createaccount(self):
        self.context.driver.find_element(*home_locator.BTN_CREATEACCOUNT).click()

    def link(self):
        self.context.driver.get("https://gamersclub.gg/lol")

    def click_login(self):
        self.context.driver.find_element(*home_locator.BTN_LOGIN).click()

    def fill_login(self, login):
        self.context.driver.find_element(*home_locator.FIELD_LOGIN).clear()
        self.context.driver.find_element(*home_locator.FIELD_LOGIN).send_keys(login)

    def check_login(self):
        element = home_locator.CHECK_LOGIN
        SU.wait_for_element_located(self.context.driver, 5, element)

    def click_enter(self):
        self.context.driver.find_element(*home_locator.BTN_ENTER).click()

    def view_message_erro(self):
        element = home_locator.VIEW_MESSAGE_ERRO
        SU.wait_for_element_located(self.context.driver, 5, element)
