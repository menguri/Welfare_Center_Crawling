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


# 전처리 날짜 확인 -----------------------------------------------------------------------------------------------------------------------------------------------------
import datetime
df_now = datetime.datetime.now()


# center file 전처리 -----------------------------------------------------------------------------------------------------------------------------------------------------
center_file_path = os.path.dirname(os.path.realpath(__file__)) + '/' + f"{df_now.month}월{df_now.day}일_센터 현황.xlsx"
print(center_file_path)


# 상주 인구현황 file 전처리 -----------------------------------------------------------------------------------------------------------------------------------------------------
human_file_path = os.path.dirname(os.path.realpath(__file__)) + '/' + f"{df_now.month-1}월_상주인구현황.xlsx"
print(human_file_path)