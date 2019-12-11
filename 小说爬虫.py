import requests
import re
from lxml import etree
url = "http://www.555zw.com/book/39/39085/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
r = requests.get(url,headers=headers)
oo = r.content.decode('gbk')
# print(oo)
data = re.findall(r'<td class=\"ccss\"><a href="(.*?)" title=.*?<\/a></td>',oo)

da = data[:5]
print(da)
with open("С˵.tex","w") as f:
    for ur in da:
        urls = url + ur
        bu = requests.get(urls,headers=headers)
        r = bu.content.decode("gbk")
        b = etree.HTML(r)
        c = b.xpath("//div[text()]/text()")
        for i in c:
            # print(type(i))
            f.write(i)
