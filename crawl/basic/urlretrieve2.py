# urlretrieve

import urllib.request as req

# 이미지, 문서 가져오기

# 가져올 url 지정
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEyMDRfMjk5%2FMDAxNjM4NjEyNjg0ODI5.ovPJmCIu0bTakGRHOaPjEnTGPSXPn8v4PQoggWZEXnAg.iXFf5NlZrgJ59ASqcyh1B9vq30WUCEzzUPMs1f3hwo0g.JPEG.skehop%2FKakaoTalk_20211118_131904323_13.jpg&type=a340"
doc_url = "https://www.naver.com"

# 저장할 파일명 지정
save_img = "c:\\users\\user\\Desktop\\dog.png"
save_doc = "c:\\users\\user\\Desktop\\naver.html"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
    file2, header2 = req.urlretrieve(doc_url, save_doc)
except Exception as e:
    print(e)
else:
    print(header1)
    print("-" * 50)
    print(header2)
    print()

    print("Filename : {}".format(file1))
    print("Filename : {}".format(file2))
