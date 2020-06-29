# -*- coding: UTF-8 -*-

from selenium import webdriver

class SeleniumDriverFactory(object):
    """Driver factory to provide driver for running tests on web browsers.
    Supported browsers are 'chrome' and 'chromeheadless.
    """
    def __init__(self, browser=None, platform='linux'):
        self.browser = browser
        self.platform = platform

    def get_driver(self):
                                     
        web_driver = getattr(self, self.browser)
        return web_driver()

    def chrome(self):   
        """Configure options for Chrome driver.
        Use screen resolution 1366 x 768.
        
        Returns:
            Webdriver -- Returns Chrome webdriver
        """
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1366,768")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--lang=pt_BR")
        return webdriver.Chrome(chrome_options=options)
    
    def chrome_responsive(self):
        """Configure options for Chromeheadless driver.
        Use screen resolution 375 x 667 (Iphone 8).

        Returns:
            Webdriver -- Returns Chromeheadless webdriver
        """
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=375,667")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--lang=pt_BR")
        return webdriver.Chrome(chrome_options=options)

    def chromeheadless(self):
        """Configure options for Chromeheadless driver.
        Use screen resolution 1366 x 768.

        Returns:
            Webdriver -- Returns Chromeheadless webdriver
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1366,768")
        options.add_argument("--disable-gpu")  
        options.add_argument("--incognito")  
        options.add_argument("--disable-extensions")  
        options.add_argument("--no-sandbox")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-first-run")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--enable-logging")
        options.add_argument("--lang=pt_BR")
        return webdriver.Chrome(chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    def chromeheadless_responsive(self):
        """Configure options for Chromeheadless driver.
        Use screen resolution 375 x 667 (Iphone 8).

        Returns:
            Webdriver -- Returns Chromeheadless webdriver
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=375,667")
        options.add_argument("--disable-gpu")  
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--lang=pt_BR")
        return webdriver.Chrome(chrome_options=options)