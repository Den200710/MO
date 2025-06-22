import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_class import Base
from config.links import Links


class LeftSidebar(Base):

    PAGE_URL = Links.COMMON_PAGE

    # Locators

    ecological_aspect = ("xpath", "//*[contains(text(),'Экологические аспекты')]")
    examinations = ("xpath", "//*[contains(text(),'Внутренние проверки')]")
    employees_page = ("xpath", "//*[contains(text(),'Персонал')]")

    @allure.step("Go to 'Employees' page")
    def click_employees_page(self):
        self.wait.until(EC.element_to_be_clickable(self.employees_page)).click()

    def get_scroll_ecological_aspect(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ecological_aspect)))
    def get_scroll_examinations(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.examinations)))

    # Actions


    # Methods

    """Method scroll ecological aspect"""
    def scroll_ecological_aspect(self):
        ecological_aspect = self.get_scroll_ecological_aspect()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ecological_aspect)
    def scroll_examinations(self):
        examinations = self.get_scroll_examinations()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", examinations)

