import time
import random
import requests
import pandas

import signaturehelper

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}

BASE_URL = 'https://api.naver.com'
API_KEY = '******'
SECRET_KEY = '******'
CUSTOMER_ID = '******'

list = pandas.read_excel("./검색량측정_리스트.xlsx")
product = []
keyword = []
query = []
click = []

uri = '/keywordstool'
method = 'GET'

for k in range(len(list)) :
    r = requests.get(BASE_URL + uri, params={'hintKeywords':list.iloc[k, 1], 'showDetail': 1}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
    result = r.json()
    print(result['keywordList'][0])

    product.append(list.iloc[k, 0])
    keyword.append(result['keywordList'][0]['relKeyword'])
    try:
        query.append(round(result['keywordList'][0]['monthlyPcQcCnt'] / 30 * 7, 0))
        click.append(result['keywordList'][0]['monthlyAvePcCtr'])
    except:
        query.append(0)
        click.append(0)

    time.sleep(1)

dic = {'상품':product, '키워드':keyword, '주간쿼리':query, '주간클릭':click}

data = pandas.DataFrame(dic)

data.to_excel('주간쿼리.xlsx', index=False)
print('완료')