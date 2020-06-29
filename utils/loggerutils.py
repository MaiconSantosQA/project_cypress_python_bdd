# -*- coding: UTF-8 -*-

import os
import logging
import time
import string

from logging.config import dictConfig
from time import strftime

# Log folder directory
LOG_DIR = "logs"

# Logger configuration settings
LOG_SETTINGS = {

    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'formatted_console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'formatted_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': "logs" + os.path.sep + "uitests_" + strftime("%Y-%m-%d_%H_%M_%S") + ".log",
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'unformatted_console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'blank',
            'stream': 'ext://sys.stdout',
        },
        'unformatted_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'blank',
            'filename': "logs" + os.path.sep + "uitests_" + strftime("%Y-%m-%d_%H_%M_%S") + ".log",
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
    },
    'formatters': {
        'detailed': {
            'format': '[%(levelname)s] : %(asctime)s : %(filename)s : %(funcName)s:%(lineno)d : %(message)s',
        },
        'blank': {
            'format': '',
        },
    },
    'loggers': {
        'formatted_log': {
                'level': 'DEBUG',
                'handlers': ['formatted_file', 'formatted_console']
            },
        'unformatted_log': {
            'level': 'DEBUG',
            'handlers': ['unformatted_file', 'unformatted_console']
        },
    }
}


def setup_logging():
    """Use the LOG_SETTINGS defined above and initialize the logger
    :return: None
    """
    logging.config.dictConfig(LOG_SETTINGS)


def setup_formatted_logging(context):
    """Formatted log includes file name, time stamp and log levels
    :param context: Holds contextual information
    :return: None
    """
    context.logger = logging.getLogger('formatted_log')


def setup_unformatted_logging(context):
    """Unformatted logging doesn't include file name, timestamp and/or log levels
    Ideal for situations where you want to print some messages to log where the above
    parameters are not required. For example to print a message to screen that
    "Testing is started ...", We do not need to include the file name, time stamp or
    log levels. It helps in separating the different section of log files and makes
    them more readable.
    :param context: Holds contextual information
    :return: None
    """
    context.logger = logging.getLogger('unformatted_log')

def log_before_all(context):

    #disable logger
    #logging.disable(logging.CRITICAL) 

    context.test_started_milli_time = int(round(time.time() * 1000))
    context.logger.info("\n")
    context.logger.info("=============================================================================================")
    context.logger.info("TESTING STARTED AT : " + strftime("%Y-%m-%d %H:%M:%S"))
    context.logger.info("=============================================================================================")
    context.logger.info("\n")

def log_before_feature(context, feature):

    context.logger.info("\n")
    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("STARTED EXECUTION OF FEATURE: " + str(feature.name))
    context.logger.info("Tags: " + str([str(item) for item in feature.tags]))
    context.logger.info("Filename: " + str(feature.filename))
    context.logger.info("Line: " + str(feature.line))
    context.logger.info("---------------------------------------------------------------------------------------------")

def log_before_scenario(context, scenario):
    
    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("STARTED EXECUTION OF SCENARIO: " + str(scenario.name))
    context.logger.info("Tags: " + str([str(item) for item in scenario.tags]))
    context.logger.info("Filename: " + str(scenario.filename))
    context.logger.info("Line: " + str(scenario.line))
    context.logger.info("---------------------------------------------------------------------------------------------")

def log_after_scenario(context, scenario):

    context.logger.info("\n")
    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("FINISHED EXECUTION OF SCENARIO: " + str(scenario.name))
    context.logger.info("Result: " + str(scenario.status).upper())
    context.logger.info("Time taken: " + str("{0:.2f}".format(scenario.duration / 60)) + " mins, " +
                        str("{0:.2f}".format(scenario.duration % 60)) + " secs")
    context.logger.info("---------------------------------------------------------------------------------------------")

def log_after_feature(context, feature):

    context.logger.info("\n")
    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("FINISHED EXECUTION OF FEATURE: " + str(feature.name))
    context.logger.info("Result: " + str(feature.status).upper())
    context.logger.info("Time taken: " + str("{0:.2f}".format(feature.duration / 60)) + " mins, " +
                        str("{0:.2f}".format(feature.duration % 60)) + " secs")
    context.logger.info("---------------------------------------------------------------------------------------------")

def log_after_all(context):

    context.logger.info("\n")
    context.logger.info("=============================================================================================")
    context.logger.info("TESTING FINISHED AT : " + strftime("%Y-%m-%d %H:%M:%S"))
    context.logger.info("=============================================================================================")
    context.logger.info("\n")

def delete_old_logs_file(context):

    now = time.time()
    number_of_days_to_keep_log_files = int(context.config[context.environment]['number_of_days_to_keep_log_files'])

    try:
        for f in os.listdir('logs'):
            if os.stat(os.path.join('logs', f)).st_mtime < now - number_of_days_to_keep_log_files * 86400 and \
                    f.lower().endswith('.log'):
                        os.remove(os.path.join('logs', f))
    except Exception as e:
        context.logger.error("Unable to delete old log files! Error: %s" % e)