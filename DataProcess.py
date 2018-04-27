import csv
import re
from DrawBarChart import one_year_bar_chart, draw_stackedbar_chart,year_bar_chart,draw_source_bar_pic
from FenCi import fenci
#fin = open('x2010.csv','r',encoding = 'utf-8')

'''获得数据'''
'''按读入顺序，把数据存入列表并返回'''
'''读入：csv_filename.csv 微博数据文本，以utf-8带bom编码（windows)'''
'''输入：文件名'''
'''输出：'''
'''返回：以每一行的有序字典列表形式返回微博数据'''
def get_data(csv_filename):
    fin = open(csv_filename + '.csv','r',encoding = 'utf-8-sig')
    # reader = csv.reader(fin,delimiter=',')
    # fieldnames = next(reader)
    raw_data = []
    fieldnames = ['created_at','id','auth','is_retweet','is_long_text','text','text_length','has_pics','pics_num','pics','source', 'comments_count','attitudes_count','page']
    # reader = csv.DictReader(fin,fieldnames = fieldnames)
    reader = csv.DictReader(fin,fieldnames = fieldnames)
    for row in reader:
        raw_data.append(row)

    print('data get')
    return raw_data

'''将按年分好类的数据按月分类'''
'''读入：'''
'''输入：按年分好类的数据'''
'''输出：'''
'''返回：每一月为一个key值的字典，其value为微博数据的列表'''
def clarify_by_month(data):    
    ###'''待优化'''###
    '''数据按月存入字典'''
    dict_data_month = {}
    '''每月数据存入列表'''
    list_data = []
    last_month = 12
    '''分词'''
    text = ''
    file_name = ''

    for row in data:
        t = re.split('\W+',row['created_at']) 
        file_name = t[0] 
        # row['']为Date字段,被拆为['2010', '11', '05']      
        if last_month != int(t[1]): # 按月分类
            dict_data_month[str(last_month)] = list_data
            list_data = []
            last_month = int(t[1])

        text = text + ' , ' + row['text']
        list_data.append(row)

    dict_data_month[str(last_month)] = list_data #最后一个月的数据

    fenci(text,file_name + '.txt')
    print('clarify_by_month done!')

    return dict_data_month

'''将数据按年分类'''
'''读入：'''
'''输入：列表形式的微博数据数据'''
'''输出：'''
'''返回：每一年为一个key值的字典，其value为按月分好类的字典'''
def clarify_by_year(data,end):
    dict_data_year = {}
    '''每月数据存入列表'''
    list_data = []
    last_year = end
    for row in data:
        t = re.split('\W+',row['created_at'])  
        # row['']为Date字段,被拆为['2010', '11', '05']  
        if last_year != int(t[0]): # 按年分类  
            dict_data_year[str(last_year)] = clarify_by_month(list_data)
            list_data = []
            last_year = int(t[0])

        list_data.append(row)

    dict_data_year[str(last_year)] = clarify_by_month(list_data) #最后一个月的数据

    print('clarify_by_year done!')

    return dict_data_year

'''获得一年中月数据的统计值'''
'''读入：'''
'''输入：一个月数据列表'''
'''输出：'''
'''返回：字典，一个月统计值，'''
def get_statistical_data(by_month):
    blog_num = len(by_month)

    word_num, pic_blog_num, com_num, att_num, ret_num, auth_num = 0,0,0,0,0,0
    for row in by_month:
        if row['text_length']:
            word_num = word_num + int(row['text_length'])
        if row['pics_num']:
            pic_blog_num = pic_blog_num + int(row['has_pics'])
        
        com_num  = com_num  + int(row['comments_count'])
        att_num  = att_num  + int(row['attitudes_count'])
        ret_num  = ret_num  + int(row['is_retweet'])

        if row['auth'] == 1:
            auth_num = auth_num + 1
    
    statistics = {}

    statistics['blog_num'] = blog_num
    statistics['word_num'] = word_num
    statistics['pic_blog_num'] = pic_blog_num
    statistics['com_num']  = com_num
    statistics['att_num']  = att_num
    statistics['ret_num']  = ret_num
    statistics['auth_num'] = auth_num
    if blog_num == 0:
        statistics['avg_word'] = 0
        statistics['avg_ret'] = 0
    else:
        statistics['avg_word'] = round(word_num / blog_num, 0)
        #statistics['avg_com']  = round(att_num  / blog_num, 1)
        statistics['avg_ret']  = round(ret_num  / blog_num * 100, 1)
        
    
    return statistics

