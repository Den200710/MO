import allure
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links

class EmployeesPage(Base):

    PAGE_URL = Links.EMPLOYEES_PAGE

    select_third_employee = ("xpath", "//div[contains(text(), 'Алтынбаева')][1]")

    @allure.step("Click third employee")
    def click_third_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.select_third_employee)).click()