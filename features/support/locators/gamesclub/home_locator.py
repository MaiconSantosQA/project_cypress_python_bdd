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


BTN_CREATEACCOUNT = (By.XPATH, "//button[contains(text(), 'Criar conta')]")
BTN_ENTER = (By.XPATH, "//button[contains(@data-test, 'login')]")
FIELD_LOGIN = (By.ID, "email")
CHECK_LOGIN = (By.XPATH, "(//div[contains(text(), 'te')])[2]")
BTN_LOGIN = (By.XPATH, "//button[contains(text(), 'Entrar')]")
VIEW_MESSAGE_ERRO = (By.XPATH, "//p[contains(text(),'Credenciais inválidas. Tente novamente.')]")

