from email import header
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# res = requests.get("http://naver.com")
# res = requests.get("https://github.com/flyhigh528")

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("응답코드 : ", res.status_code) # 200이면 정상
# res.raise_for_status()
# print("웹 스크래핑을 진행합니다.")    
# print(len(res.text))
# print(res.text)

with open("github.html", "w", encoding="utf8") as f:
    f.write(res.text)