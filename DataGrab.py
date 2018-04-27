import json
import csv

'''获得一个卡片下的信息'''
'''读入：'''
'''输入：已从json提取出的字典形式的一个卡片的数据 页码'''
'''输出：'''
'''返回：以字典形式返回微博数据'''
host_url = 'https://m.weibo.cn'
def get_one_card_Info(mblog,page):
    one_card_Info = {}
    ##'''加入页码，方便校对'''##
    ##'''但仍然会有返回数据不一致问题，待消除，可能可以利用id但要改进存储方式防止截断'''##
    one_card_Info['page'] = page
    one_card_Info['created_at'] = mblog['created_at'] #发微博时间
    one_card_Info['id'] = mblog['id']  #微博id
    # mid = mblog['mid']
    '''点赞、转发标记'''
    # reports_count = mblog['reports_count']
    one_card_Info['comments_count'] = mblog['comments_count']
    one_card_Info['attitudes_count'] = mblog['attitudes_count']
    one_card_Info['source'] = mblog['source']
    
    '''是否含有图片'''
    if 'pics' in mblog:
        one_card_Info['has_pics'] = 1
        ##'''待加入自动下图片函数，有图直接下''##
        one_card_Info['pics_num'] = len(mblog['pics'])
        
        L = []
        for pic in mblog['pics']:
            L.append(pic['large']['url'])

        one_card_Info['pics'] = L

    '''标记是否转发'''
    if 'raw_text' in mblog:
        one_card_Info['is_retweet'] = 1
        one_card_Info['text'] = mblog['raw_text'].split('//')[0]
        one_card_Info['is_long_text'] = 0  #判断长文
    else:
        one_card_Info['is_retweet'] = 0
        ###'''15末以前的博文没有此标识，要加入判断'''###
        if 'textLength' in mblog:
            one_card_Info['text_length'] = mblog['textLength']
        else:
            one_card_Info['text_length'] = None
        '''长文判断,转发判断'''
        '''处理表情<img src="//h5.sinaimg.cn/m/emoticon/icon/default/d_hehe-4f9f713058.png" style="width:1em;height:1em;" alt="[微笑]">'''
        if mblog['isLongText']:
            one_card_Info['is_long_text'] = 1
            text_url = host_url + '/status/' + one_card_Info['id']
            one_card_Info['text'] = text_url
        else:
            one_card_Info['is_long_text'] = 0
            ##'''要加入文章内容筛选，去表情链接'''##
            one_card_Info['text'] = mblog['text']

    ##'''标记仅好友可见内容标识'''##
    if 'title' in mblog:
        if mblog['title']['text'] == '仅好友可见':
            one_card_Info['auth'] = 1
        elif mblog['title']['text'] == '置顶':
            one_card_Info['auth'] = 2
        else:
            one_card_Info['auth'] = 10
    else:
        one_card_Info['auth'] = 0
    ##'''扒评论函数'''##
    ##'''评论人，内容，点赞等'''##

    #one_card_Info = [created_at,blog_id,is_retweet,is_long_text,text,text_length,source, comments_count,attitudes_count]
    
    return one_card_Info


#fw = open('mblog4.txt','w',encoding = 'utf-8') 
#fc = open('card.txt','w',encoding = 'utf-8')
# f = open('getIndex24.json')
'''从json中获取一页数据'''
'''读入：'''
'''输入：从网页返回的json数据 页码'''
'''输出：weibo.csv 微博数据'''
'''返回：'''
def get_one_page_data(data,page):
    fcsv = open('weibo.csv','a',encoding = 'utf-8',newline = '') 
    fieldnames = ['created_at','id','auth','is_retweet','is_long_text','text','text_length','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    # fieldnames = ['created_at','id','auth','is_retweet','is_long_text','text','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    Data = json.loads(data)
    #Data = json.load(data)
    # print(Data)

    htmlstr = Data['data']
    # print(htmlstr)
    cards = htmlstr['cards']
    #print(htmlstr,file = fc)
    
    writer = csv.DictWriter(fcsv, fieldnames=fieldnames)
    # writer.writeheader() # 写入文件头
    for card in cards:
        if card['card_type'] == 9:
            #print(card['mblog'],file = fc)    
            #print(get_one_card_Info(card['mblog']),file = fw)
            writer.writerow(get_one_card_Info(card['mblog'],page))

    print('Page '+ str(page) +' Done!')
# get_one_page_data(f)

# def get_one_card_user_Info(user):
#     user_name = user['screen_name']
#     profile_img


    # mblog = cards['mblog']
    # print(mblog)

# fw = open('cards.txt','w',encoding = 'utf-8')  
# print(cards,file = fw)