'''得到一年中每一个月的统计值'''
'''读入：'''
'''输入：按月分类的数据'''
'''输出：'''
'''返回：一年中每一个月的统计值，及一年总统计值，字典'''
def get_months_statistical_data(mon_data,year):#后期加入文件名
    # data = get_data()
    # mon_data = clarify_by_month(data)
    one_year_data = [] # 按月排列一年统计数据
    year_blog_num, year_word_num, year_retweet_num = 0,0,0
    year_pic_blog_num, year_com_num,   year_att_num = 0,0,0
    for month in range(1,13):
        try:
            mon = mon_data[str(month)]
        except:
            print('No month ' + str(month) + ' values!')# 后期无数据全设成零
            one_year_data.append({'blog_num': 0,'word_num': 0,'pic_blog_num': 0, 'com_num':0, 'att_num': 0,
                                        'ret_num':0,'auth_num': 0,'avg_word': 0,'avg_ret':0})
            # one_year_data.append({'blog_num': 0,'word_num': 0,'pics_num': 0, 'com_num':0, 'att_num': 0,
            #                             'ret_num':0,'auth_num': 0, 'avg_word': 0, 'avg_com':0, 'avg_ret':0})
        else:
            one_year_data.append(get_statistical_data(mon))
    
    month_data_classified = {} #统计数据提取归类并存入字典中
    year_data = {}
    blog_num, word_num, pic_blog_num, com_num, att_num = [],[],[],[],[]
    ret_num, auth_num, avg_word,avg_ret= [],[],[],[] 
    # avg_com = []
    for row in one_year_data:
        year_blog_num = year_blog_num + row['blog_num']
        blog_num.append(row['blog_num'])

        year_word_num = year_word_num + row['word_num']
        word_num.append(row['word_num'])

        year_pic_blog_num = year_pic_blog_num + row['pic_blog_num']
        pic_blog_num.append(row['pic_blog_num'])

        year_com_num =  year_com_num + row['com_num']
        com_num.append(row['com_num'])

        year_att_num = year_att_num + row['att_num']
        att_num.append(row['att_num'])

        year_retweet_num = year_retweet_num + row['ret_num']
        ret_num.append(row['ret_num'])

        auth_num.append(row['auth_num'])
        avg_word.append(row['avg_word'])
        #avg_com.append(row['avg_com'])
        avg_ret.append(row['avg_ret'])

    month_data_classified['blog_num'] = blog_num
    month_data_classified['word_num'] = word_num
    month_data_classified['pic_blog_num'] = pic_blog_num
    month_data_classified['com_num']  = com_num
    month_data_classified['att_num']  = att_num
    month_data_classified['ret_num']  = ret_num
    month_data_classified['auth_num'] = auth_num
    month_data_classified['avg_word'] = avg_word
    #month_data_classified['avg_com']  = avg_com
    month_data_classified['avg_ret']  = avg_ret
    #print(one_year_data)
    year_data['year_blog_num']     = year_blog_num
    year_data['year_word_num']     = year_word_num
    year_data['year_pic_blog_num'] = year_pic_blog_num
    year_data['year_com_num']      = year_com_num
    year_data['year_att_num']      = year_att_num
    year_data['year_retweet_num']  = year_retweet_num

    print(str(year) + '\'s statistical data classified!')
    return month_data_classified, year_data

###'''主要函数'''###
'''从文件读入所有年份数据，并归类'''
'''读入：weibo.csv'''
'''输入：文件名，起止年份'''
'''输出：各统计图表'''
'''返回：'''
def get_all_statistical_data(csv_filename,start,end):
    data = get_data(csv_filename)
    year_data = clarify_by_year(data,end)
    year_data_by_month = {} # 按年排列一年统计数据
    whole_year_statistices_data = {}
    for year in range(start,end+1):
        try:
            ye = year_data[str(year)]
        except:
            print('No year ' + str(year) + ' values!')# 后期无数据全设成零
        else:
            year_data_by_month[str(year)], whole_year_statistices_data[str(year)] = get_months_statistical_data(ye,year)
            draw_one_year_pic(year_data_by_month[str(year)],year)
            print(str(year) + ' pics done!')

    draw_whole_year_pic(whole_year_statistices_data,start,end)

