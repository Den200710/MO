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
    first_field = "//input[@id='name']"
    second_field = "//input[@id='quantitative_value']"
    third_field = "//span[@id='unit-describe']"
    selection_third_field = "//span[@class='rs-picker-select-menu-item']"
    fourth_field = "//input[@id='lib_env_impact_factor_id']"
    selection_fourth_field = "//*[contains(text(),'Аварии и инциденты')]"

    # login_button = "//button[@type='submit']"

    # Getters

    def get_ecological_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ecological_button)))

    def get_add_ecological_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.add_ecological_button)))

    def get_first_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_word)))
    def get_first_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_field)))
    def get_second_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.second_word)))
    def get_second_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.second_field)))
    def get_third_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.third_word)))
    def get_third_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.third_field)))
    def get_selection_third_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.selection_third_field)))
    def get_fourth_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.fourth_word)))
    def get_fourth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.fourth_field)))
    def get_selection_fourth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.selection_fourth_field)))
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

    def input_first_field(self, first_field):
        self.get_first_field().send_keys(first_field)
        print("Input first_field")
    def input_second_field(self, second_field):
        self.get_second_field().send_keys(second_field)
        print("Input second_field")
    def click_third_field(self):
        self.get_third_field().click()
        print("Click third_field")
    def click_selection_third_field(self):
        self.get_selection_third_field().click()
        print("Click selection_third_field")

    def click_fourth_field(self):
        self.get_fourth_field().click()
        print("Click fourth_field")
    def click_selection_fourth_field(self):
        self.get_selection_fourth_field().click()
        print("Click selection_fourth_field")


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

        # Проверяем наличие псевдоэлемента ::after для каждого input
        assert self.check_after(
            self.get_first_word()), "Необязательное поле 1"
        assert self.check_after(
            self.get_second_word()), "Необязательное поле 2"
        assert self.check_after(
            self.get_third_word()), "Необязательное поле 3"
        assert self.check_after(
            self.get_fourth_word()), "Необязательное поле 4"
        assert self.check_after(
            self.get_fifth_word()), "Необязательное поле 5"
        assert self.check_after(
            self.get_sixth_word()), "Необязательное поле 6"
        assert self.check_after(
            self.get_seventh_word()), "Необязательное поле 7"
        assert self.check_after(
            self.get_eighth_word()), "Необязательное поле 8"
        assert self.check_after(
            self.get_ninth_word()), "Необязательное поле 9"
        assert self.check_after(
            self.get_tenth_word()), "Необязательное поле 10"

        #Заполняем поля
        self.input_first_field('Авто экологический аспект')
        self.input_second_field('Кол-ое значение')
        self.click_third_field()
        self.click_selection_third_field()
        self.click_fourth_field()
        self.click_selection_fourth_field()