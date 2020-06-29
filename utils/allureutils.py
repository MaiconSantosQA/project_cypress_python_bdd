import platform
import os
import allure

class Allure(object):
    """[summary]
    
    Arguments:
        object {[type]} -- [description]

    """

    @staticmethod
    def fill_environment_file(context):
        try:
            allure.title("Plataforma de Inovação P&D")
            abs_file_path_smoke = os.path.abspath("allure-results-smoke/environment.properties")
            abs_file_path_full = os.path.abspath("allure-results/environment.properties")
            my_file_smoke=open(abs_file_path_smoke, 'w')
            my_file_full=open(abs_file_path_full, 'w')
            Allure.fill_fields(context, my_file_smoke, "SMOKE")
            Allure.fill_fields(context, my_file_full, "FULL")

        except IOError:
            print("Error on fill allure environment file")

    @staticmethod
    def fill_fields(context, execution_file, execution_type):
        execution_file.write("\nBROWSER = " + context.driver.capabilities['browserName'])
        execution_file.write("\nBROWSER-VERSION = " +  str(context.driver.capabilities['version']))
        execution_file.write("\nRESOLUTION = " + str(context.resolution))
        execution_file.write("\nSTAGE = DESENVOLVIMENTO WEB (" + execution_type + ")")
        execution_file.write("\nPLATFORM = " + str(platform.system()))
        execution_file.write("\nPLATFORM-VERSION = " + str(platform.release()))
        execution_file.write("\nURL= " + context.application_url)
        execution_file.close()