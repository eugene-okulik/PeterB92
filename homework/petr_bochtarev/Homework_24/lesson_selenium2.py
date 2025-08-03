from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_1(driver):
    driver.get('http://testshop.qa-practice.com/')
    product = driver.find_element(By.XPATH, "//a[text()='Customizable Desk']")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    tab = driver.window_handles
    driver.switch_to.window(tab[1])
    driver.find_element(By.ID, 'add_to_cart').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Continue Shopping']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//sup[@class='my_cart_quantity badge text-bg-primary "
                                                           "position-absolute top-0 end-0 mt-n1 me-n1 "
                                                           "rounded-pill']")))
    driver.close()
    driver.switch_to.window(tab[0])
    product = driver.find_element(By.XPATH, "//a[text()='Customizable Desk']").text
    driver.find_element(By.XPATH, "(//a[@href='/shop/cart'])[1]").click()
    assert product in driver.find_element(By.XPATH, "//h6[text()='Customizable Desk (Steel, White)']").text


def test_2(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    bag = driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    add_to_compare = driver.find_element(By.XPATH, "(//a[@title='Add to Compare'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(bag).click(add_to_compare).perform()
    bag = driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    wait = WebDriverWait(driver, 10)
    compare_products = wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@id="compare-items"]//a['
                                                                              '@class="product-item-link"]')))
    assert bag.get_attribute('alt') == compare_products.text
