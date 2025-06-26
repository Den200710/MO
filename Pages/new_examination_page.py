import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links
import random
from selenium.webdriver import Keys
from datetime import datetime


class NewExaminationPage(Base):

    PAGE_URL = Links.NEW_EXAMINATION_PAGE

    button_select_company = ("xpath", "(//div[contains(@class,'rs-btn-group')])[1]")
    select_first_company = ("xpath", "(//tr[@class='ui-table_has_action__M6b_l'])[1]")
    button_select_team = ("xpath", "(//div[contains(@class,'rs-btn-group')])[2]")
    select_first_team = ("xpath", "(//div[@class='team-node_root__AhXss'])[1]")
    field_type_check = ("xpath", "//span[@id='type-describe']")
    first_type_check = ("xpath", "(//span[@class='rs-picker-select-menu-item'])[1]")
    field_member_commission = ("xpath", "(//input[contains(class, rs-input)])[9]")
    button_add_commission = ("xpath", "//span[contains(text(),'Добавить члена комиссии')]")
    select_first_member_commission = ("xpath", "(//td[contains(@class,'ui-table_cell__cnEqM')])[1]")
    field_name_of_check = ("xpath", "//input[@id='name']")
    field_responsible = ("xpath", "//input[@id='responsible_id']")
    select_responsible = ("xpath", "(//td[contains(@class,'ui-table_cell__cnEqM')])[1]")
    field_start_check = ("xpath", "//input[@id='start_date']")
    now_day = ("xpath", "(//div[@tabindex='0'])[4]")
    field_finish_check = ("xpath", "//input[@id='complete_before']")
    field_audit_scope = ("xpath", "(//input[contains(class, rs-input)])[11]")
    audit_scope = ("xpath", "//div[contains(text(),'Технический надзор')]")
    button_save = ("xpath", "//button[@type='submit']")
    name_new_examination = ("xpath", "(//div[contains(@class,'view-header_title')])[2]")
    @allure.step("Add company")
    def add_company(self):
        self.wait.until(EC.element_to_be_clickable(self.button_select_company)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_first_company)).click()
        self.click_close_window()
    @allure.step("Add team")
    def add_team(self):
        self.wait.until(EC.element_to_be_clickable(self.button_select_team)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_first_team)).click()
        self.click_close_window()
    @allure.step("Select type examination")
    def select_type_examination(self):
        self.wait.until(EC.element_to_be_clickable(self.field_type_check)).click()
        self.wait.until(EC.element_to_be_clickable(self.first_type_check)).click()
    @allure.step("Select member of commission")
    def select_member_of_commission(self):
        self.wait.until(EC.element_to_be_clickable(self.field_member_commission)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_first_member_commission)).click()
    @allure.step("Name of examination")
    def name_of_examination(self):
        field_name_examination = self.wait.until(EC.element_to_be_clickable(self.field_name_of_check))
        self.driver.execute_script("arguments[0].scrollIntoView();", field_name_examination)
        time.sleep(1)
        examination_name = f"ВП {random.randint(1, 100)}"
        field_name_examination.send_keys(examination_name)
        self.var_name_of_examination = examination_name
    @allure.step("Select responsible")
    def select_responsible_examination(self):
        self.wait.until(EC.element_to_be_clickable(self.field_responsible)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_responsible)).click()
    @allure.step("Select dates of examination")
    def dates_of_examination(self):
        self.wait.until(EC.element_to_be_clickable(self.field_start_check)).click()
        self.wait.until(EC.element_to_be_clickable(self.now_day)).click()
        self.wait.until(EC.element_to_be_clickable(self.field_finish_check)).click()
        self.wait.until(EC.element_to_be_clickable(self.now_day)).click()
    @allure.step("Audit scope")
    def select_audit_scope(self):
        self.wait.until(EC.element_to_be_clickable(self.field_audit_scope)).click()
        self.wait.until(EC.element_to_be_clickable(self.audit_scope)).click()
    @allure.step("Click save exam")
    def save_examination(self):
        self.wait.until(EC.element_to_be_clickable(self.button_save)).click()
        time.sleep(1)
    @allure.step("Check name of new_examination")
    def check_name_of_new_examination(self):
        new_examination_name = self.wait.until(EC.element_to_be_clickable(self.name_new_examination)).text
        assert self.var_name_of_examination == new_examination_name, \
            f"Ожидалось: {self.var_name_of_examination}, но получено: {new_examination_name}"

