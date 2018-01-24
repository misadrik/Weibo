import requests
import time
from DataGrab import get_one_page_data
from BreakPoints import get_urls_to_download,record_downloaded_urls,record_failed_urls

##'''多进程爬取，想办法消除下载顺序问题后加入'''##
##'''加代理'''##
start_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1736657132&containerid=1076031736657132&page={}'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.3 Mobile Safari/537.36',
    'Cookie':'_T_WM=6ee6c87c3fab3ac21e8b10a5c33a11f1; SCF=AoNFHvGJl-JZuW6e8OvC4yd7v_qoQuRuFUgEq_eK979h9vYTORkiHst88dluLBr_MvaPzIFnpPMBfOmtU0Gvgr4.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWD8SbcsE2cNcX2Sz9r9d215JpX5K-hUgL.Fo2R1KMNSo.NSoB2dJLoI79DK-LKq-Bt; SUB=_2A253YqdgDeRhGedG4lUW9ifLzTiIHXVUrMkorDV6PUJbkdBeLXndkW1NUOegEovkfNck4zAmPPw4scwhQeyHrc_Q; SUHB=079ilYP948qg6Y; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2310021736657132_-_HOTMBLOG%26fid%3D1076031510517954%26uicode%3D10000011',
    'Refer':'https://m.weibo.cn/u/1736657132'
}

def get_wb_data():
    url_to_download = get_urls_to_download()
    ##'''加入已爬取识别'''##
    for url in url_to_download:
    #for page in [110,111,112,113]:
        page = int(url.split('=')[-1])
        try:
            wb_data = requests.get(url,headers = headers)
            print('Page ' + str(page) + ' data get!')
        except:
            print('Page ' + str(page) + ' failed!')
            record_failed_urls(url)
            time.sleep(30)
        else:
            get_one_page_data(wb_data.text,page)
            time.sleep(10)
            record_downloaded_urls(url)

if __name__ == '__main__':
    get_wb_data()
