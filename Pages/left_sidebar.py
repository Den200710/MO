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

    @allure.step("Go to 'Examinations' page")
    def click_examinations_page(self):
        element = self.wait.until(EC.element_to_be_clickable(self.examinations))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()


