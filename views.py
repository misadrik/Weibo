import json
import csv

seed_url = 'https://m.weibo.cn/api/comments/show?id={}&page={}'

def get_one_card_view():



def get_one_page_view(view_data):
    fcsv = open('weibo.csv','a',encoding = 'utf-8',newline = '') 
    fieldnames = ['created_at','id','is_retweet','is_long_text','text','text_length','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    # fieldnames = ['created_at','id','is_retweet','is_long_text','text','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    
    writer = csv.DictWriter(fcsv, fieldnames=fieldnames)


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
            get_one_page_view()

            if i == Max_page:
                break
            else:
                i = i + 1

        print(id+'\'s '+ total_number + ' views Done!')
    #print(htmlstr,file = fc)
    
    