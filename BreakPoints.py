
seed_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1736657132&containerid=1076031736657132&page={}'
def generate_sites(start, end, url):
    f = open('download.txt','a',encoding = 'utf-8')
    for page in range(start,end + 1):
        print(seed_url.format(str(page)),file = f)

    print('urls: ' + str(start) + ' to ' + str(end) + ' generated!')

def get_urls_to_download():
    ftodownload = open('download.txt','r')
    fdownloaded = open('downloaded.txt','r')
    fout = open('123.txt','a',encoding = 'utf-8')
    
    urls_to_download = []

    for url in ftodownload:
        url = url.split('\n')[0]
        if url not in urls_to_download:
            urls_to_download.append(url)

    # urls_to_download = set()
    # for url in fin:
    #    url = url.split('\n')[0]
    #    urls_to_download.add(url) 

    url_downloaded = [url.split('\n')[0] for url in fdownloaded]
    print(list(set(urls_to_download) - set(url_downloaded)),file = fout)
    #print(str(len(urls_to_download)) + ' urls get!')
    return set(urls_to_download) - set(url_downloaded)


def record_downloaded_urls(url):
    fout = open('downloaded.txt',"a",encoding = 'utf-8')
    print(urls,file = fout)

    

if __name__ == '__main__':
#     #generate_sites(1,1150,seed_url)
    get_urls_to_download()