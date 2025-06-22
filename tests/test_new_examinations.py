from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from Pages.ecological_aspect import Ecological_aspect_page
from Pages.examinations import Examinations_page
from Pages.login_page import Login_page


def test_Examinations():
    #options.add_argument("--headless")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    ep = Examinations_page(driver)
    ep.add_new_examinations()
