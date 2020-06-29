from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
    StaleElementReferenceException, NoSuchElementException


def wait_for_element_located(driver, time, element_locator):
    try:
        return WebDriverWait(driver, time).until(
            EC.presence_of_element_located(element_locator)
        )
    except:
        raise NoSuchElementException('Element not located')


def wait_for_element_unlocated(driver, time, element):
    try:
        if hasattr(element, 'class'):
            WebDriverWait(driver, time).until(
                EC.staleness_of(element)
        )
    except:
        return False


def wait_for_element_to_be_clickable(driver, time, element_locator):
    try:
        return WebDriverWait(driver, time).until(
            EC.element_to_be_clickable(element_locator)
        )
    except:
        raise NoSuchElementException('Element not clickable')


def wait_for_element_visible(driver, time, element):
    try:
        return WebDriverWait(driver, time).until(
            EC.visibility_of(element)
        )
    except:
        raise NoSuchElementException('Element not visible')


def wait_for_url_to_be(driver, time, new_url):
    try:
        WebDriverWait(driver, time).until(EC.url_to_be(new_url))
        return True
        
    except TimeoutException:
        return False
