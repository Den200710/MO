

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
        assert valua_word == result

    def check_after_pseudo_element(self, element):
        # Используем JavaScript для проверки наличия псевдоэлемента ::after
        script = """
        let computedStyle = window.getComputedStyle(arguments[0], '::after');
        return computedStyle.content !== 'none' && computedStyle.content !== '';
        """
        has_after = self.driver.execute_script(script, element)
        return has_after




