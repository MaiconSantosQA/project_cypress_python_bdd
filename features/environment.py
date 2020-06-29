# -*- coding: UTF-8 -*-

from utils import loggerutils

from behave.model import Scenario
from features.driverfactory import SeleniumDriverFactory
from utils.reportutils import Report
from utils.configutils import Config
from utils.allureutils import Allure

from support.pages.gamesclub.home_page import HomePage
from support.pages.gamesclub.createaccount_page import CreateAccount
from support.pages.gamesclub.hostemail_page import HostEmail


# ----------------------------------------------------------------------------
# before_step(context, step), after_step(context, step)
#   * These run before and after every step.
#   * The step passed in is an instance of Step.
# before_scenario(context, scenario), after_scenario(context, scenario)
#   * These run before and after each scenario is run.
#   * The scenario passed in is an instance of Scenario.
# before_feature(context, feature), after_feature(context, feature)
#   * These run before and after each feature file is exercised.
#   * The feature passed in is an instance of Feature.
# before_tag(context, tag), after_tag(context, tag)
#   * These run before and after each tag.
#   * The tag passed in is an instance of Tag
# ----------------------------------------------------------------------------

def before_all(context):
    """Set up test environment
    Create driver based on the desired capabilities provided.
    Valid desired capabilities can be 'chrome' or 'chromeheadless'.
    For adding new drivers add a new method in DriverFactory class.

    :param context: Holds contextual information during the running of tests
    :return: None
    """
    userdata = context.config.userdata
    continue_after_failed = userdata.getbool("runner.continue_after_failed_step")
    Scenario.continue_after_failed_step = continue_after_failed

    setup_debug_on_error(context.config.userdata)

    context.environment = userdata.get("environment")
    context.stage = userdata.get("stage")

    setup_env(context)

def before_feature(context, feature):
    """Set up driver, launch browser, open application and starting of execution of feature
   :param context: Holds contextual information during the running of tests
   :param feature: Holds contextual information about the feature during the running of tests
   :return: None
   """
    setup_driver(context)
    context.driver.get(context.application_url)
    

def before_scenario(context, scenario):
    """Initialize all pages, preparing to test it
    :param context: Holds contextual information during the running of tests
    :param scenario: Holds contextual information about scenario during the running of tests
    :return: None
    """
    init_pages(context)
          

def after_step(context, step):
    """Save screenshot in case of test step failure
    This function runs everytime after a step is executed. Check is step passed, then just log it and return
    if step fails and step is a part of portal scenario, take the screenshot of the failure. The screenshot file name
    is scenario_name.png where spaces within step name is replaced by '_'
    example: Login_do_usuário_2018-08-19_12-34-32.png
    :param context: Holds contextual information during the running of tests
    :param step: Holds contextual information about step during the running of tests
    :return: None
    """
    Report.take_screenshot(context, step)

    # if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
    #     # -- ENTER DEBUGGER: Zoom in on failure location.
    #     # NOTE: Use IPython debugger, same for pdb (basic python debugger).
    #     import ipdb
    #     ipdb.post_mortem(step.exc_traceback)

def after_scenario(context, scenario):
    """
    :param context: Holds contextual information during the running of tests
    :param scenario: Holds contextual information about scenario during the running of tests
    :return: None
    """
    Report.take_screenshotAll(context)

    try:
        if scenario.status == 'failed':
            context.logger.info(context.file_name)
    except AttributeError:
        return
    

def after_feature(context, feature):
    """Close browser and quit driver
    :param context: Holds contextual information during the running of tests
    :param feature: Holds contextual information about feature during the running of tests
    :return: None
    """
    close_driver(context)
    
def after_all(context):
    """
    :param context: Holds contextual information during the running of tests
    :return: None
    """


def before_tag(context, tag):
    """Configure actions before features or scenarios by tagging specifis tags
    For more specifics behaviors by after_tag, add in this method.
    Arguments:
        context -- Holds contextual information during the running of tests
        tag -- Word used before feature or scenario, used to control the execution. 
        Always starts with  @.
    """

    if 'login' in tag:
        context.scenario.login_page.login(context.user, context.password)
    




        
def after_tag(context, tag):
    """Configure actions after features or scenarios by tagging specifis tags
    For more specifics behaviors by after_tag, add in this method.
    Arguments:
        context -- Holds contextual information during the running of tests
        tag -- Word used before feature or scenario, used to control the execution. 
        Always starts with  @.
    """
    if 'logout' in tag:
        context.scenario.navbar_page.logoff_user()
    
        
def setup_env(context):
    """Set up test environment: Load params from yml file, configure logs, remove old logs and screenshots.
    
    Arguments:
        context  -- Holds contextual information during the running of tests
    """
    Config.configure_yml_file(context)
    loggerutils.setup_logging()
    loggerutils.setup_unformatted_logging(context)
    loggerutils.delete_old_logs_file(context)
    Report.delete_old_screenshots(context)
    Report.delete_old_reports(context)

def setup_driver(context):
    """Set up test driver: Configure driver by yml params. 
    Use tag @ci to define chrome or chromeheadless browser execution.
    
    Arguments:
        context -- Holds contextual information during the running of tests
        feature -- Holds contextual information about feature during the running of tests
    """

    context.browser = context.config[context.environment]['browser']
    context.resolution = context.config[context.environment]['resolution']

    # Get the appropriate driver for the browser specified in config.yml file
    driver_factory = SeleniumDriverFactory(context.browser)

    context.driver = driver_factory.get_driver()
    context.driver.delete_all_cookies()

    # Set driver implicit timeout. 
    # Webdriver will keep polling for the element for the specified timeout period.
    timeout = context.config[context.environment]['implicit_timeout']

    context.driver.implicitly_wait(timeout)

    context.application_url = context.config[context.stage]
    context.user = context.config[context.environment]['user']
    context.password = context.config[context.environment]['password']

    Allure.fill_environment_file(context)

def close_driver(context):
    """Verify if driver is alive and close it.
    
    Arguments:
        context -- Holds contextual information during the running of tests
    """

    if context.driver is not None:
        try:
            context.driver.close()
        except Exception as e:
            context.logger.error("Unable to close browser window! Error: %s" % e, exc_info=True)

        try:
            context.driver.quit()
        except Exception as e:
            context.logger.error("Unable to quit driver! Error: %s" % e, exc_info=True)

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def init_pages(context):
    """Initialize all pages available to test.
    
    Arguments:
        context -- Holds contextual information during the running of tests
    """
    context.scenario.home_page = HomePage(context)
    context.scenario.createaccount_page = CreateAccount(context)
    context.scenario.hostemail_page = HostEmail(context)







