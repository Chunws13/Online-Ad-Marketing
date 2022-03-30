from selenium import webdriver
import time
import datetime

class Daily_Report():
    def __init__(self, nosp_list):
        self.nosp_list = nosp_list

    def Daily(self):

        driver = webdriver.Chrome("크롬 드라이버 파일 경로")
        # 어제 기준: SNC 만 사용
        yesterday = str(datetime.date.today() - datetime.timedelta(days=1)).replace('-', '')

        # 네이버 리포트 다운
        naver_list = ['계정 별 다운로드 URL 입력']

        driver.get('https://searchad.naver.com/')
        driver.implicitly_wait(3)

        driver.find_element_by_xpath('//*[@id="uid"]').send_keys('접속 아이디 입력')
        driver.find_element_by_xpath('//*[@id="upw"]').send_keys('비밀번호 입력')
        driver.find_element_by_xpath('//*[@id="container"]/main/div/div[1]/home-login/div/fieldset/span/button').click()
        driver.implicitly_wait(3)

        for list in naver_list:
            driver.get(list)
            driver.implicitly_wait(5)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a').send_keys('\n')
            time.sleep(2)

        # 다음 리포트 다운
        driver.get('https://clixagency.biz.daum.net/')
        driver.implicitly_wait(3)

        driver.find_element_by_xpath('//*[@id="userId"]').send_keys('아이디 입력')
        driver.find_element_by_xpath('//*[@id="userPw"]').send_keys('비밀번호 입력')
        driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/button').click()
        driver.implicitly_wait(3)

        daum_list = ['계정 별 다운로드 URL 입력']

        for list in daum_list:
            driver.get(list)
            driver.implicitly_wait(3)
            driver.find_element_by_xpath('//*[@id="listTableBody"]/tr[1]/td[4]/div/div/a').click()
            time.sleep(2)

        # NOSP 리포트 다운
        driver.get('https://ndim.da.naver.com/sso/login')

        driver.find_element_by_xpath('//*[@id="userId"]').send_keys('아이디 입력')
        driver.find_element_by_xpath('//*[@id="userPw"]').send_keys('비밀번호 입력')
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

        nosp_list = ['다운로드 필요한 보고서 URL 리스트 입력']

        for list in nosp_list:
            driver.get(list)
            driver.implicitly_wait(3)
            time.sleep(2)
            btn = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div/ul/li[3]/a')
            driver.execute_script('arguments[0].click();', btn)
            time.sleep(3)

        # SNC 리포트 다운
        driver.get('http://adcenter.sc.dreamad.co.kr/login')
        driver.implicitly_wait(3)

        snc_id_list = ['계정 목록 입력']
        snc_pw_list = ['계정 별 비밀번호 순차 입력']

        for list in range(len(snc_id_list)):
            driver.find_element_by_xpath('//*[@id="loginFrm"]/div[1]/input').send_keys(snc_id_list[list])
            driver.find_element_by_xpath('//*[@id="loginFrm"]/div[2]/input').send_keys(snc_pw_list[list])
            driver.find_element_by_xpath('//*[@id="loginFrm"]/button').click()
            driver.implicitly_wait(3)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="topMenu_adreport"]/a').click()
            driver.implicitly_wait(3)
            time.sleep(2)

            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div[3]/ul/li[3]/a').send_keys('\n')
            driver.implicitly_wait(3)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="searchStartDate"]').clear()
            driver.find_element_by_xpath('//*[@id="searchStartDate"]').send_keys(yesterday)

            driver.find_element_by_xpath('//*[@id="searchEndDate"]').clear()
            driver.find_element_by_xpath('//*[@id="searchEndDate"]').send_keys(yesterday)

            driver.find_element_by_xpath('//*[@id="report_call2"]').send_keys('\n')
            driver.find_element_by_xpath('//*[@id="reportByAllKeywordTable_wrapper"]/div[3]/a').click()

            time.sleep(3)

            driver.get('http://adcenter.sc.dreamad.co.kr/login')

        # Neo click 리포트 다운
        neo_id_list = ['계정 목록 입력']
        neo_pw_list = ['계정 별 비밀번호 순차 입력']

        for list in range(len(neo_id_list)):
            driver.get('http://www.neoclick.co.kr/')
            driver.implicitly_wait(3)

            log_in = driver.find_element_by_xpath('//*[@id="loginBtn"]')
            driver.execute_script('arguments[0].click();', log_in)

            driver.find_element_by_xpath('//*[@id="idForm_txt"]').send_keys(neo_id_list[list])
            driver.find_element_by_xpath('//*[@id="passForm_txt"]').send_keys(neo_pw_list[list])

            btn = driver.find_element_by_xpath('//*[@id="login"]/div[1]/img')
            driver.execute_script('arguments[0].click();', btn)

            driver.get('http://adcenter.neoclick.co.kr/admanager/adcenter_101.asp')
            driver.implicitly_wait(3)

            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/p/span[4]/a/img').click()
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/a[2]/div').click()
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/a[3]/div/span').click()
            time.sleep(2)

            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]').click()
            driver.find_element_by_xpath('//*[@id="dwn_img"]').click()

            driver.find_element_by_xpath('//*[@id="logout"]').click()

        # 네이트 리포트 다운
        driver.get('https://oasis.nate.com/')
        driver.implicitly_wait(3)

        driver.find_element_by_xpath('//*[@id="login_id"]').send_keys('아이디 입력')
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('비밀번호 입력')
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/form/fieldset/div[2]/input').click()

        driver.get('계정 리포트 URL 입력')
        driver.find_element_by_xpath(
            '//*[@id="contents"]/div/div[1]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[1]/a').click()
        time.sleep(3)

        driver.get('계정 리포트 URL 입력')
        driver.find_element_by_xpath(
            '//*[@id="contents"]/div/div[1]/table/tbody/tr[4]/td/table/tbody/tr/td[1]/a').click()
        time.sleep(3)

        driver.get('계정 리포트 URL 입력')
        driver.find_element_by_xpath(
            '//*[@id="contents"]/div/div[1]/table/tbody/tr[4]/td/table/tbody/tr/td[1]/a').click()
        time.sleep(3)

        driver.close()
