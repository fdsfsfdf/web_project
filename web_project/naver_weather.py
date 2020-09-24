import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의 날씨]")
    baseUrl='https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='
    plusUrl=input("어느 지역의 날씨를 검색하고 싶으신가요.")
    url=baseUrl+plusUrl+'날씨'
    res=requests.get(url)
    res.raise_for_status()
    soup= BeautifulSoup(res.text,"html.parser")
    #흐림, 어제보다 00도 높아요
    cast = soup.find('p',attrs={"class":"cast_txt"}).get_text()
    #현재 00도 (최저 00/최고 00)
    curr_temp = soup.find("p", attrs={"class":"cast_txt"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    #오전 강수확률/오후 강수확률
    morning_rain_rate = soup.find("span",attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip()

    print(cast)
    print("현재 {} (최저{}/최고{})".format(curr_temp, min_temp, max_temp))
    print("오전{}/오후{}".format(morning_rain_rate, afternoon_rain_rate))


if __name__ == "__main__":
    scrape_weather()


