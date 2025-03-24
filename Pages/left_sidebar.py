from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LeftSidebar():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    ecological_aspect = "//*[contains(text(),'Экологические аспекты')]"

    # Getters

    def get_scroll_ecological_aspect(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ecological_aspect)))


    # Actions


    # Methods

    """Method scroll ecological aspect"""
    def scroll_ecological_aspect(self):
        ecological_aspect = self.get_scroll_ecological_aspect()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ecological_aspect)


