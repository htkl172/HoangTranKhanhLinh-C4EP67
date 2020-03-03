import requests
from bs4 import BeautifulSoup
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')


db = client['c4e']
kpop = db['kpop_database']

kpop_content = requests.get('https://dbkpop.com/db/all-k-pop-idols')

soup=BeautifulSoup(kpop_content.text,'html.parser')

#html_file = open("kpop.html","w")
#html_file.write(soup.prettify())
#html_file.close()

div_table_content = soup.find('tbody')

tr_content = div_table_content.find_all('tr') #list
idol_list=[]
for tr in tr_content:
    td_content = tr.find_all('td')
    idol_info=[]
    for td in td_content: 
        idol_info.append(td.string)
    idol_list.append(idol_info)

for i in idol_list:
    kpop.insert_one({
        'Stage name': i[1],
        'Korean name': i[4],
        'DOB': i[5],
        'POB': i[7]
    })

#    print(li.h4.a['href'])
#    news_link = li.h4.a['href']
#    news_title = li.h4.a.string.strip()
#    dantri_collection.insert_one({
#        'title':news_title,
#        'link':news_link
# })
#print(news_link,news_title)