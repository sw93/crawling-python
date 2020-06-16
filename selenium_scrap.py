# pip install selenium

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
# move page
driver.get('https://www.coupang.com/np/campaigns/82/components/194176?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1')
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()

time.sleep(5)

