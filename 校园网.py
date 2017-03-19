import requests
url = 'http://10.10.10.10/srun_portal_pc.php?ac_id=1&url='
k = {'action':'login','username':'123456','password':'{B}MTIzNDU2','ac_id':'1','user_ip':'','nas_ip':'','save_me':'0','ajax':'1'}
h = {'X-Requested-With':'XMLHttpRequest','Cache-Control':'no-cache','User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)'}
r = requests.post(url, data=k, headers=h)

        
