from datetime import datetime
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_class import Base
from Pages.left_sidebar import LeftSidebar

class Examinations_page(Base, LeftSidebar):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Variable
    basis_check_push = 'Основание для проверки'
    name_check_push = 'Внутренняя проверка авто'
    var5_field = '30'
    var6_field = '40'
    var7_field = '50'
    var8_field = '60'
    var11_field = (int(var5_field) + int(var6_field) + int(var7_field) + int(var8_field)) // 4
    var11_str = f"{str(var11_field)} Б"


    # Locators
    close = "//button[contains(@class,'rs-drawer-header-close')]"
    """Наименование страницы"""
    name_page = "//div[contains(@class,'view-header_title__272WQ')]"
    """Локаторы кнопок"""
    examinations_button = "//*[@id='__next']/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div[3]/a/div/div[3]"
    add_examination = "//a/button[1]"
    """Локаторы выбор компании"""
    select_company_button = "//*[@id='__next']/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div[2]/button/span[1]"
    select_main_company = "/html/body/div[4]/div/div/div/div[2]/div/div[3]/div[2]/table/tbody/tr[1]"
    close_select_company = "/html/body/div[4]/div/div/div/div[1]/button"
    check_main_company = "//*[@id='__next']/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/div/div[1]/div"
    field_company = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div[1]/label"
    """Локаторы вид проверки"""
    field_view_check = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[1]/label"
    select_view_check = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div[1]"
    view_check = "/html/body/div[3]/div/div[1]/span"

    """Локаторы причины проверки"""
    field_reason_check = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/label"
    reason_check = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/span"

    """Локаторы основания для проверки"""
    field_basis_check = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[3]/label"
    basis_check = "/html/body/div[1]/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[3]/div/input"

    """Локаторы Наименование проверки"""
    field_name_check = "//label[@id='name-label']"
    name_check = "//input[@aria-labelledby='name-label']"

    """Локаторы Выбор СП"""
    select_team = "(//span[@class='view-block_action_text__N6iUV'])[2]"
    first_team = "(//div[@class='team-node_root__AhXss'])[1]"
    close_select_team = "//button[contains(@class,'rs-drawer-header-close')]"
    field_select_team = "(//label[contains(@class,'required rs-form-control-label')])[7]"
    save_name_team = "//div[@class='formatters-common_content_text__KBBdb']"  #Локатор название выбранного СП

    """Локаторы Выбор месторождения"""
    field_object_territory = "(//label[contains(@class,'rs-form-control-label')])[12]"
    select_object_territory = "(//span[@class='view-block_action_text__N6iUV'])[3]"
    first_object_territory = "//td[@class='ui-table_cell__cnEqM ui-table_hide_mobile__4lT7x']/div[1]"
    save_name_object_territory = "formatters-common_content__clz41']"  #Локатор название выбранного месторождения

    """Локаторы Выбор члена комиссии"""
    field_commission = "(//label[contains(@class,'required rs-form-control-label')])[8]"
    field_employee_commission = "(//label[contains(@class,'required rs-form-control-label')])[9]"
    select_employee_commission = "(//input[contains(@id,'rs-«r7h4»')])"
    first_employee_commission = "(//div[@class='photo-formatter_photo__DWFcK'])[1]"
    """Локаторы Ответственное лицо"""
    field_responsible = "//label[@id='responsible_id-label']"
    select_responsible_employee = "//input[@id='responsible_id']"
    first_responsible_employee = "(//div[@class='photo-formatter_root__8jnAN'])[1]"

    """Локаторы дат"""
    field_date_begin = "//label[@id='start_date-label']"
    field_date_finish = "//label[@id='complete_before-label']"
    date_start = "//input[@id='start_date']"
    date_finish = "//input[@id='complete_before']"
    now = datetime.now()
    now_date = '2025.05.23'
    #now.strftime("%d.%m.%Y"))
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
    """Закрыть окно выбора"""
    def get_close(self):

        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.close)))

    """Наименование страницы"""
    def get_name_page(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.name_page)))

    """Геттеры кнопок создания"""
    def get_examinations_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.examinations_button)))
    def get_add_examination(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.add_examination)))

    """Геттеры выбор компании"""
    def get_select_company_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_company_button)))
    def get_select_main_company(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_main_company)))
    def get_close_select_company(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.close_select_company)))
    def get_check_main_company(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.check_main_company)))
    def get_field_company(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_company)))

    """Геттеры Вид проверки"""
    def get_field_view_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_view_check)))
    def get_select_view_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_view_check)))
    def get_view_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.view_check)))

    """Геттеры причины проверки"""
    def get_field_reason_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_reason_check)))
    def get_reason_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.reason_check)))

    """Геттеры основания для проверки"""
    def get_field_basis_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_basis_check)))
    def get_basis_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.basis_check)))

    """Геттеры наименования проверки"""
    def get_field_name_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_name_check)))
    def get_name_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.name_check)))

    """Геттеры Выбор СП"""
    def get_select_team(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_team)))
    def get_first_team(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_team)))
    def get_field_select_team(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_select_team)))
    def get_save_name_team(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.save_name_team)))

    """Геттеры Выбор месторождения"""
    def get_field_object_territory(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_object_territory)))
    def get_select_object_territory(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_object_territory)))
    def get_first_object_territory(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_object_territory)))

    """Геттеры Выбор члена комиссии"""
    def get_field_commission(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_commission)))
    def get_field_employee_commission(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.field_employee_commission)))
    def get_select_employee_commission(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_employee_commission)))
    def get_first_employee_commission(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.first_employee_commission)))

    """Геттеры Выбор ответственного за проверку"""
    def get_field_responsible(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_responsible)))
    def get_select_responsible_employee(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_responsible_employee)))
    def get_first_responsible_employee(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_responsible_employee)))

    """Геттеры Дат начала окончания"""
    def get_field_date_begin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_date_begin)))
    def get_field_date_finish(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_date_finish)))
    def get_date_start(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.date_start)))
    def get_date_finish(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.date_finish)))

    # Actions

    def click_close(self):
        self.get_close().click()
        print("Click close")

    def click_examinations_button(self):
        self.get_examinations_button().click()
        print("Click examinations_button")

    def click_add_examination(self):
        self.get_add_examination().click()
        print("Click add_examination")

    """Экшены выбор компании"""
    def click_select_company_button(self):
        self.get_select_company_button().click()
        print("Click select_company_button")

    def click_select_main_company(self):
        self.get_select_main_company().click()
        print("Click select_main_company")
    def click_close_select_company(self):
        self.get_close_select_company().click()
        print("Click close_select_company")

    """Экшены Вид проверки"""
    def click_select_view_check(self):
        self.get_select_view_check().click()
        print("Click select view check")
    def click_view_check(self):
        self.get_view_check().click()
        print("Click view check")

    """Экшены основания проверки"""
    def input_basis_check(self, basis_check):
        self.get_basis_check().send_keys(basis_check)
        print("Input basis_check")

    """Экшены основания проверки"""
    def input_name_check(self, name_check):
        self.get_name_check().send_keys(name_check)
        print("Input name_check")

    """Выбор СП"""
    def click_select_team(self):
        self.get_select_team().click()
        print("Click select_team")
    def click_first_team(self):
        self.get_first_team().click()
        print("Click first_team")

    """Выбор месторождения"""
    def click_select_object_territory(self):
        self.get_select_object_territory().click()
        print("Click select_object_territory")
    def click_first_object_territory(self):
        self.get_first_object_territory().click()
        print("Click first_object_territory")

    """Выбор члена комиссии"""
    def click_select_employee_commission(self):
        self.get_select_employee_commission().click()
        print("Click select_employee_commission")
    def click_first_employee_commission(self):
        self.get_first_employee_commission().click()
        print("Click first_employee_commission")

    """Выбор ответственного за проверку"""
    def click_select_responsible_employee(self):
        self.get_select_responsible_employee().click()
        print("Click select_responsible_employee")
    def click_first_responsible_employee(self):
        self.get_first_responsible_employee().click()
        print("Click first_responsible_employee")

    """Экшены Дат проверки"""
    def click_date_start(self):
        self.get_date_start().click()
        print("Input name_check")
    def input_date_start(self, date_start):
        self.get_date_start().send_keys(str(date_start))
        print("Input name_check")
    #def input_date_finish(self, date_now):
    #    self.get_date_finish().send_keys(str(date_now))
    #   print("Input name_check")

    # Methods
    def add_new_examinations(self):
        self.scroll_examinations()
        print('ok')
        self.click_examinations_button()
        print('ok2')
        time.sleep(1)
        self.click_add_examination()
        print('ok3')
        time.sleep(1)
        """Проверка страницы"""
        self.get_current_title()
        self.get_assert_word(self.get_name_page(), "Создание новой внутренней проверки")
        print('ok4')

        """Выбор компании"""
        self.click_select_company_button()
        print('ok5')
        self.click_select_main_company()
        self.click_close_select_company()
        print('ok6')

        """Проверка поля компания на обязательность. наименования поля и наименование выбранной компании"""
        self.get_assert_word(self.get_field_company(), 'ОРГАНИЗАЦИИ, УЧАСТВУЮЩИЕ В ПРОВЕРКЕ')
        print('ok7')
        assert self.check_after(self.get_field_company())
        print('ok8')
        self.get_field_value((By.XPATH, self.get_check_main_company()), 'var_main_company')
        print('ok9')

        """Выбор вида проверки, проверка на обязательность поля"""
        assert self.check_after(self.get_field_company())
        print('Вид проверки обязательное поле')
        self.click_select_view_check()
        self.click_view_check()

        """Причины проверки"""
        assert self.check_after(self.get_field_view_check())
        print('Причины проверки необязательное поле')
        self.get_assert_word(self.get_reason_check(), "Плановая")
        print('Причины проверки ок')

        """Основание проверки"""
        assert self.check_not_required(self.get_field_basis_check())
        print('Основание проверки необязательное поле')
        self.input_basis_check(self.basis_check_push)
        print('Основание проверки ок')

        """Наименование проверки"""
        assert self.check_after(self.get_field_name_check())
        print('Наименование проверки обязательное поле')
        self.input_name_check(self.name_check_push)
        print('Наименование проверки ок')

        """Выбор Месторождения"""
        assert self.check_not_required(self.get_field_object_territory())
        self.click_select_object_territory()
        self.click_first_object_territory()
        self.click_close()

        """Выбор СП"""
        assert self.check_after(self.get_field_select_team())
        self.click_select_team()
        self.click_first_team()
        self.click_close()

        """Выбор члена комиссии"""
        assert self.check_after(self.get_field_commission())
        assert self.check_after(self.get_field_employee_commission())
        self.click_select_employee_commission()
        self.click_first_employee_commission()

        self.driver.execute_script("window.scrollBy(0,500)")

        assert self.check_after(self.get_field_responsible())
        self.click_select_responsible_employee()
        self.click_first_responsible_employee()

        """Выбор дат начала - окончания проверки"""
        assert self.check_after(self.get_field_date_begin())
        assert self.check_after(self.get_field_date_finish())
        self.click_date_start()
        self.input_date_start(self.now_date)
        #self.input_date_finish(self.now_date)

        #self.get_assert_word(self.get_second_word(), "Количественное значение, характеризующее экологический аспект")
        #self.get_assert_word(self.get_third_word(), "Единица измерения количественного значения аспекта")
        #self.get_assert_word(self.get_fourth_word(), "Фактор воздействия на ОС")
        #self.get_assert_word(self.get_fifth_word(), "Масштабность")
        #self.get_assert_word(self.get_sixth_word(), "Регулируемость")
        #self.get_assert_word(self.get_seventh_word(), "Затратность")
        #self.get_assert_word(self.get_eighth_word(), "Срочность")
        #self.get_assert_word(self.get_ninth_word(), "Основные источники образования, вкладывающие более 30% в величину количественного значения аспекта (наименование и № цеха; наименование технологического процесса, установки)")
        #self.get_assert_word(self.get_tenth_word(), "Фактическое и потенциально возможное воздействие на ОС")

