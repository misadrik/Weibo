import csv
import urllib.request
import time
from threading import Thread
import multiprocessing
import datetime
'''断点续传程序'''


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


def download_pics(urls, thread_id):
    folder_path = 'D:/Python/WeiboCrawler/Download_pics/'
    fout = open('failed_pics.txt', "a", encoding='utf-8')
    print('thread: %d is running' % (thread_id))
    for url in urls:
        try:
            urllib.request.urlretrieve(
                url, folder_path + url.split('/')[-1])
            time.sleep(1)
            print('pic: ' + url.split('/')[-1] + ' done!')
        except:
            print(url, file=fout)  # 下载失败 保存链接
            print('pic: ' + url.split('/')[-1] + ' failed!')
            # else:
            #     time.sleep(2)
            #     print('pic: ' + url.split('/')[-1] + ' done!')


def thread_run(download_urls):  # 多线程
    url_group_0 = []
    url_group_1 = []
    url_group_2 = []
    url_group_3 = []

    for index in range(len(download_urls)):  # 将url分为四组
        if index % 4 == 0:
            url_group_0.append(download_urls[index])
        elif index % 4 == 1:
            url_group_1.append(download_urls[index])
        elif index % 4 == 2:
            url_group_2.append(download_urls[index])
        elif index % 4 == 3:
            url_group_3.append(download_urls[index])

    url_groups = [url_group_0, url_group_1, url_group_2, url_group_3]

    for i in range(0, 4):
        try:
            t = Thread(target=download_pics, args=(url_groups[i], i))
            t.start()
        except:
            print('wrong')


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
            target=thread_run, args=(each_group,))
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
    end_time = datetime.datetime.now()
    print(end_time - start_time)
