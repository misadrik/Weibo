from bs4 import BeautifulSoup
import requests
import time
from dataprocess import get_one_page_data

##'''多进程爬取，想办法消除下载顺序问题后加入'''##
##'''加代理'''##
start_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1736657132&containerid=1076031736657132&page={}'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3253.3 Safari/537.36',
    'Cookie':'',
    'Refer':'https://m.weibo.cn/u/1736657132'
}

def get_wb_data():
    ##'''加入已爬取识别'''##
    for page in range(0,100):
    #for page in [110,111,112,113]:
        wb_data = requests.get(start_url.format(str(page)),headers = headers)
        get_one_page_data(wb_data.text,page)
        time.sleep(20)
        if page < 40:
            time.sleep(5)
        elif page < 80:
            time.sleep(10)
        else:
            time.sleep(15)

if __name__ == '__main__':
    get_wb_data()
