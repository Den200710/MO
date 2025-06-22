from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from Pages.ecological_aspect import Ecological_aspect_page
from Pages.login_page import Login_page


def test_Ecological_aspect():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    eap = Ecological_aspect_page(driver)
    eap.add_new_ecological_aspect()
