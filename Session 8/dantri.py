import requests 
from bs4 import BeautifulSoup
import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['c4e']
dantri_collection = db['dantri']


dantri_content = requests.get('https://dantri.com.vn/')

soup = BeautifulSoup(dantri_content.text, 'html.parser')
print(soup.prettify())

div_content = soup.find('div', {'class': 'xnano'})

ul_content = div_content.find('ul', {'class': 'ul1 ulnew'})
print(ul_content)
li_content = ul_content.find_all('li')
for li in li_content:
    news_title = str(li.h4.a.string).strip()
    news_link = li.h4.a['href']
    dantri_collection.insert_one({
        'title': news_title,
        'link': news_link,
    })