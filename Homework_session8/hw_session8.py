import requests
from bs4 import BeautifulSoup

web_content = requests.get("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")

soup = BeautifulSoup(web_content.text, "html.parser")

table_content = soup.find('table', {'id': 'tableContent'})

tr_content = table_content.find_all('tr')

data_list=[]
for tr in tr_content:
    td_content = tr.find_all('td')
    data_info=[]
    for td in td_content: 
        data_info.append(td.text.strip())
    for info in data_info:
        if info == '':
            data_info.remove(info)
    if len(data_info) > 6:
        data_list.append(data_info)    
# print(data_list)

import pyexcel as p
table_data = []
for i in data_list:
    records = {
    '': i[0],
    'Quý 3-2017': i[4],
    'Quý 1-2017': i[2],
    'Quý 2-2017': i[3],
    'Quý 1-2016': i[1]
    }
    table_data.append(records)
print(table_data)

p.save_as(records = table_data, dest_file_name='hw_session8.xlsx')

