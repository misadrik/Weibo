import requests
import time
from fans import get_one_page_fans

##只能下前500多个粉丝，关注的人更是只能第一页，可能新浪限制
'''####'''处换成自已id
start_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_####&type=all&since_id={}'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.3 Mobile Safari/537.36',
    'Cookie':''
    }

def get_fans_data():
    for page in range(1,100):
        fans_data = requests.get(start_url.format(str(page)),headers = headers)
        print('Page ' + str(page) + ' info get!')
       # print(fans_data.content)
        #print(fans_data.encoding)
        get_one_page_fans(fans_data.content,page)
        time.sleep(10)
        if page < 40:
            time.sleep(5)
        elif page < 80:
            time.sleep(10)
        else:
            time.sleep(15)

if __name__ == '__main__':
    get_fans_data()
