#!python3

from typing import Generator

import requests
from pyquery import PyQuery as pq

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

def get_page(url: str) -> str:
    headers = dict(base_headers)
    print('Getting ', url)
    try:
        r = requests.get(url, headers=headers)
        print('Getting responds', url, r.status_code)
        if r.ok:
            return r.text
    except ConnectionError:
        print('Crawling Failed', url)

class ProxyMetaclass(type):
    """
        Meta class: FreeProxyGetter

        `params`:
            `__CrawlFunc__` : craw function.
            `__CrawlFuncCount__` : craw function count.
    """
    @classmethod
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        count = 0
        attrs['__CrawlFunc__'] = []
        attrs['__CrawlName__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlName__'].append(k)
                attrs['__CrawlFunc__'].append(v)
                count += 1
        for k in attrs['__CrawlName__']:
            attrs.pop(k)
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)

class ProxyGetter(object, metaclass=ProxyMetaclass):
    def get_raw_proxies(self, site: str) -> list:
        proxies = []
        print('Site', site)
        for f in self.__CrawlFunc__:
            if f.__name__ == site:
                this_page_proxies = f(self)
                for proxy in this_page_proxies:
                    print('Getting', proxy, 'from', site)
                    proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4) -> Generator:
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_proxy360(self) -> Generator:
        start_url = 'http://www.proxy360.cn/Region/China'
        print('Crawling', start_url)
        html = get_page(start_url)
        if html:
            doc = pq(html)
            lines = doc('div[name="list_proxy_ip"]').items()
            for line in lines:
                ip = line.find('.tbBottomLine:nth-child(1)').text()
                port = line.find('.tbBottomLine:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_goubanjia(self) -> Generator:
        start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
        html = get_page(start_url)
        if html:
            doc = pq(html)
            tds = doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                yield td.text().replace(' ', '')

if __name__ == '__main__':
    crawler = ProxyGetter()
    print(crawler.__CrawlName__)
    for site_label in range(crawler.__CrawlFuncCount__):
        site = crawler.__CrawlName__[site_label]
        myProxies = crawler.get_raw_proxies(site)
