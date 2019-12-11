import requests
import re
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
url = "http://image.so.com"
# url = "https://p.ssl.qhimg.com/t019e98aea4fd1a3812.jpg"
r = requests.get(url,headers=headers)
# r = r.content
# with open("aa.jpg","wb") as f:
#     f.write(r)
oo = r.content.decode()

tu = re.findall("https:\/\/p\.ssl\.qhimg\.com\/[\w]{19}\.jpg",oo)
print(tu)
i = 0
for url1 in tu:
    l = requests.get(url1,headers=headers)
    bb = l.content
    # print(bb)
    i += 1
    with open(str(i)+".jpg","wb") as f:
        f.write(bb)
    print(i)

# <img src="https://p.ssl.qhimg.com/t016e4132d1112bee40.jpg">
# ret = re.match("[\w]{4,20}@163\.com", email)