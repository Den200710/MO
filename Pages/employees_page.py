import os
from pathlib import Path
import allure
import pandas
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links


class EmployeesPage(Base):

    parent_directory = Path(os.path.dirname(os.getcwd()))
    download_dir = parent_directory / 'Downloads'
    path = download_dir / "Список сотрудников.xlsx"
    inactiv_employee = "Абдрафиков Чингиз Данирович"

    PAGE_URL = Links.EMPLOYEES_PAGE

    select_first_employee = ("xpath", "(//div[contains(@class,'employee-fio-formatter_root')])[1]")
    button_print_form = ("xpath", "//button[@title='Печать списка']")
    select_format_describe = ("xpath", "//span[@id='format-describe']")
    button_select_exel = ("xpath", "//span[@class='rs-picker-select-menu-item']")
    button_generate_report = ("xpath", "(//button[contains(@class,'rs-btn-green')])[2]")
    button_download = ("xpath", "//a[contains(@href,'download')]")


    @allure.step("Click third employee")
    def click_first_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.select_first_employee)).click()

    @allure.step("Click print form employees")
    def click_button_print_form(self):
        self.wait.until(EC.element_to_be_clickable(self.button_print_form)).click()
    @allure.step("Click select_format_describe")
    def click_select_format_describe(self):
        self.wait.until(EC.element_to_be_clickable(self.select_format_describe)).click()

    @allure.step("Select exel print form employees")
    def click_button_select_exel(self):
        self.wait.until(EC.element_to_be_clickable(self.button_select_exel)).click()
    @allure.step("Generate exel print form employees")
    def click_button_generate_report(self):
        element = self.wait.until(EC.element_to_be_clickable(self.button_generate_report))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Download exel print form employees")
    def click_button_download(self):
        self.wait.until(EC.element_to_be_clickable(self.button_download)).click()
        temp_filename = "Список сотрудников.xlsx.crdownload"
        final_filename = "Список сотрудников.xlsx"

        temp_file_path = self.download_dir / temp_filename
        final_file_path = self.download_dir / final_filename
        # Вызов метода из базового класса
        self.wait_for_download_completion(temp_file_path)
        # Переименование файла после завершения скачивания
        temp_file_path.rename(final_file_path)

    @allure.step("Assert file")
    def check_employees_file(self):
        list_employees = pandas.read_excel(self.path)
        result = (list_employees["ФИО"] == self.fio_employees).any()
        assert result, "Такого чувака нет"
        assert not (list_employees["ФИО"] == self.inactiv_employee).any(), "В списке неактивный чувак"
    @allure.step("Delete file")
    def delete_employees_file(self):
        os.path.exists(self.path)
        os.remove(self.path)

    @allure.step("Get_fio_first_employee")
    def get_fio_first_employee(self):
        self.fio_employees = self.wait.until(EC.element_to_be_clickable(self.select_first_employee)).text
        print(f'ФИО первого сотрудника{self.fio_employees}')

