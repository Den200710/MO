

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

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




