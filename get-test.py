#!python3
import requests as r
import sys
import re
import html
from codecs import encode, decode

urls = [
    "http://www.offcn.com/yinhang/shiti/2401/",
    "http://www.offcn.com/yinhang/shiti/2401/2.html",
    "http://www.offcn.com/yinhang/shiti/2401/3.html",
    "http://www.offcn.com/yinhang/shiti/2401/4.html"
]

get_pate = []

rgx_1 = r"http[s]?://www.offcn.com/yinhang/2018/\d{4}/\d{5}.html"
rgx_2 = r"<title>.*</title>"
rgx_3 = r'<div class="nry_content">.*?</div>'

for url in urls:
    res = r.get(url)
    res.encoding = 'gbk'
    ma_list = re.findall(rgx_1, res.text)
    get_pate += ma_list

for url in get_pate:
    try:
        res = r.get(url)
        content = decode(res.content, 'gbk')

        hd = re.findall(rgx_2, content)[0]
        hd = hd.replace("<title>", "").replace("</title>", "")

        ct = re.findall(rgx_3, content, flags=re.S)
        if ct:
            ct = ct[0]
        else:
            print(hd, 'no nry_content')
            continue

        gac = []
        for i in ct.splitlines():
            if re.search(r'</?[atds]', i):
                continue
            else:
                i = i.strip('</p>')
                i = html.unescape(i)
                gac.append(i)
        del gac[len(gac) - 1]
        del gac[0]
    
    except IndexError:
        print(hd, "gac:", gac)
    
    with open(f'./out/{hd}.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(gac))
