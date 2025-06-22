import allure
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links

class ThirdEmployeePage(Base):

    PAGE_URL = Links.THIRD_EMPLOYEES_PAGE

    button_change_employee = ("xpath", "//button/span[text()='Изменить']")

    @allure.step("Click change employee")
    def click_change_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.button_change_employee)).click()
