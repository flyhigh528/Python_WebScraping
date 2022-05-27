from xml.dom.minidom import Attr
import requests
import re
from bs4 import BeautifulSoup

good_name = "기저귀"
minPrice =''
maxPrice =''
page = 6
is_rocket = "True"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q="+good_name+"&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice="+minPrice+"&maxPrice="+maxPrice+"&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(i)+"&rocketAll="+is_rocket+"&searchIndexingToken=1=5&backgroundColor="

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print(" 광고상품은 제외!!!!! " + ad_badge.get_text())
            continue

        name = item.find("div",  attrs={"class":"name"}).get_text() # 제품명
        # 맥북은 제외
        if "Apple" in name:
            print(" Apple 제품은 제외!!!!!")
            continue

        price_base = item.find("del",  attrs={"class":"base-price"}) # 할인전 가격
        if price_base:
            price_base = price_base.get_text()
        else:
            price_base = ""       
        price = item.find("strong",  attrs={"class":"price-value"}).get_text() # 가격

        rate = item.find("em",  attrs={"class":"rating"}) # 평점
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"    
            print(" 평점없는 상품 제외!!! ")
            continue
        
        if rate != "평점 없음":
            rate_cnt = item.find("span",  attrs={"class":"rating-total-count"}).get_text() # 평점 수
            rate_cnt = rate_cnt[1:-1]
        else:
            rate_cnt = "평점 수 없음"
            print(" 평점 수 없는 상품 제외!!! ")
            continue

        #  평점이 4.5이상 리뷰수가 100개 이상인 상품만 출력
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            goods_url = "https://coupang.com"+ item.a["href"]
            print(name, price_base, price, rate, rate_cnt)
            print("바로가기 : {}".format(goods_url))