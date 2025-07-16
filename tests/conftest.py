import os
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)  # будет создавать экземпляр браузера для каждого теста отдельно
def driver(request):            # для создания объекта драйвера внутри тестов и pages
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Отключает детекцию автоматизации
    options.add_argument("--disable-infobars")  # Убирает сообщение "Chrome is being controlled..."
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Скрывает "Automation controlled"
    # options.add_experimental_option("useAutomationExtension", False)  # Отключает расширения автоматизации

    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    download_directory = os.path.join(parent_directory, 'Downloads')
    preference = {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False

    }
    options.add_experimental_option("prefs", preference)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield driver
    driver.quit()
