# urlretrieve

import urllib.request as req

# 좋아하는 사진 저장하기 / python.org 사이트 저장

img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA2MTJfMTQ0%2FMDAxNTkxOTYxMTk1Mzc4.3IFL8HvprdRVpjIeuO_xOchzhFXVO0nnHP-zIzhAVFog.R6CxG42nBtAUr51gqEAP-N0E2jwaLtHnQi61w1mFUfsg.JPEG.luvly_avely%2FIMG_8878.jpg&type=a340"
site_url = "https://www.python.org"

save_img = "c:\\users\\user\\Desktop\\background.jpg"
save_site = "c:\\users\\user\\Desktop\\python.html"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
    file2, header2 = req.urlretrieve(site_url, save_site)
except Exception as e:
    print(e)
else:
    print(header1)
    print("-" * 50)
    print(header2)
    print()

    print("Filename : {}".format(file1))
    print("Filename : {}".format(file2))
