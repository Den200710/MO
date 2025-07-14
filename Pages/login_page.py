import os
from dotenv import load_dotenv
import allure
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from config.links import Links


class LoginPage(Base):
    load_dotenv(dotenv_path="C:\\Users\\User\\PycharmLessons\\MO\\.venv\\.env")
    PAGE_URL = Links.LOGIN_PAGE

    # Locators

    user_name = ("xpath", "//input[@id='username']")
    password = ("xpath", "//input[@id='password']")
    login_button = ("xpath", "//button[@type='submit']")
    main_word = ("xpath", "//div[@class='view-header_titles__3eiIN view-header_left_padding__mNHAb']")
    select_company = ("xpath", "(//div[contains(@class,'company')])[2]")

    # Getters
    @allure.step("Enter login")
    def enter_login(self):
        self.wait.until(EC.element_to_be_clickable(self.user_name)).send_keys(os.environ["LOGIN"])

    @allure.step("Enter password")
    def enter_password(self):
        self.wait.until(EC.element_to_be_clickable(self.password)).send_keys(os.environ["PASSWORD"])

    @allure.step("Click submit")
    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    @allure.step("Select company")
    def click_select_company(self):
        self.wait.until(EC.element_to_be_clickable(self.select_company)).click()



