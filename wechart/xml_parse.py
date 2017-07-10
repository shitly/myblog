import urllib.request as ur

from bs4 import BeautifulSoup
import re
import pandas as pd
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码  

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = ur.Request(url=url, headers=headers)  # python2，urllib.request()
    response = ur.urlopen(req)  # python2，urllib2.urlopen()
    return response.read().decode('utf-8')


def parse_xml():
    with open("e://c.txt", "r", encoding="utf-8") as f:
        data = f.read()
        f.close()

    print("==========================0-===========")
    import re
    partern = r'''.*<item>(.*?).*'''
    data1 = re.findall(partern, data, flags=0)
    print(data1)
import xml_parse
# parse_xml()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') #改变标准输出的默认编码  
file = 'F:\\this_file_can_be_delete_anytime\\SUMMARY\\wk\\mysite1\\focus\\templates\\new 1.html'

with open(file, "r+") as f:
    data = f.read()
from bs4 import BeautifulSoup
soup1 = BeautifulSoup(data, 'html.parser')
tt = soup1.findAll("item")
print(tt)