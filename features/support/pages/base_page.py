# -*- coding: UTF-8 -*-
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
import utils.seleniumutils as SU
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    """All page classes must extend this class in order to use the webdriver actions
    """

    def __init__(self, context):
        self.context = context

    @property
    def base_url(self):
        return self.context.application_url

    @property
    def get_url(self):
        return self.context.driver.current_url

    def navigate(self, url):
        self.context.driver.get(url)

    def select_element_visible_text(self, time, locator, value):
        """[summary]
        
        Arguments:
            time {[type]} -- [description]
            locator {[type]} -- [description]
            value {[type]} -- [description]
        """
        select_element = SU.wait_for_element_located(self.context.driver, time, locator)

        try:
            if value is not None:
                Select(select_element).select_by_visible_text(value)
                return True
        except NoSuchElementException:
            return False

    def select_element(self, time, locator):
        """[summary]
        
        Arguments:
            time {[type]} -- [description]
            locator {[type]} -- [description]
        """
        select_element = SU.wait_for_element_located(self.context.driver, time, locator)

        return Select(select_element)

    def select_input_element(self, time, locator, value):
        try:
            element = SU.wait_for_element_to_be_clickable(self.context.driver, time, locator)
            element.click()
            actions = ActionChains(self.context.driver)
            actions.send_keys(value)
            actions.pause(2)
            actions.send_keys(Keys.ENTER).perform()
            value_selected = element.text
            if value_selected is value:
                return True
            else:
                return False
        except TimeoutException:
            return False
