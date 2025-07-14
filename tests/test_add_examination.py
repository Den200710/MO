import random
import time
import allure
import pytest
from Base.base_test import BaseTest

@allure.feature("Add examination")
class TestAddNewExamination(BaseTest):

    @allure.title("Add new examination")
    @allure.severity("Critical")
    #@pytest.mark.smoke
    def test_add_new_examination(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_button()
        self.login_page.click_select_company()
        self.left_sidebar.is_opened()
        time.sleep(2)
        self.left_sidebar.click_examinations_page()
        self.examinations_page.is_opened()
        self.examinations_page.click_new_examination()
        self.new_examination_page.is_opened()
        self.new_examination_page.add_company()
        self.new_examination_page.add_team()
        self.new_examination_page.select_type_examination()
        self.new_examination_page.select_member_of_commission()
        self.new_examination_page.name_of_examination()
        self.new_examination_page.select_responsible_examination()
        self.new_examination_page.dates_of_examination()
        self.new_examination_page.select_audit_scope()
        self.new_examination_page.save_examination()
        self.new_examination_page.check_name_of_new_examination()
