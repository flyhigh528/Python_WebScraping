import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=641253"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# title = webtoons[0].a.get_text()
# link = webtoons[0].a["href"]

# print(title)
# print("https://comic.naver.com" + link)

# 제목 + 링크 출력
# webtoons = soup.find_all("td", attrs={"class":"title"})
# for webtoon in webtoons:
#     title = webtoon.a.get_text()
#     link = "https://comic.naver.com" + webtoon.a["href"] 

#     print(title, link)

# 평점 출력
webtoons = soup.find_all("div", attrs={"class":"rating_type"})
for webtoon in webtoons:
    # star = webtoon.find("strong").get_text()
    star = webtoon.strong.get_text()

    print(star)
