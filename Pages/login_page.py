from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Login_page(Base):

    url = 'http://rc3.lan/'


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@id='username']"
    password = "//input[@id='password']"
    login_button = "//button[@type='submit']"
    main_word = "//div[@class='view-header_titles__3eiIN view-header_left_padding__mNHAb']"
    choice_company = "//*[@id='__next']/div[1]/div/div/div/div[3]/div/div/div[1]/div[1]"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    def get_choice_company(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.choice_company)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user_name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login_button")
    def click_choice_company(self):
        self.get_choice_company().click()
        print("Click choice_company")


    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name('sample@sample.com')
        self.input_password('123654')
        self.click_login_button()
        self.click_choice_company()
        self.get_assert_word(self.get_main_word(), "Сводная информация")
        


