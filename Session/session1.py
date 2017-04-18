#! python3
#  -*- coding:utf-8 -*-
__author__ = 'Hypnoes'

import os, re, urllib
import urllib.request

rootUrl = 'http://www.heibanke.com/lesson/crawler_ex00/'
viewedContent = []

def begin():
    url = rootUrl
    with open('spider.txt','w', encoding='utf-8') as f:
        while url != None:
            f.write('****************************************************************\n')
            f.write('On page {0} we find:\n'.format(url))
            f.write(getContent(url)+'\n')
            print(getContent(url))            
            url = getNextUrl(url)
            f.write("Next page: {0}\n".format(url))
            f.write('****************************************************************\n')            
        f.write('=============================END================================')
    

def getPage(url):
    req = urllib.request.Request(url)
    rep = urllib.request.urlopen(req)
    if rep.code in range(200,299):
        return rep.read().decode()
    else:
        print('Http Error:{0}'.format(rep.code))
        return 'Http Error:{0}'.format(rep.code)

def getNextUrl(url):
    page = getPage(url)
    reg = re.compile('<h3>(.)*</h3>')
    reg2 = re.compile('\d{5}')
    try:
        s = reg.search(page).group(0)      
        nextId = reg2.search(s).group(0)
    except:
        return
    viewedContent.append(nextId)
    return rootUrl+nextId

def getContent(url):
    page = getPage(url)
    reg = re.compile('<h3>(.)*</h3>')
    try:
        s = reg.search(page).group(0)
        return s[4:-5]
    except:
        return 'Not in here!'

if __name__ == '__main__':
    begin()

