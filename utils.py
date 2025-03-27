import re
import requests
from bs4 import BeautifulSoup

class html_get():
    def __init__(self,url):
        self.bs = BeautifulSoup(requests.get(url).content,"lxml")
        self.bs=self.bs.p.string
        self.string=str(self.bs)
        
        #covid_contry=re.search(re_con,self.string)
        #self.num = re.search(re_num,self.string)
        #self.con=covid_contry[0]


if __name__=='__main__':
    html_get_result=html_get("https://www.ams.usda.gov/mnreports/wa_gr101.txt")
    print(html_get_result.string)