
import os
import yaml
import time
import glob
import string



class Config(object):
    """Config open config.yml file and set your fields to context.config
    """

    @staticmethod
    def configure_yml_file(context):
        with open(os.getcwd() + os.path.sep + "config.yml", 'r') as ymlfile:
            context.config = yaml.load(ymlfile)
