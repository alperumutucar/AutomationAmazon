from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')

if False:
    driver.get('http://www.amazon.com/')

    #driver2 = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')
    #driver2.get('https://www.gmail.com')

    #gm1 = driver2.find_element_by_css_selector('#identifierId')
    #gm1.send_keys("seleniumtestdeneme@gmail.com")
    #gm1.send_keys(Keys.RETURN)

    #gm2 = driver2.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    #gm2.send_keys("")
    #gm2.send_keys(Keys.RETURN)

    if False:
        ab1 = driver.find_element_by_css_selector("#nav-link-accountList > span.nav-line-2")
        ab1.click()

        ab2 = driver.find_element_by_css_selector("#ap_email")
        ab2.send_keys("alper.ucar@useinsider.com")
        ab2.send_keys(Keys.RETURN)

        ab3 = driver.find_element_by_css_selector("#ap_password")
        ab3.send_keys("")
        ab3.send_keys(Keys.RETURN)

        print('--------------')
        ab4 = driver.find_element_by_css_selector('#twotabsearchtextbox')
        ab4.send_keys('Samsung')
        ab4.send_keys(Keys.RETURN)

        ab5 = driver.find_element_by_css_selector('#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(10) > div > div > span > div > div > ul > li:nth-child(3)')
    #ab5 = driver.find_element_by_css_selector('#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(27) > span > div > div > ul > li.a-last')
    ab5.click()

    ab6 = driver.find_element_by_css_selector('#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div > span > div > div > div:nth-child(2) > div.sg-col-4-of-24.sg-col-4-of-12.sg-col-4-of-36.sg-col-4-of-28.sg-col-4-of-16.sg-col.sg-col-4-of-20.sg-col-4-of-32 > div > div > span > a > div')
    ab6.click()

    ab7 = driver.find_element_by_css_selector('#wishListMainButton > span')
    ab7.click()

print('the previous part was for Amazon')
driver.get('http://www.n11.com/')

element = WebDriverWait(driver, 10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#userKvkkModal > div > div.btnHolder > span'))).click()

assert "n11" in driver.title
#n1 = driver.find_element_by_css_selector('#userKvkkModal > div > div.btnHolder > span')
#n1.click()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#header > div > h1 > a > img'))).click()

#n3 = driver.find_element_by_css_selector('#header > div > h1 > a > img')
#n3.click()
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.menuTitle.nobg'))).click()

#n2 = driver.find_element_by_class_name('btnSignIn')
#n2.click()

#email
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#email'))).send_keys("alper.ucar@useinsider.com")





time.sleep(20) #BU ZAMAN ARALIĞI ELLE GİRİŞ YAPMAK İÇİN AYRILMIŞTIR





#time.sleep(10)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginButton'))).click()

print('burada')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#searchData'))).send_keys("Samsung")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.searchBtn'))).click()


#we need to scroll to the bottom of the page here
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

print('burada2')


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#contentListing > div > div > div.productArea > div.pagination > a:nth-child(2)'))).click()
print('burada3')


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#p-417971638 > div.pro > a > img'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.addWishListBtn.b-dt-wishlist'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#addToFavouriteWishListBtn'))).click()

#time.sleep(2)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.menuTitle'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#myAccount > div.accMenu > div.accMenu-cover > div.accNav > ul > li:nth-child(5) > a'))).click()

assert "Favorilerim (1)" in driver.find_element_by_css_selector('#myAccount > div.accContent > ul > li.wishGroupListItem.favorites > div > a > h4').text

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#myAccount > div.accContent > ul > li.wishGroupListItem.favorites > div > a > h4'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#p-417971638 > div.wishProBtns > span'))).click()

time.sleep(2)
assert "Ürününüz listeden silindi." in driver.find_element_by_css_selector('body > div.lightBox > div > span.message').text #this works correctly.

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btnBlack.confirm'))).click()

