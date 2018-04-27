import csv
import urllib.request
import time
from threading import Thread
import multiprocessing
import datetime
import gevent
from gevent.pool import Pool
'''断点续传程序'''
from gevent import monkey
monkey.patch_all()


def break_piont_continue():
    to_down = open('weibo.csv', 'r', encoding='utf-8', newline='')
    csv_data = csv.reader(to_down)

    download_urls, downloaded_urls = [], []
    count = 0
    for data in csv_data:
        if data[9] == '':
            pass
        elif len(data[9].split(',')):
            # print([data[9].strip('[').strip(']').strip('\'')])
            # print('---')
            # print(len(data[9].split(',')))
            # 读入数据为urls字符串，去除无用字符转为url—list
            # print(repr(data[9].split(',')[1].strip(
            #     '[').strip(']').strip(' ').strip('\'')))

            # 读入数据为urls字符串，去除无用字符转为url—list
            for num in range(len(data[9].split(','))):
                # print(num)
                download_urls.append(data[9].split(
                    ',')[num].strip('[').strip(']').strip(' ').strip('\''))
                print(str(count) + ' Done!')
                count = count + 1
        else:
            print('Error')

    # f = open('download_pics.txt', 'w', encoding='utf-8')
    # for url in download_urls:
    #     print(url, file=f)

    return download_urls


'''下载图片程序'''

def download_pics(url):
    folder_path = 'D:/Python/WeiboCrawler/Download_pics/'
    fout = open('failed_pics.txt', "a", encoding='utf-8')
    print('download_pics')
    try:
        urllib.request.urlretrieve(
            url, folder_path + url.split('/')[-1])
        time.sleep(1)
        print('pic: ' + url.split('/')[-1] + ' done!')
    except:
        print(url, file=fout)  # 下载失败 保存链接
        print('pic: ' + url.split('/')[-1] + ' failed!')

def Coroutine_run(urls):
    p = Pool()
    p.map(download_pics, urls)
    # g = [gevent.spawn(download_pics, url) for url in urls]
    # gevent.joinall(g)


def multi_process(urls):
    process = []
    url_group_0 = []
    url_group_1 = []
    url_group_2 = []
    url_group_3 = []

    for index in range(len(urls)):  # 将url分为四组
        if index % 4 == 0:
            url_group_0.append(urls[index])
        elif index % 4 == 1:
            url_group_1.append(urls[index])
        elif index % 4 == 2:
            url_group_2.append(urls[index])
        elif index % 4 == 3:
            url_group_3.append(urls[index])
    url_groups = [url_group_0, url_group_1, url_group_2, url_group_3]

    for each_group in url_groups:  # 每组执行多线程下载
        each_process = multiprocessing.Process(
            target=Coroutine_run, args=(each_group,))
        process.append(each_process)
    for one_process in process:
        one_process.start()
    for one_process in process:
        one_process.join()          # 阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。


if __name__ == '__main__':
    start_time = datetime.datetime.now()  # 用于统计时间
    #    break_piont_continue()
    download_urls = break_piont_continue()
    multi_process(download_urls)
    # Coroutine_run(download_urls)
    end_time = datetime.datetime.now()
    print(end_time - start_time)
