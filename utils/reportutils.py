import os
import time
import glob
import allure
from utils.loggerutils import logging
from pathlib import Path

from time import strftime

class Report(object):
    """Wrapper functions on report actions
    Usage:
        Report.take_screenshot(context)
        Report.delete_old_screenshot(context)
    """

    @staticmethod
    def take_screenshot(context, step):
        if step.status == "Passed":

            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')

            __current_scenario_name = context.scenario.name.split("--")[0]
            __screenshot_file_name = "screenshots" + os.path.sep + __current_scenario_name.replace(" ", "_") + "_" + \
                                    strftime("%Y-%m-%d_%H-%M-%S") + '.png'

            context.driver.save_screenshot(__screenshot_file_name)

            allure.attach.file(__screenshot_file_name,__screenshot_file_name,
                            allure.attachment_type.PNG)
    
    @staticmethod
    def take_screenshotAll(context):
       
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')

            __current_scenario_name = context.scenario.name.split("--")[0]
            __screenshot_file_name = "screenshots" + os.path.sep + __current_scenario_name.replace(" ", "_") + "_" + \
                                    strftime("%Y-%m-%d_%H-%M-%S") + '.png'

            context.driver.save_screenshot(__screenshot_file_name)

            allure.attach.file(__screenshot_file_name,__screenshot_file_name,
                            allure.attachment_type.PNG)                        

    @staticmethod
    def delete_old_screenshots(context):
        try:
            for images in os.listdir('screenshots'):
                os.remove(os.path.join('screenshots', images))
        except Exception as e:
            context.logger.error("Unable to delete old screenshots files! Error: %s" % e)

    @staticmethod
    def delete_old_reports(context):
        
        try:
            for f in os.listdir('allure-results'):
                if  f.lower().endswith('.json') or f.lower().endswith('.png') or f.lower().endswith('.csv'):
                    os.remove(os.path.join('allure-results', f))

        except Exception as e:
            context.logger.error("Unable to delete old allure reports files! Error: %s" % e)