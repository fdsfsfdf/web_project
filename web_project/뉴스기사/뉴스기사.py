from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd    
import os
import math
import urllib.request
import urllib
import win32com.client as win32   #pywin32 , pypiwin32 설치후 동작
import win32api  #파이썬 프롬프트를 관리자 권한으로 실행해야 에러없음
import cx_Oracle
import numpy
import requests
# import pymysql

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"html.parser")
    return soup

def naverPolitics_news(i):
    url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day"
    soup=create_soup(url)
    updatedNews = soup.find("li","num1").find('div','thumb').find('a')
    # print(updatedNews)
    title = updatedNews['title']
    print(title)
    link = "https://news.naver.com" + updatedNews["href"]
    print(link)
    img = updatedNews.find("img")['src']
    print(img)
    

naverPolitics_news(1)


# conn=pymysql.connect(host='localhost',user='13',password='dw314129')
# curs=conn.cursor()
# sql = " SELECT * FROM "
