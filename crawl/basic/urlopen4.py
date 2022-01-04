# 다음 뉴스 가져오기
# https://news.v.daum.net/v/20211231101307520

import urllib.request as req

news_url = "https://news.v.daum.net/v/20211231101307520"

try:
    response = req.urlopen(news_url).read().decode("utf-8")
except Exception as e:
    print(e)
else:
    print(response[:4000])
