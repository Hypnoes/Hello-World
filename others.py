import re
import requests

reg = r"""<a href=["|']\S*.avi["|']>"""
reg2 = r"""http.*\.avi"""

r = requests.get("http://cvlab.epfl.ch/data/pom/")

cont = r.content.decode()

x = re.findall(r, cont)

links = []
for i in x:
    link = re.findall(reg2, x)
    links.append(link[0])

for i in links:
    savename = i.split('/')[-1]
    with open(savename, "wb") as target:
        target.write(requests.get(i).content)
        