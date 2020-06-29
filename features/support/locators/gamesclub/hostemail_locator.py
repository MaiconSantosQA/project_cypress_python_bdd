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


BTN_EMAIL = (By.XPATH, "//input[contains(@value, 'Check Inbox')]")
BTN_CONFIRM = (By.XPATH, "//a[contains(@title, 'Confirmar')]")

FIELD_EMAIL = (By.ID, "login")

VIEW_EMAIL = (By.XPATH, "//h1[contains(text(), 'Confirme sua conta')]")
FRAME = (By.ID, "ifmail")
