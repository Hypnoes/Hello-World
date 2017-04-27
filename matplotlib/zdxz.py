import re
import requests

def main():

    url = 'http://matplotlib.org/examples/animation/{0}'
    reg = re.compile(r'reference internal" href="\S*.html')
    reg2 = re.compile(r'"\S*.html')
    a = []

    r = requests.get(url.format('index.html'))
    page = r.content.decode()
    s = reg.findall(page)
    for i in s:
        a.append(reg2.findall(i)[0][1:-4] + "py")
    for i in a:
        with open(i, 'w') as f:
            content = requests.get(url.format(i)).content.decode()
            f.writelines(content)

if __name__ == '__main__':
    main()
