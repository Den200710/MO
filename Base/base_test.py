import pytest

from Pages.login_page import LoginPage
from Pages.left_sidebar import LeftSidebar
from Pages.employees_page import EmployeesPage
from Pages.edit_first_employee import EditFirstEmployeePage
from Pages.first_employee import FirstEmployeePage
from Pages.examinations_page import ExaminationsPage
from Pages.new_examination_page import NewExaminationPage

class BaseTest:

    login_page : LoginPage
    left_sidebar : LeftSidebar
    employees_page : EmployeesPage
    edit_first_employee : EditFirstEmployeePage
    first_employee : FirstEmployeePage
    examinations_page : ExaminationsPage
    new_examination_page : NewExaminationPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.left_sidebar = LeftSidebar(driver)
        request.cls.employees_page = EmployeesPage(driver)
        request.cls.edit_first_employee = EditFirstEmployeePage(driver)
        request.cls.first_employee = FirstEmployeePage(driver)
        request.cls.examinations_page = ExaminationsPage(driver)
        request.cls.new_examination_page = NewExaminationPage(driver)
