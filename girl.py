# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 22:47
# @Author  : Rhmpz
# @Site    : https://www.mn53.com/meihuoxiezhen/
# @File    : girl.py
# @Software: PyCharm
# @Describe:小姐姐网页爬取
import time
import requests
import re
url="https://www.mn53.com/meihuoxiezhen/"
res=requests.get(url)
pattern=re.compile('class="item-media entry".*?src="(.*?)"',re.S)
results=re.findall(pattern,res.text)

num=1
for img_url in results:
    time.sleep(0.5)
    response=requests.get("https:"+img_url)
    with open('img/%d.jpg'%num,'wb') as f:
        f.write(response.content)
    print("已经下载%d张："%num+"https:"+img_url)
    num=num+1

#todo
# urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None))