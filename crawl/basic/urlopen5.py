import urllib.request as req

news_url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=056&aid=0011186409"

try:
    request_url = req.Request(news_url)
    response = req.urlopen(request_url).read().decode("euc-kr")

except Exception as e:
    print(e)
else:
    print(request_url.header_items())
    print(response[:4000])
