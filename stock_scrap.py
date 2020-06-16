import requests
from bs4 import BeautifulSoup

# HTML 확보
res = requests.get('https://finance.naver.com/')

soup = BeautifulSoup(res.text, 'html.parser')
#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num
out_tag = soup.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')
print(out_tag.text)
print(float(out_tag.text.replace(',', '')))