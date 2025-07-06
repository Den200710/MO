import allure
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links
from selenium.webdriver import Keys

class EditFirstEmployeePage(Base):

    PAGE_URL = Links.EDIT_THIRD_EMPLOYEES_PAGE

    first_name_field = ("xpath", "//input[@id='first_name']")
    save_button = ("xpath", "//button[text()='Сохранить']")


    def field_first_name(self, new_first_name):
        with allure.step(f"Change name on '{new_first_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.first_name_field))
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            assert first_name_field.get_attribute("value") == "", "There is text"
            first_name_field.send_keys(new_first_name)

    @allure.step("Click save change")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
