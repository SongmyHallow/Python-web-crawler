import os,shutil
import json
import re

business_file =open('business.json',encoding="utf8")
photo_file = open('photo.json',encoding="utf8")

business_outfile = open('business_id.txt','w+')
photo_idfile = open('photo_id.txt','w+')
photo_menufile = open('photo_menu_id.txt','w+')
photo_foodfile = open('photo_food_id.txt','w+')
photo_drinkfile = open('photo_drink_id.txt','w+')
photo_insidefile = open('photo_inside_id.txt','w+')
photo_outsidefile = open('photo_outside_id.txt','w+')

pattern1 = 'Restaurants'
pattern2 = re.compile(r'\bJuice\b | \bSalad\b', flags=re.I | re.X)

target_id_dic = {}

for business in business_file:
    setting = json.loads(business)
    categories = setting['categories']
    if(re.search(pattern2, str(setting['categories']))):
        business_outfile.write(str(setting['business_id'])+'\n')
        target_id_dic[str(setting['business_id'])] = []

for photo in photo_file:
    photo_profile = json.loads(photo)
    if(str(photo_profile['business_id']) in target_id_dic.keys()):
        target_id_dic[str(photo_profile['business_id'])].append(str(photo_profile['photo_id']))
        photo_idfile.write(str(photo_profile['photo_id'])+'\t'+str(photo_profile['label'])+'\n')
        if(str(photo_profile['label']) == 'menu'):
            photo_menufile.write(str(photo_profile['photo_id'])+'\n')
            try:
                shutil.copy('C:\\Users\\tjuso\\Downloads\\yelp\\photos\\'+str(photo_profile['photo_id'])+'.jpg','C:\\Users\\tjuso\\Downloads\\yelp\\menu')
            except:
                print('Menu file does not exist:'+str(photo_profile['photo_id']+'.jpg'))
        elif(str(photo_profile['label']) == 'food'):
            photo_foodfile.write(str(photo_profile['photo_id'])+'\n')
            try:
                shutil.copy('C:\\Users\\tjuso\\Downloads\\yelp\\photos\\'+str(photo_profile['photo_id'])+'.jpg','C:\\Users\\tjuso\\Downloads\\yelp\\food')
            except:
                print('Food file does not exist:'+str(photo_profile['photo_id']+'.jpg'))
        elif(str(photo_profile['label']) == 'drink'):
            photo_drinkfile.write(str(photo_profile['photo_id'])+'\n')
            try:
                shutil.copy('C:\\Users\\tjuso\\Downloads\\yelp\\photos\\'+str(photo_profile['photo_id'])+'.jpg','C:\\Users\\tjuso\\Downloads\\yelp\\drink')
            except:
                print('Drink file does not exist:'+str(photo_profile['photo_id']+'.jpg'))
        elif(str(photo_profile['label']) == 'inside'):
            photo_insidefile.write(str(photo_profile['photo_id'])+'\n')
            try:
                shutil.copy('C:\\Users\\tjuso\\Downloads\\yelp\\photos\\'+str(photo_profile['photo_id'])+'.jpg','C:\\Users\\tjuso\\Downloads\\yelp\\inside')
            except:
                print('Inside file does not exist:'+str(photo_profile['photo_id']+'.jpg'))
        elif(str(photo_profile['label']) == 'outside'):
            photo_outsidefile.write(str(photo_profile['photo_id'])+'\n')
            try:
                shutil.copy('C:\\Users\\tjuso\\Downloads\\yelp\\photos\\'+str(photo_profile['photo_id'])+'.jpg','C:\\Users\\tjuso\\Downloads\\yelp\\outside')
            except:
                print('Outside file does not exist:'+str(photo_profile['photo_id']+'.jpg'))
        else:
            pass

business_file.close()
photo_file.close()

business_outfile.close()
photo_idfile.close()
photo_menufile.close()
photo_foodfile.close()
photo_drinkfile.close()