import requests
import re

url = 'http://matplotlib.org/examples/animation/{0}'
r = requests.get(url.format('index.html'))
print(r.status_code)
page = r.content.decode()
reg = re.compile('reference internal" href="\S*.html')
s = reg.findall(page)
reg2 = re.compile('"\S*.html')
a = []
for i in s:
    a.append(reg2.findall(i)[0])
b = []
for i in a:
    b.append(i[1:-4] + "py")
for i in b:
    with open(i, 'w') as f:
        content = requests.get(url.format(i)).content.decode()
        f.writelines(content)