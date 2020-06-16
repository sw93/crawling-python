import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

response = requests.get('https://www.coupang.com/np/campaigns/82/components/194176?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=Y&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=194176&rating=0', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

product_list = soup.select_one('#productList')
product_li_list = product_list.find_all('li')

product_lists = []

for li in product_li_list:
    product_lists.append([
    li.select_one('a > dl > dd > div.name').text.strip(),
    li.select_one('a > dl > dd > div.price-area > div > div.price > em > strong')
        .text.strip().replace(',', ''),
    li.select_one('a > dl > dd > div.other-info > div > span.rating-total-count')
        .text.strip()[1:-1]
    ])

#pprint.pprint(product_lists)

# csv, excel로 저장
df = pd.DataFrame(product_lists, columns=['상품명', '가격', '상품평 수'])
df.to_csv('coupang.csv')
df.to_excel('coupang_export.xlsx', encoding='utf-8')
print('save complete')
