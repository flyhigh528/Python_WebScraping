from xml.dom.minidom import Attr
import requests
import re
from bs4 import BeautifulSoup

good_name = "노트북"
minPrice =''
maxPrice =''
page = "1"
is_rocket = "True"

# url = "https://www.coupang.com/np/search?q="+good_name+"&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice="+minPrice+"&maxPrice="+maxPrice+"&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+page+"&rocketAll="+is_rocket+"&searchIndexingToken=1=5&backgroundColor="
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print(res.text)
# items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
# for item in items:
#     ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
#     if ad_badge:
#         print(" 광고상품은 제외!!!!! " + ad_badge.get_text())
#         continue

#     name = item.find("div",  attrs={"class":"name"}).get_text() # 제품명
#     # 맥북은 제외
#     if "Apple" in name:
#         print(" Apple 제품은 제외!!!!!")
#         continue

#     price_base = item.find("del",  attrs={"class":"base-price"}) # 할인전 가격
#     if price_base:
#         price_base = price_base.get_text()
#     else:
#         price_base = ""       
#     price = item.find("strong",  attrs={"class":"price-value"}).get_text() # 가격

#     rate = item.find("em",  attrs={"class":"rating"}) # 평점
#     if rate:
#         rate = rate.get_text()
#     else:
#         rate = "평점 없음"    
#         print(" 평점없는 상품 제외!!! ")
#         continue
    
#     if rate != "평점 없음":
#         rate_cnt = item.find("span",  attrs={"class":"rating-total-count"}).get_text() # 평점 수
#         rate_cnt = rate_cnt[1:-1]
#     else:
#         rate_cnt = "평점 수 없음"
#         print(" 평점 수 없는 상품 제외!!! ")
#         continue

#     #  평점이 4.5이상 리뷰수가 100개 이상인 상품만 출력
#     if float(rate) >= 4.5 and int(rate_cnt) >= 100:
#         goods_url = "https://coupang.com"+ item.a["href"]
#         print(name, price_base, price, rate, rate_cnt, "\n"+ goods_url)