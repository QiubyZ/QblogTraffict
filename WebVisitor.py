import requests
import os
from re import findall
from bs4 import BeautifulSoup as cantik
def banner():
    os.system("clear")
    __author__ = "Qiuby Zhukhi"
    __TEAM__ = "-- [ PBM-TEAM ] --"
    print """                                        

     _         _        
    / \  _   _| |_ ___  Author: {}
   / _ \| | | | __/ _ \ Team: {}
  / ___ \ |_| | || (_) |webTraffic
 /_/   \_\__,_|\__\___/ 
        """.format(__author__, __TEAM__)
list = []
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

def pepong():
    cek = requests.session()
    dic = {}
    count = 0
    pro = "https://www.sslproxies.org"
    page = cek.get(pro).text
    proxy = findall(r"\d+\.\d+\.\d+\.\d+",page)
    port = findall(r"\**<td>\d+</td>", page)
    for i in range(len(proxy)):
        count += 1
        ports = port[i].replace("<td>", "").replace("</td>", "")
        print str(count)+". "+B+proxy[i]+":"+str(ports)+W
        dic.update({proxy[i]:str(ports)})        
    return dic

def parser(p):
    try:
        bs4 = cantik(p, "html.parser").find("span", {"class":"td-nr-views-4492"})
        return bs4.text
    except AttributeError, e:
        return e
        
def strawpoll(proxy, url):
    views = ""
    proxy = {"https":"https://"+proxy}
#             "http":"http://"+proxy}
    h = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.185.1002 Safari/537.36",
         "Connection":"keep-alive"}
    req = requests.session()
    try:
        resp = req.get(url, proxies=proxy, timeout=3, stream=True, headers=h)

#        req = req.get(url, proxies=proxy,timeout=3,stream=True, headers=None)
        view = parser(resp.text)
        print resp.headers
        print "Jumlah: ", view
    except requests.exceptions.ConnectionError as e:
        print "Tidak dapat tersambung ke proxy ", proxy
    except requests.exceptions.Timeout, e:
        print "Proxy TimeOut"
    except requests.exceptions.ContentDecodingError, e:
        print e
    except:
        print "Tidak dapat tersambung ke ", proxy
    req.cookies.clear()
    req.close()  

def start(jumlah,url):
    n = 0
    for number in range(0,jumlah):
        print "TES TING GRAB PROXY ( %s )"+str(number)
        for proxy, port in pepong().items():
            n += 1
            proxy = proxy+":"+port
            print "==== [ PROXY TEST ] ===="
            print proxy
            print url
            strawpoll(proxy,url)
        print "Total Proxy Test: ", str(n) 
        print "==== [ FINISH ] ===="

if __name__ == "__main__":
    url = "laptop-ajaib.blogspot.com"
#    url = "penasultra.com/2018/08/02/seleksi-cpns-di-sultra-menunggu-kepres/"
    if url:
        url = "https://"+url
    jml = 1
    banner()
#    pid = raw_input("insert PID: ")
#    vote = raw_input("insert check Vote: ")
#    jml = int(raw_input("Jumlah grab: "))
#    url = raw_input("insert Url: ")    
    start(jml, url)
