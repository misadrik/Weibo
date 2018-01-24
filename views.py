import json
import csv

seed_url = 'https://m.weibo.cn/api/comments/show?id={}&page={}'

def get_one_card_view(view_data):
    one_card_view = {}
    one_card_view['id'] =  view_data['id']
    one_card_view['created_at'] = view_data['created_at']
    one_card_view['source'] = view_data['source'] if view_data['source'] else None
    one_card_view['text'] = view_data['text']

    if 'reply_text' in view_data:
        one_card_view['is_reply'] = 1
        one_card_view['reply_text'] = view_data['reply_text']
        one_card_view['reply_id'] = view_data['reply_id']
        one_card_view['relike_counts'] = view_data['like_counts']
    else:
        one_card_view['is_reply'] = 0
        one_card_view['reply_text'] = None
        one_card_view['reply_id'] = None
        one_card_view['like_counts'] = view_data['like_counts']
        one_card_view['view_id'] = view_data['user']['id']
        one_card_view['view_name'] = view_data['user']['screen_name']

    return one_card_view





def get_one_page_view(view_data,page):
    fcsv = open('views.csv','a',encoding = 'utf-8',newline = '') 
    fieldnames = ['id','created_at','source','is_retweet','is_long_text','text','text_length','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    # fieldnames = ['created_at','id','is_retweet','is_long_text','text','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    
    writer = csv.DictWriter(fcsv, fieldnames=fieldnames)
    for card in view_data:
        writer.writerow(get_one_card_view(card))

'''获取页码，根据链接'''
def get_all_view(id,headers):
        i = 1
        while True:
            wb_data = requests.get(seed_url.format(id,'i'),headers = headers)
            Data = json.loads(wb_data.text)

            htmlstr = Data['data']
            total_number = htmlstr['total_number']
            Max_page = htmlstr['max']
            # print(htmlstr)
            view_data = htmlstr['data']
            get_one_page_view(views,i)

            if i == Max_page:
                break
            else:
                i = i + 1

            print(id +'\'s '+ i +' of '+ total_number + ' views Done!')
    #print(htmlstr,file = fc)
    
    