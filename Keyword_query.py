import time, os
import requests
import pandas

import signaturehelper

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}

BASE_URL = 'https://api.naver.com'
API_KEY = ''
SECRET_KEY = ''
CUSTOMER_ID = ''

list = pandas.read_excel("./검색량측정_리스트.xlsx")
keyword, PC_Query, MO_Query, PC_Click, MO_Click = [], [], [], [], []

uri = '/keywordstool'
method = 'GET'

count = 0
total_len = len(list)

for k in range(len(list)) :
    r = requests.get(BASE_URL + uri, params={'hintKeywords':list.iloc[k, 0], 'showDetail': 1}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
    result = r.json()
    # print(result['keywordList'][0])

    keyword.append(result['keywordList'][0]['relKeyword'])
    target_list = [ 'monthlyPcQcCnt', ]
    try:
        PC_Query.append(result['keywordList'][0]['monthlyPcQcCnt'])
    
    except:
        PC_Query.append(0)
    
    try:
        PC_Click.append(result['keywordList'][0]['monthlyAvePcClkCnt'])

    except:
        PC_Click.append(0)

    try:
        MO_Query.append(result['keywordList'][0]['monthlyMobileQcCnt'])
    except:
        MO_Query.append(0)
    
    try:
        MO_Click.append(result['keywordList'][0]['monthlyAveMobileClkCnt'])

    except:
        MO_Click.append(0)
        
    time.sleep(0.3)
    count += 1
    print(">>>", count, "/", total_len, "진행 중", ":", result['keywordList'][0]['relKeyword'])
dic = {'키워드':keyword, 'PC 검색량':PC_Query, '월간 평균 PC 클릭수':PC_Click, "MO 검색량" : MO_Query, "월간 평균 MO 클릭수" : MO_Click}
data = pandas.DataFrame(dic)

data.to_excel('월간쿼리.xlsx', index=False)
print('완료')