'''作出月数据的统计图'''
'''读入：'''
'''输入：字典形式月数据，年份'''
'''输出：月数据统计图'''
'''返回：'''
def draw_one_year_pic(dict_data,year):
    '''年月动态统计'''
    '''年微博平均字数统计'''
    '''年含图微博统计'''
    '''年评论统计'''
    '''年点赞统计'''
    one_year_bar_chart(str(year)+'年月动态统计',dict_data['blog_num'])
    one_year_bar_chart(str(year)+'年含图微博统计',dict_data['pic_blog_num'])
    one_year_bar_chart(str(year)+'年评论统计',dict_data['com_num'])
    if year > 2013:
        one_year_bar_chart(str(year)+'年点赞统计',dict_data['att_num'])
    
    ###'''待优化，对text正则后统计字数'''###
    if year >2015:
        one_year_bar_chart(str(year)+'年微博平均字数统计',dict_data['avg_word'])

'''作出年数据的统计图'''
'''读入：'''
'''输入：字典形式年数据，年份起止'''
'''输出：年数据统计图'''
'''返回：'''
def draw_whole_year_pic(dict_data, start, end):
    year_blog_num, year_word_num, year_retweet_num = [],[],[]
    year_pic_blog_num, year_com_num,  year_att_num = [],[],[]
    avg_word, avg_att,avg_com, orig_percent, ret_percent =[],[],[],[],[]
    
    for year in range(start,end+1):
        try:
            ye = dict_data[str(year)]
        except:
            year_blog_num.append(0)
            year_word_num.append(0)
            year_ret_num.append(0)
            year_pic_blog_num.append(0)
            year_com_num.append(0)
            year_att_num.append(0)
            print('No year ' + str(year) + ' values!')# 后期无数据全设成零
        else:
            year_blog_num.append(dict_data[str(year)]['year_blog_num'])
            year_word_num.append(dict_data[str(year)]['year_word_num'])
            year_retweet_num.append(dict_data[str(year)]['year_retweet_num'])
            year_pic_blog_num.append(dict_data[str(year)]['year_pic_blog_num'])
            year_com_num.append(dict_data[str(year)]['year_com_num'])
            year_att_num.append(dict_data[str(year)]['year_att_num'])

    for word,comment, attitude, retweet, number in zip(year_word_num,year_com_num,year_att_num,year_retweet_num,year_blog_num):
        if number == 0:
            avg_word.append(0)
            avg_com.append(0)
            avg_att.append(0)
            ret_percent.append(0)
        
        avg_att.append(round(attitude/number,0))
        avg_com.append(round(comment/number,0))
        avg_word.append(round(word/number,0))
        ret_percent.append(round(retweet/number*100,0))
        orig_percent.append(100 - round(retweet/number*100,0))

    '''年度动态统计'''
    year_bar_chart('年度动态统计',year_blog_num,start,end)
    '''年评论统计'''
    year_bar_chart('年评论统计',year_com_num,start,end)
    '''年平均评论统计'''
    year_bar_chart('年平均评论统计',avg_com,start,end)
    '''年点赞统计'''
    year_bar_chart('年点赞统计',year_att_num,start,end)
    '''年平均点赞统计'''
    year_bar_chart('年平均点赞统计',avg_att,start,end)
    '''年转发微博统计'''
    year_bar_chart('年转发微博统计',year_retweet_num,start,end)
    '''年字数微博统计'''
    year_bar_chart('年字数微博统计',year_word_num,start,end)
    '''年转发占比统计'''
    draw_stackedbar_chart('年转发占比统计',orig_percent,ret_percent,start,end)

'''作出终端的统计图'''
'''读入：weibo.csv微博数据'''
'''输入：文件名'''
'''输出：使用量前10终端数据统计图'''
'''返回：'''
def get_blog_source(csv_filename):
    data = get_data(csv_filename)
    source = {}
    for row in data:
        if row['source'] not in source:
            source[row['source']] = 1
        else:
            source[row['source']] = source[row['source']] + 1

    sorted_source = sorted(source.items(), key = lambda item:item[1], reverse=True)
    draw_source_bar_pic('发博终端统计',sorted_source[:10])
    fout = open('source.txt','w')
    print(sorted_source,file = fout)
    print('source get!')


# draw_one_year_pic(dict_data)
#data = get_data()

# fout = open('1.txt','w')
# print(year_data['2010'],file = fout)
if __name__ == '__main__':
    get_all_statistical_data(csv_filename,2016,2018)
    get_blog_source(csv_filename)