import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_class import Base
from Pages.left_sidebar import LeftSidebar


class Ecological_aspect_page(Base, LeftSidebar):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Variable
    var1_field = 'Авто экологический аспект'
    var2_field = 'Кол-ое значение'
    var5_field = '30'
    var6_field = '40'
    var7_field = '50'
    var8_field = '60'
    var11_field = (int(var5_field) + int(var6_field) + int(var7_field) + int(var8_field)) // 4
    var11_str = f"{str(var11_field)} Б"


    # Locators
    """Локаторы кнопок"""
    ecological_button = "//*[contains(text(),'Экологические аспекты')]"
    add_ecological_button = "//span[@class='ui-smart-list-header-action_text__BArQV']"
    """Локаторы наименований"""
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
    """Локаторы полей"""
    first_field = "//input[@id='name']"
    second_field = "//input[@id='quantitative_value']"
    third_field = "//div[@id='unit']"
    selection_third_field = "//span[@class='rs-picker-select-menu-item']"
    fourth_field = "//input[@id='lib_env_impact_factor_id']"
    selection_fourth_field = "//*[contains(text(),'Аварии и инциденты')]"
    fifth_field = "//input[@id='scale']"
    sixth_field = "//input[@id='adjustability']"
    seventh_field = "//input[@id='cost']"
    eighth_field = "//input[@id='urgency']"
    ninth_field = "//*[@id='__next']/div[1]/div[3]/div/div[3]/form/div[1]/div[2]/div[1]/div/div/div[1]/div/div"
    selection_ninth_field = "/html/body/div[4]/div/div/div/div[2]/div/div[3]/div[2]/table/tbody/tr/td[1]"
    close_right_window = "/html/body/div[4]"
    tenth_field = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[2]/div[2]/div/div/div[1]/div/div"
    selection_tenth_field = "//td[@class='ui-table_cell__cnEqM ui-table_hide_mobile__4lT7x']"

    save_button = "//button[@type='submit']"

    """Локаторы страницы Описание"""
    field_first = "//*[@id='__next']/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]"
    field_second = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]"
    field_third = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]"
    field_fourth = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div[2]"
    field_fifth = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]"
    field_sixth = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[5]/div[2]"
    field_seventh = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[6]/div[2]"
    field_eighth = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[7]/div[2]"
    field_ninth = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div"
    field_tenth = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div"
    field_eleven = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div[2]/div/div[8]/div[2]"
    open_block = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/div/div[2]"
    open_block_fact = "//*[@id='__next']/div[1]/div[3]/div/div[3]/div/div[2]/div[3]/div[1]/div[2]"



    # Getters

    def get_ecological_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ecological_button)))

    def get_save_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.save_button)))
    def get_add_ecological_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.add_ecological_button)))
    """Геттеры наименований"""
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

    """Геттеры полей"""
    def get_first_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_field)))
    def get_second_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.second_field)))
    def get_third_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.third_field)))
    def get_selection_third_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.selection_third_field)))
    def get_fourth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.fourth_field)))
    def get_selection_fourth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.selection_fourth_field)))
    def get_fifth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.fifth_field)))
    def get_sixth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.sixth_field)))
    def get_seventh_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.seventh_field)))
    def get_eighth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.eighth_field)))
    def get_ninth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.ninth_field)))
    def get_selection_ninth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.selection_ninth_field)))
    def get_close_right_window(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.close_right_window)))
    def get_tenth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.tenth_field)))
    def get_selection_tenth_field(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.selection_tenth_field)))

    """Геттеры полей Описание"""
    def get_field_first(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_first)))
    def get_field_second(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_second)))
    def get_field_third(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_third)))
    def get_field_fourth(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_fourth)))
    def get_field_fifth(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_fifth)))
    def get_field_sixth(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_sixth)))
    def get_field_seventh(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_seventh)))
    def get_field_eighth(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_eighth)))
    def get_field_ninth(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_ninth)))
    def get_field_tenth(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_tenth)))
    def get_field_eleven(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_eleven)))
    def get_open_block(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.open_block)))
    def get_open_block_fact(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.open_block_fact)))


    # Actions

    def click_ecological_button(self):
        self.get_ecological_button().click()
        print("Click ecological_button")

    def click_add_ecological_button(self):
        self.get_add_ecological_button().click()
        print("Click add_ecological_button")
    def click_save_button(self):
        self.get_save_button().click()
        print("Click save_button")

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
    def input_fifth_field(self, fifth_field):
        self.get_fifth_field().send_keys(fifth_field)
        print("Input fifth_field")
    def input_sixth_field(self, sixth_field):
        self.get_sixth_field().send_keys(sixth_field)
        print("Input sixth_field")
    def input_seventh_field(self, seventh_field):
        self.get_seventh_field().send_keys(seventh_field)
        print("Input seventh_field")
    def input_eighth_field(self, eighth_field):
        self.get_eighth_field().send_keys(eighth_field)
        print("Input eighth_field")
    def click_ninth_field(self):
        self.get_ninth_field().click()
        print("Click ninth_field")
    def click_selection_ninth_field(self):
        self.get_selection_ninth_field().click()
        print("Click selection_ninth_field")

    def click_close_right_window(self):
        self.get_close_right_window().click()
        print("Click close_right_window")

    def click_tenth_field(self):
        self.get_tenth_field().click()
        print("Click tenth_field")
    def click_selection_tenth_field(self):
        self.get_selection_tenth_field().click()
        print("Click selection_tenth_field")
    def click_open_block(self):
        self.get_open_block().click()
        print("Click open_block")
    def click_open_block_fact(self):
        self.get_open_block_fact().click()
        print("Click open_block_fact")

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
        self.get_assert_word(self.get_ninth_word(), "Основные источники образования, вкладывающие более 30% в величину количественного значения аспекта (наименование и № цеха; наименование технологического процесса, установки)")
        self.get_assert_word(self.get_tenth_word(), "Фактическое и потенциально возможное воздействие на ОС")

        # Проверяем наличие псевдоэлемента ::after для каждого input
        assert self.check_after(self.get_first_word())
        assert self.check_after(self.get_second_word())
        assert self.check_after(self.get_third_word())
        assert self.check_after(self.get_fourth_word())
        assert self.check_after(self.get_fifth_word())
        assert self.check_after(self.get_sixth_word())
        assert self.check_after(self.get_seventh_word())
        assert self.check_after(self.get_eighth_word())
        assert self.check_after(self.get_ninth_word())
        assert self.check_after(self.get_tenth_word())

        #Заполняем поля
        self.input_first_field(self.var1_field)
        self.input_second_field(self.var2_field)
        self.click_third_field()
        self.click_selection_third_field()
        self.click_fourth_field()
        self.click_selection_fourth_field()
        self.click_ninth_field()
        self.click_selection_ninth_field()
        self.click_close_right_window()
        self.click_tenth_field()
        time.sleep(1)
        self.click_selection_tenth_field()
        time.sleep(1)
        self.click_close_right_window()

        self.get_field_value((By.XPATH, self.third_field), 'var3_field')
        self.get_field_value((By.XPATH, self.ninth_field), 'var9_field')
        self.get_field_value((By.XPATH, self.tenth_field), 'var10_field')


        self.driver.execute_script("window.scrollBy(0, 800)")
        time.sleep(1)
        self.input_fifth_field(self.var5_field)
        time.sleep(1)
        self.input_sixth_field(self.var6_field)
        time.sleep(1)
        self.input_seventh_field(self.var7_field)
        time.sleep(1)
        self.input_eighth_field(self.var8_field)


        """Сохраняем значения полей, вызывая один метод с различными локаторами"""

        self.get_field_value((By.XPATH, self.fourth_field), 'var4_field')
        self.click_save_button()
        time.sleep(2)
        self.get_assert_word(self.get_field_first(), self.var1_field)
        self.get_assert_word(self.get_field_second(), self.var2_field)
        self.get_assert_word(self.get_field_third(), self.var3_field)
        self.get_assert_word(self.get_field_fourth(), self.var4_field)
        self.get_assert_word(self.get_field_fifth(), self.var5_field)
        self.get_assert_word(self.get_field_sixth(), self.var6_field)
        self.get_assert_word(self.get_field_seventh(), self.var7_field)
        self.get_assert_word(self.get_field_eighth(), self.var8_field)
        self.click_open_block()
        self.get_assert_word(self.get_field_ninth(), self.var9_field)
        self.click_open_block_fact()
        self.get_assert_word(self.get_field_tenth(), self.var10_field)
        self.get_assert_word(self.get_field_eleven(), self.var11_str)





