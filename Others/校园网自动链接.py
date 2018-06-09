import requests
import re, time

def con():
    url = 'http://10.10.10.10/srun_portal_pc.php?ac_id=1&url='
    k = {
        'action':'login',
        'username':'16108028',
        'password':'{B}MTE4MDI3',
        'ac_id':'1',
        'user_ip':'',
        'nas_ip':'',
        'save_me':'0',
        'ajax':'1'
        }
    h = {
        'X-Requested-With':'XMLHttpRequest',
        'Cache-Control':'no-cache',
        'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)'
        }
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
    i = 60
    r = con()
    while(tes(i) == None):
        pass
        
#if __name__ == '__main__ ':
while(True):
    main()
