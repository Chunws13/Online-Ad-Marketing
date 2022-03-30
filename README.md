# Online-Ad-Marketing

검색량 측정기
1. Keyword_query.py [키워드 검색량 조회 프로그램]
2. signaturehelper.py [API 구동을 위한 네이버 측 제공 파일]

네이버 광고시스템 - 키워드도구에서 키워드 검색 시
검색 키워드 1개 + 연관 키워드 다수의 조합으로 결과 조회

검색량 원하는 키워드가 다수인 경우
검색을 여러번 해야하는 불편함이 있음

위의 불편함을 해소하기 위해 측정기 파일 내
검색을 원하는 키워드 작성 후 프로그램 실행 시
입력한 키워드에 해당하는 주간 검색량 측정 후 반환

단, 월간 키워드 검색량 10 이하시 0으로 반환

------

광고 리포트 자동 다운로드 프로그램
1. Auto_Report_Downloader.py

매일 광고 집행 중인 계정으로 접속하여 
개별적으로 리포트 다운로드 받아야 하나
다수 매체에서 광고 집행중이며
동일 매체 내 계정이 많은 관계로 
리포트 다운로드 시 상대적은로 많은 시간이 소요됨

자동 다운로드 프로그램 제작하여 리포트 작성에 소요되는 시간 절감
