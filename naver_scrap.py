import requests
from bs4 import BeautifulSoup

# HTML 확보
res = requests.get('https://www.naver.com/')
#print(res.text)

# HTML 파싱을 위한 bs4
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

# 데이터 추출
# themecast > div.theme_cont > div:nth-child(2) > div > ul > li:nth-child(2) > a.theme_info > strong
out_tag = soup.select_one('#themecast > div.theme_cont > div:nth-child(2) > div > ul > li:nth-child(2) > a.theme_info > strong')
print(out_tag)
print(out_tag.text)