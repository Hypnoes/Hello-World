import requests
import re, time

def con():
    url = 'http://10.10.10.10/srun_portal_pc.php?ac_id=1&url='
    k = {'action':'login','username':'123456','password':'{B}MTIzNDU2','ac_id':'1','user_ip':'','nas_ip':'','save_me':'0','ajax':'1'}
    h = {'X-Requested-With':'XMLHttpRequest','Cache-Control':'no-cache','User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)'}
    r = requests.post(url, data=k, headers=h)
    return r

def tes(sec):
    baidu = 'http://www.baidu.com'
    mc = r'10\.10\.10\.10'
    t = requests.get(baidu)
    if re.search(mc, t.url) == None:
        print('Yes')
        return time.sleep(sec)                  #链接正常
    else:
        print('No')
        return con()                            #链接异常

def main():
    i = 5
    r = con()
    while(tes(i) == None):
        i = i * 2
        if i > 1800:
            i = 1280

#if __name__ == '__main__ ':
while(True):
    main()
        
