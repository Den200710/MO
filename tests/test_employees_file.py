import random
import time

import allure
import pytest
from Pages.employees_page import EmployeesPage
from Base.base_test import BaseTest

@allure.feature("Change employee")
class TestPrintFormEmployees(BaseTest):

    @allure.title("Check print form exel employees")
    @allure.severity("Minor")
    @pytest.mark.smoke
    def test_print_form_exel_employees(self, driver):
        self.login_page.open()
        self.login_page.enter_login("sample@sample.com")
        self.login_page.enter_password("123654")
        self.login_page.click_button()
        self.login_page.click_select_company()
        self.left_sidebar.is_opened()
        self.left_sidebar.click_employees_page()
        self.employees_page.is_opened()
        self.employees_page.click_button_print_form()
        self.employees_page.click_button_select_exel()

        self.employees_page.click_button_download()
        employees_page = EmployeesPage(driver)
        employees_page.delete_employees_file()
