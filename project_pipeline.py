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
from file_crawling import center_crawling, sangju_human
from file_processing import centerfile_processing, humanfile_processing
import datetime
df_now = datetime.datetime.now()
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')

# 작업 디렉토리 문제
import os
import sys
if getattr(sys, 'frozen', False):
    #test.exe로 실행한 경우,test.exe를 보관한 디렉토리의 full path를 취득
    program_directory = os.path.dirname(os.path.abspath(sys.executable))
else:
    #python test.py로 실행한 경우,test.py를 보관한 디렉토리의 full path를 취득
    program_directory = os.path.dirname(os.path.abspath(__file__))
#현재 작업 디렉토리를 변경
os.chdir(program_directory)

print(program_directory)

# 크롤링 Options  -----------------------------------------------------------------------------------------------------------------------------------------------------
# 갑자기 안될 때는 크롬 버전이 달라서 그런 것이므로, 그에 맞는 driver 다운로드하면 된다.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("start-maximized")
options.add_argument("--disable-software-rasterizer")
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})



# pipeline 운영시작 -----------------------------------------------------------------------------------------------------------------------------------------------------


center_crawling(program_directory)
print('센터현황 크롤링이 완료되었습니다.')
centerfile_processing(program_directory)
print('센터현황 전처리가 완료되었습니다.')
sangju_human(program_directory)
print('상주인구현황 크롤링이 완료되었습니다.')
try:
    humanfile_processing(program_directory)
    print('상주인구현황 전처리가 완료되었습니다.')
except:
    print('인구현황 전처리가 되지 않았습니다.')


# gmail로 보내기 -----------------------------------------------------------------------------------------------------------------------------------------------------
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl

