from flask import Flask, render_template
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
    link = "https://news.naver.com" + updatedNews["href"]
    img = updatedNews.find("img")['src']
    return title,link,img

app = Flask(__name__)

@app.route('/')
# @app.route('/index')

# print(naverPolitics_news(1))
def index():
    return render_template('index.html'
    ,naver_title1 = naverPolitics_news(1)[0],
    naver_src1 = naverPolitics_news(1)[1],
    naver_img1 = naverPolitics_news(1)[2]
    
    )

if __name__ == '__main__':
    app.run(debug=True)