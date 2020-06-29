# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
# ----------------------------------------------------------------------------
#   SUPPORTED LOCATOR STRATEGIES:
#       * XPATH
#       * ID
#       * NAME
#       * CSS_SELECTOR
#       * TAG_NAME
#       * LINK_TEXT
#       * PARTIAL_LINK_TEXT
# ----------------------------------------------------------------------------


FIELD_EMAIL = (By.XPATH, "(//input[contains(@type, 'email')])[1]")
FIELD_CEMAIL = (By.XPATH, "(//input[contains(@type, 'email')])[2]")
FIELD_PASSWORD = (By.XPATH, "//input[contains(@type, 'password')]")
FIELD_NAME = (By.ID, "name")
FIELD_NICKNAME = (By.ID, "nickname")

BTN_CREATEACCOUNT = (By.XPATH, "//button[contains(text(),'Criar conta')]")
BTN_REGISTER = (By.XPATH, "//button[contains(text(),'Cadastrar')]")
BTN_NEXT = (By.XPATH, "//button[contains(text(), 'Próximo')]")
VIEW_CONGRATULATION = (By.XPATH, "//P[contains(text(), 'Parabéns!')]")
