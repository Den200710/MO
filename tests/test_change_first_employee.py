import random
import time

import allure
import pytest

from Base.base_test import BaseTest

@allure.feature("Change employee")
class TestChangeThirdEmployee(BaseTest):

    @allure.title("Change lastname employee")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_lastname_third_employee(self):
        self.login_page.open()
        self.login_page.enter_login("sample@sample.com")
        self.login_page.enter_password("123654")
        self.login_page.click_button()
        self.login_page.click_select_company()
        self.left_sidebar.is_opened()
        self.left_sidebar.click_employees_page()
        self.employees_page.is_opened()
        self.employees_page.click_first_employee()
        self.first_employee.is_opened()
        self.first_employee.click_change_employee()
        self.edit_first_employee.field_first_name(f"Test {random.randint(1, 100)}")
        time.sleep(1)
        self.edit_first_employee.save_changes()
        time.sleep(3)

