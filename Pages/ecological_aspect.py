from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base
from Pages.left_sidebar import LeftSidebar


class Ecological_aspect_page(Base, LeftSidebar):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    ecological_button = "//*[contains(text(),'Экологические аспекты')]"
    add_ecological_button = "//span[@class='ui-smart-list-header-action_text__BArQV']"
    first_word = "//label[@id='name-label']"
    second_word = "//label[@id='quantitative_value-label']"
    third_word = "//label[@id='unit-label']"
    fourth_word = "//label[@id='lib_env_impact_factor_id-label']"
    fifth_word = "//label[@id='scale-label']"
    sixth_word = "//label[@id='adjustability-label']"
    seventh_word = "//label[@id='cost-label']"
    eighth_word = "//label[@id='urgency-label']"
    ninth_word = "//label[@id='libTechProcesses-label']"
    tenth_word = "//label[@id='libPossibleImpacts-label']"

    # login_button = "//button[@type='submit']"

    # Getters

    def get_ecological_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ecological_button)))

    def get_add_ecological_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.add_ecological_button)))

    def get_first_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_word)))

    def get_second_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.second_word)))

    def get_third_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.third_word)))

    def get_fourth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.fourth_word)))

    def get_fifth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.fifth_word)))

    def get_sixth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.sixth_word)))

    def get_seventh_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.seventh_word)))

    def get_eighth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.eighth_word)))

    def get_ninth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ninth_word)))

    def get_tenth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.tenth_word)))

    #def get_login_button(self):
    #    return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    # Actions

    def click_ecological_button(self):
        self.get_ecological_button().click()
        print("Click ecological_button")

    def click_add_ecological_button(self):
        self.get_add_ecological_button().click()
        print("Click add_ecological_button")


    # Methods
    def add_new_ecological_aspect(self):
        self.scroll_ecological_aspect()
        self.click_ecological_button()
        self.click_add_ecological_button()
        self.get_assert_word(self.get_first_word(), "Наименование")
        self.get_assert_word(self.get_second_word(), "Количественное значение, характеризующее экологический аспект")
        self.get_assert_word(self.get_third_word(), "Единица измерения количественного значения аспекта")
        self.get_assert_word(self.get_fourth_word(), "Фактор воздействия на ОС")
        self.get_assert_word(self.get_fifth_word(), "Масштабность")
        self.get_assert_word(self.get_sixth_word(), "Регулируемость")
        self.get_assert_word(self.get_seventh_word(), "Затратность")
        self.get_assert_word(self.get_eighth_word(), "Срочность")
        self.get_assert_word(self.get_ninth_word(), "Основные источники образования, вкладывающие более 80% в величину количественного значения аспекта (наименование и № цеха; наименование технологического процесса, установки)")
        self.get_assert_word(self.get_tenth_word(), "Фактическое и потенциально возможное воздействие на ОС")

        # Проверяем наличие псевдоэлемента ::after для каждого слова
        assert self.check_after_pseudo_element(
            self.get_first_word()), "Псевдоэлемент ::after отсутствует для первого слова"
        assert self.check_after_pseudo_element(
            self.get_second_word()), "Псевдоэлемент ::after отсутствует для второго слова"
        assert self.check_after_pseudo_element(
            self.get_third_word()), "Псевдоэлемент ::after отсутствует для третьего слова"
        assert self.check_after_pseudo_element(
            self.get_fourth_word()), "Псевдоэлемент ::after отсутствует для четвертого слова"
        assert self.check_after_pseudo_element(
            self.get_fifth_word()), "Псевдоэлемент ::after отсутствует для пятого слова"
        assert self.check_after_pseudo_element(
            self.get_sixth_word()), "Псевдоэлемент ::after отсутствует для шестого слова"
        assert self.check_after_pseudo_element(
            self.get_seventh_word()), "Псевдоэлемент ::after отсутствует для седьмого слова"
        assert self.check_after_pseudo_element(
            self.get_eighth_word()), "Псевдоэлемент ::after отсутствует для восьмого слова"
        assert self.check_after_pseudo_element(
            self.get_ninth_word()), "Псевдоэлемент ::after отсутствует для девятого слова"
        assert self.check_after_pseudo_element(
            self.get_tenth_word()), "Псевдоэлемент ::after отсутствует для десятого слова"



