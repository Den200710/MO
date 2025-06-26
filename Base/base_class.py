import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)


    close_right_window = ("xpath", "//button[contains(@class,'rs-drawer-header-close')]")

    def click_close_window(self):
        with allure.step("Close rigth window"):
            self.wait.until(EC.element_to_be_clickable(self.close_right_window)).click()

    def open(self):
        with allure.step(f"Open {self.PAGE_URL}page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):            # Проверяет, что открылась та страница, которую открывали
        with allure.step(f"Page {self.PAGE_URL}is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def get_current_title(self):
        get_title = self.driver.title
        print("Current title " + get_title)

    """Method assert_word"""

    def get_assert_word(self, word, result):
        valua_word = word.text
        print(f"Значение valua_word: '{valua_word}', Ожидаемое значение result: '{result}'")
        assert valua_word == result
        print('Good assert')

    def check_after(self, element):
        # Используем JavaScript для проверки наличия псевдоэлемента ::after
        script = """
        let computedStyle = window.getComputedStyle(arguments[0], '::after');
        return computedStyle.content !== 'none' && computedStyle.content !== '';
        """
        has_after = self.driver.execute_script(script, element)
        return has_after

    def check_not_required(self, element):
        # Используем JavaScript для проверки отсутствия псевдоэлемента ::after
        script = """
        let computedStyle = window.getComputedStyle(arguments[0], '::after');
        return computedStyle.content === 'none' || computedStyle.content === '';
        """
        is_not_required = self.driver.execute_script(script, element)
        return is_not_required

    """Method get word"""

    def get_field_value(self, locator, variable_name):
        """Получает значение поля по указанному локатору и сохраняет его в переменную."""
        try:
            field_element = self.driver.find_element(*locator)
            # Здесь предполагаем, что вы имеете в виду значение поля ввода
            value = field_element.get_attribute('value')  # Получаем значение поля ввода
            if value is None:  # Если значение пустое, возможно что-то другое.
                value = field_element.text  # Пытаемся получить текст элемента
            setattr(self, variable_name, value)  # Сохраняем полученное значение в переменную
            print(f"Сохраненное значение для {variable_name}: {value}")  # Выводим значение
        except Exception as e:
            print(f"Произошла ошибка: {e}")  # Обработка ошибок




