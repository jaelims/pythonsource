import urllib.request as req
from fake_useragent import UserAgent

news_url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=056&aid=0011186409"
userAgent = UserAgent()
headers = {"user-agent": userAgent.random}

try:
    request_url = req.Request(news_url, headers=headers)
    response = req.urlopen(request_url).read().decode("euc-kr")

except Exception as e:
    print(e)
else:
    print(request_url.header_items())
    print(response[:4000])
