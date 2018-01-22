import csv
import urllib.request
import time


'''断点续传程序'''
def break_piont_continue():
    to_down = open('weibo.csv','r',encoding = 'utf-8',newline = '') 
    csv_data = csv.reader(to_down)

    download_urls, downloaded_urls = [],[]
    
    for data in csv_data:
        download_urls.append(mv_list[2])

    downed = open('downloaded.txt','r')
    downloaded_urls = []
    for url in urls:
            downloaded_urls.append(url.strip('\n')) 

    return set(download_urls) - set(downloaded_urls)


'''下载图片程序'''
def download_pics(urls):
    folder_path = 'D:/Python/weibo/pics/'
    for url in urls:
        urllib.request.urlretrieve(url, folder_path + url.split('/')[-1])
        time.sleep(20)