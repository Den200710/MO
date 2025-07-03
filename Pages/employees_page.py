import os
import time

import allure
import pandas
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links
from selenium.webdriver.common.alert import Alert

class EmployeesPage(Base):

    path = "C:\\Users\\User\\PycharmLessons\\MO\\Downloads\\Список сотрудников.xlsx"
    fio_employees = "Абеленцев Роман Сергеевичр"

    PAGE_URL = Links.EMPLOYEES_PAGE

    select_third_employee = ("xpath", "//div[contains(text(), 'Алтынбаева')][1]")
    button_print_form = ("xpath", "//button[@title='Печать списка']")
    button_select_exel = ("xpath", "(//li[contains(@class, 'smartlist-print')])[2]")
    button_download = ("xpath", "//a[contains(@href, 'download')]")

    @allure.step("Click third employee")
    def click_third_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.select_third_employee)).click()

    @allure.step("Click print form employees")
    def click_button_print_form(self):
        self.wait.until(EC.element_to_be_clickable(self.button_print_form)).click()
    @allure.step("Select exel print form employees")
    def click_button_select_exel(self):
        self.wait.until(EC.element_to_be_clickable(self.button_select_exel)).click()
    @allure.step("Download exel print form employees")
    def click_button_download(self):
        self.wait.until(EC.element_to_be_clickable(self.button_download)).click()

        download_dir = "C:\\Users\\User\\PycharmLessons\\MO\\Downloads"
        original_file_name = "Список сотрудников.xlsx.crdownload"
        final_file_name = "Список сотрудников.xlsx"

        original_file_path = os.path.join(download_dir, original_file_name)
        final_file_path = os.path.join(download_dir, final_file_name)

        # Ждем появления файла с расширением .crdownload (или другого временного расширения)
        while not os.path.exists(original_file_path):
            time.sleep(1)

        # Ждем пока файл перестанет изменяться (скачивание завершено)
        previous_size = -1
        while True:
            current_size = os.path.getsize(original_file_path)
            if current_size == previous_size:
                break  # Размер не меняется — скачивание завершено
            previous_size = current_size
            time.sleep(1)

        # После завершения скачивания — переименовываем файл
        os.rename(original_file_path, final_file_path)
    @allure.step("Assert fle")
    def check_employees_file(self):
        list_employees = pandas.read_excel(self.path)
        result = (list_employees["ФИО"] == self.fio_employees).any()
        assert result, "Такого чувака нет"
    @allure.step("Delete fle")
    def delete_employees_file(self):
        os.path.exists(self.path)
        os.remove(self.path)
