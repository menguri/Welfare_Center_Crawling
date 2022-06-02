from msilib.schema import Class
import re
from selenium.webdriver.chrome.options import Options
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import datetime
import pandas as pd
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import os
import sys


# 크롤링 날짜 확인 -----------------------------------------------------------------------------------------------------------------------------------------------------
import datetime

df_now = datetime.datetime.now()


# 절대 경로 -----------------------------------------------------------------------------------------------------------------------------------------------------
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(relative_path)))
    return os.path.join(base_path, relative_path)

chrom_exe = resource_path('chromedriver.exe')


# 크롤링 Options  -----------------------------------------------------------------------------------------------------------------------------------------------------
# 갑자기 안될 때는 크롬 버전이 달라서 그런 것이므로, 그에 맞는 driver 다운로드하면 된다.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("start-maximized")
options.add_argument("--disable-software-rasterizer")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_experimental_option("prefs", {
    "download.default_directory": os.path.dirname(os.path.realpath(__file__)),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


# file rename 함수 ------------------------------------------------------------------------------------------------------------------------------------------

def file_rename(title):
    folder_path = os.path.dirname(os.path.realpath(__file__)) + '/'
    # each_file_path_and_gen_time: 각 file의 경로와, 생성 시간을 저장함
    each_file_path_and_gen_time = []
    for each_file_name in os.listdir(folder_path):
        # getctime: 입력받은 경로에 대한 생성 시간을 리턴
        each_file_path = folder_path + each_file_name
        each_file_gen_time = os.path.getctime(each_file_path)
        each_file_path_and_gen_time.append(
            (each_file_path, each_file_gen_time)
        )
    # 가장 생성시각이 큰(가장 최근인) 파일을 리턴 
    most_recent_file = max(each_file_path_and_gen_time, key=lambda x: x[1])[0]
    print(most_recent_file)
    file_oldname = os.path.join(folder_path, f"{most_recent_file}")
    file_newname_newfile = os.path.join(folder_path, f"{title}.xlsx")
    os.rename(file_oldname, file_newname_newfile)



# 센터 현황 file 크롤링 ------------------------------------------------------------------------------------------------------------------------------------------
def center_crawling(df_now):
    # global : chrome_exe, options
    url = 'https://www.longtermcare.or.kr/npbs/r/a/201/selectLtcoSrch.web?menuId=npe0000000650'
    driver = webdriver.Chrome(executable_path=chrom_exe, chrome_options=options)
    driver.get(url=url)
    # 첫 진입
    # 지역설정
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="si_do_cd-button"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/ul/li[16]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="si_gun_gu_cd-button"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/ul/li[10]'))).click()
    # 급여
    sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAdminKindCd-button"]'))).click()
    sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/ul/li[7]'))).click()
    sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAdminKindCd-button"]'))).click()
    sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/ul/li[4]'))).click()
    sleep(2)
    # 검색 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btn_search_pop"]'))).click()
    driver.switch_to.window(driver.window_handles[-1])
    # 두 번째 진입 / 파일 다운로드
    sleep(10)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/form/div/table/tbody/tr[1]/td/button[2]'))).click()
    sleep(3)
    file_rename(f"{df_now.month}월{df_now.day}일_센터 현황")
    print("센터현황 파일 크롤링이 종료되었습니다.")
    driver.quit()



# 상주 인구 현황 file 크롤링 ------------------------------------------------------------------------------------------------------------------------------------------
def sangju_human(df_now):
    # global : chrome_exe, options
    url = 'https://www.sangju.go.kr/board/list.tc?mn=2404&viewType=sub&mngNo=389&pageIndex=1&searchKeyword=&searchCondition=1&boardName=RKRWHD&boardNo=2000037233&groupNo=0&groupDepth=0&groupOrder=0&boardCategory=&searchAll=&inputPassYn=N&pageSeq=2564&preview=&previewTempl='
    driver = webdriver.Chrome(executable_path=chrom_exe, chrome_options=options)
    driver.get(url=url)


    html = driver.page_source
    # pip install lxml
    soup = BeautifulSoup(html, 'html.parser')
    table_html = soup.find('table', {'class' : 'comp-tbl_boardtype'})
    table_html = str(table_html)
    table_df_list = pd.read_html(table_html)
    table_df = table_df_list[0]
    title = table_df['제목'][0]
    month = list(title.split(' '))[1]

    if df_now.month-1 == 5:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[2]/div/table/tbody/tr[1]/td[6]/a'))).click()
        sleep(5)
        file_rename(f"{df_now.month-1}월_상주인구현황")
    else:
        print("최근 달의 근황이 존재하지 않습니다.")
    sleep(5)
    print("인구현황 파일 크롤링이 종료되었습니다.")
    driver.quit()



center_crawling(df_now)
sangju_human(df_now)