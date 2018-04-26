from collections import Counter
import jieba.analyse
import csv

#filename = 'z2017.csv'
def fenci(input_data,out_path):
    data = jieba.cut(input_data)
    data = dict(Counter(data))
    data = sorted(data.items(), key = lambda item:item[1],reverse = True)

    result_path = out_path
    with open(result_path,'w',encoding = 'utf-8') as fw:
        for k,v in data:
            fw.write("%s,%d\n" % (k,v))

    print('FenCi: ' + out_path + ' Done!')