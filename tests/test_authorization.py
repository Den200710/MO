from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.login_page import Login_page



def test_authorization_login():
    options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test")

    login = Login_page(driver)
    login.authorization()


