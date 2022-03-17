import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
webtoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 "a" element 를 반환
for webtoon in webtoons:
    print(webtoon.get_text())