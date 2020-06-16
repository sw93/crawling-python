from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://login.coupang.com/login/login.pang')

driver.find_element_by_name('email').send_keys('loginId')
driver.find_element_by_name('password').send_keys('password')
login_button = driver.find_element_by_css_selector('body > div.member-wrapper.member-wrapper--flex > div > div > form > div.login__content.login__content--trigger > button')
login_button.click();
time.sleep(3)

driver.close()