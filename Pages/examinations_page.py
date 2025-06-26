import allure
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links

class ExaminationsPage(Base):

    PAGE_URL = Links.EXAMINATIONS_PAGE

    button_new_examination = ("xpath", "//span[contains(text(),'Добавить ВП')]")

    @allure.step("Click add new examination")
    def click_new_examination(self):
        self.wait.until(EC.element_to_be_clickable(self.button_new_examination)).click()
