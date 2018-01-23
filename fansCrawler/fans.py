import json
import csv

def get_one_card_fans(card,page):
    fans_info = {}
    fans_info['page'] = page
    #fans_info['desc1'] = card['desc1']
    user = card['user']
    fans_info['id'] = user['id']
    fans_info['name'] = user['screen_name']
    fans_info['followers'] = user['followers_count']
    fans_info['follow'] = user['follow_count']
    fans_info['description'] = user['description']
    if user['gender'] == 'f':
        fans_info['gender'] = 0
    elif user['gender'] == 'm':
        fans_info['gender'] = 1
    else:
        fans_info['gender'] = None

    return fans_info


# fw = open('fans.txt','w',encoding = 'utf-8') 
# f = open('fans2.json','rb')
def get_one_page_fans(data,page):
    fcsv = open('fans.csv','a',encoding = 'utf-8',newline = '') 
    fieldnames = ['id','name','description','follow','followers','gender','page']
    Data = json.loads(data)
    # Data = json.load(f)
    data = Data['data']
    cards = data['cards']
    card_group = cards[0]['card_group']

    writer = csv.DictWriter(fcsv, fieldnames=fieldnames)
    for card in card_group:
        if 'user' in card:
            #print(card)
            writer.writerow(get_one_card_fans(card,page))
        else:
            print('no user in this card')

    
    print('Page '+ str(page) +' Done!')

# get_one_page_fans(f,2)