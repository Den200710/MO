import os
import time

import allure
import pytest
from Pages.employees_page import EmployeesPage
from Base.base_test import BaseTest

@allure.feature("Check save print employees file")
class TestPrintFormEmployees(BaseTest):

    @allure.title("Check print form exel employees")
    @allure.severity("Minor")
    @pytest.mark.auth
    def test_print_form_exel_employees(self, driver):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_button()
        self.login_page.click_select_company()
        self.left_sidebar.is_opened()



