from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def driver2():
    # Фикстура для работы со страницей без ожидания полной её загрузки
    options = Options()
    options.add_argument('start-maximized')
    options.page_load_strategy = 'eager'
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.quit()


def test_input_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    test_string = driver.find_element(By.XPATH, "//input[@placeholder='Submit me']")
    test_string.send_keys('test' + Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text').text
    print(result_text)


def test_student_registration_form(driver2):
    driver2.get('https://demoqa.com/automation-practice-form')
    driver2.find_element(By.ID, 'firstName').send_keys('Petr')
    driver2.find_element(By.ID, 'lastName').send_keys('Bochtarev')
    driver2.find_element(By.ID, 'userEmail').send_keys('test@mail.ru')
    driver2.find_element(By.XPATH, "(//label[@class='custom-control-label'])[1]").click()
    driver2.find_element(By.ID, 'userNumber').send_keys('8918111111')
    driver2.find_element(By.ID, 'dateOfBirthInput').click()
    month = driver2.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    dropdown_month = Select(month)
    dropdown_month.select_by_value('2')
    year = driver2.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    dropdown_year = Select(year)
    dropdown_year.select_by_value('1992')
    driver2.find_element(By.XPATH,
                         "//div[@class='react-datepicker__day react-datepicker__day--005']").click()
    driver2.find_element(By.ID, 'subjectsInput').send_keys('chemistry')
    driver2.find_element(By.XPATH, "//div[contains(@class, 'subjects-auto-complete__menu')]//*[text("
                                   ")='Chemistry']").click()
    driver2.find_element(By.XPATH, "(//label[@class='custom-control-label'])[4]").click()
    driver2.find_element(By.XPATH, "(//label[@class='custom-control-label'])[5]").click()
    driver2.find_element(By.XPATH, "(//label[@class='custom-control-label'])[6]").click()
    driver2.find_element(By.ID, 'currentAddress').send_keys('г. Краснодар')
    driver2.find_element(By.XPATH, "//div[text()='Select State']").click()
    driver2.find_element(By.XPATH, "//*[text()='Uttar Pradesh']").click()
    driver2.find_element(By.XPATH, "//div[text()='Select City']").click()
    driver2.find_element(By.XPATH, "//*[text()='Agra']").click()
    driver2.find_element(By.ID, 'submit').click()
    table = driver2.find_element(By.CLASS_NAME, 'table-responsive').text
    print(table)


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_language = driver.find_element(By.NAME, 'choose_language')
    dropdown = Select(choose_language)
    dropdown.select_by_visible_text('Python')
    select_text = dropdown.first_selected_option.text
    driver.find_element(By.ID, 'submit-id-submit').click()
    you_selected = driver.find_element(By.ID, 'result-text')
    assert you_selected.text == select_text


def test_start(driver):
    driver.get(' https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/*[text()='Hello World!']")))
    verification_text = 'Hello World!'
    assert element.text == verification_text
