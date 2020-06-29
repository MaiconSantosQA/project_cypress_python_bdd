
from features.support.locators.gamesclub import createaccount_locator
from features.support.pages.base_page import BasePage
import utils.seleniumutils as SU

class CreateAccount(BasePage):

    def __init__(self, context):
        super(CreateAccount, self).__init__(context)

    def fill_email(self, email):
        self.context.driver.find_element(*createaccount_locator.FIELD_EMAIL).clear()
        self.context.driver.find_element(*createaccount_locator.FIELD_EMAIL).send_keys(email)

    def fill_cemail(self, email):
        self.context.driver.find_element(*createaccount_locator.FIELD_CEMAIL).clear()
        self.context.driver.find_element(*createaccount_locator.FIELD_CEMAIL).send_keys(email)

    def fill_password(self, password):
        self.context.driver.find_element(*createaccount_locator.FIELD_PASSWORD).clear()
        self.context.driver.find_element(*createaccount_locator.FIELD_PASSWORD).send_keys(password)

    def fill_name(self, name):
        self.context.driver.find_element(*createaccount_locator.FIELD_NAME).clear()
        self.context.driver.find_element(*createaccount_locator.FIELD_NAME).send_keys(name)

    def fill_nickname(self, nickname):
        self.context.driver.find_element(*createaccount_locator.FIELD_NICKNAME).clear()
        self.context.driver.find_element(*createaccount_locator.FIELD_NICKNAME).send_keys(nickname)

    def click_next(self):
        self.context.driver.find_element(*createaccount_locator.BTN_NEXT).click()

    def click_register(self):
        self.context.driver.find_element(*createaccount_locator.BTN_REGISTER).click()

    def view_congratulation(self):
        element = createaccount_locator.VIEW_CONGRATULATION
        SU.wait_for_element_located(self.context.driver, 5, element)



