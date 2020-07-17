from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_title(input):
    assert input in driver.title

def test_text(input, selector):
    assert input in driver.find_element_by_css_selector(selector).text


driver = webdriver.Firefox(executable_path='chromedriver_linux64/geckodriver')
driver.get('http://www.n11.com/')

element = WebDriverWait(driver, 10)
driver.maximize_window()

element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn'))).click()

test_title("Hayat Sana Gelir")
time.sleep(3)
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.menuTitle.nobg'))).click()
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btnLogin'))).click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

#email and password, please enter here
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email'))).send_keys('')
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pass'))).send_keys('')
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pass'))).send_keys(Keys.RETURN)

driver.switch_to.window(driver.window_handles[0])

time.sleep(10)
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchData'))).send_keys("Samsung")
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.searchBtn'))).click()

time.sleep(3)
element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.pagination a')))[1].click() #20
element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#view .column .plink')))[2].click()

time.sleep(5)
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#getWishList'))).click()
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#addToFavouriteWishListBtn'))).click()

element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.menuTitle'))).click()
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.accNav ul:nth-child(1) li:nth-child(5)'))).click()

test_text("Favorilerim (1)", '.listItemTitle')
element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.listItemWrap h4')))[0].click()
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.deleteProFromFavorites'))).click()

time.sleep(2)
test_text("Ürününüz listeden silindi.", 'span.message')
element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btnBlack.confirm'))).click()
