
#seed_url = ''
'''生成链接函数'''
'''读入：无'''
'''输入：起止年份，种子url'''
'''输出：download.txt下载链接'''


def generate_sites(start, end, seed_url):
    f = open('download.txt', 'a', encoding='utf-8')
    for page in range(start, end + 1):
        print(seed_url.format(str(page)), file=f)

    print('urls: ' + str(start) + ' to ' + str(end) + ' generated!')


'''读入待爬链接程序'''
'''读入：download.txt由generate_sites函数产生的链接文本'''
'''输入：无'''
'''输出：'''
'''返回：以列表形式返回读入的url'''


def get_urls_to_download():
    ftodownload = open('download.txt', 'r')
    # fdownloaded = open('downloaded.txt','r')
    # fout = open('123.txt','a',encoding = 'utf-8')

    urls_to_download = []

    for url in ftodownload:
        url = url.split('\n')[0]
        if url not in urls_to_download:
            urls_to_download.append(url)

    # urls_to_download = set()
    # for url in fin:
    #    url = url.split('\n')[0]
    #    urls_to_download.add(url)
    return urls_to_download

    # url_downloaded = [url.split('\n')[0] for url in fdownloaded]
    # return list(set(urls_to_download) - set(url_downloaded))


'''输出已爬链接程序'''
'''读入：无'''
'''输入：无'''
'''输出：downloaded.txt已下载链接'''


def record_downloaded_urls(url):
    fout = open('downloaded.txt', "a", encoding='utf-8')
    print(url, file=fout)


'''输出爬取失败链接程序'''
'''读入：无'''
'''输入：无'''
'''输出：failed.txt下载失败链接'''


def record_failed_urls(url):
    fout = open('failed.txt', "a", encoding='utf-8')
    print(url, file=fout)


if __name__ == '__main__':
    generate_sites(1, 50, seed_url)
    # get_urls_to_download()
