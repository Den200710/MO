import pytest

from Pages.login_page import LoginPage
from Pages.left_sidebar import LeftSidebar
from Pages.employees_page import EmployeesPage
from Pages.edit_third_employee import EditThirdEmployeePage
from Pages.third_employee import ThirdEmployeePage

class BaseTest:

    login_page : LoginPage
    left_sidebar : LeftSidebar
    employees_page : EmployeesPage
    edit_third_employee : EditThirdEmployeePage
    third_employee : ThirdEmployeePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.left_sidebar = LeftSidebar(driver)
        request.cls.employees_page = EmployeesPage(driver)
        request.cls.edit_third_employee = EditThirdEmployeePage(driver)
        request.cls.third_employee = ThirdEmployeePage(driver)
