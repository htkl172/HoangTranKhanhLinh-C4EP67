import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e', retryWrites = False)
db = client['c4e']
customer_collection = db['customers']
post_collection = db['posts']

# EXERCISE 2
new_data ={
        "title": "Phố cổ",
        "author": "Tin's waifuuu",
        "content": "Phố khuya màn mưa chưa nhạt nhoà từng tên đường, con phố. Tiếng rao nửa đêm nghe thật buồn, bàn chân người lãng du. Tàu điện leng keng leng keng, vội vã, chở người đi xa đi xa không về. Thoáng qua ngày mưa âm thầm nhớ, những nỗi nhớ nào về em còn. Phố khuya tìm em chưa lạnh lùng, tìm tôi vừa ấm áp. Giữa đông ngựa xe qua mặt người, lạnh run từng phím mơ. Tình đầu đi qua đi qua vội vã, người tình đi xa đi xa, không về. Phố quên màu rêu xanh cỏ lá, tóc buông xoã bờ vai trắng thề đón đưa. Phố cổ ngày thưa thớt bóng người, tất cả kề bên phố lên đèn.…"
    }
post_collection.insert_one(new_data)

# EXERCISE 3
events_count = customer_collection.count_documents({'ref': 'events'})
print(events_count)
ads_count = customer_collection.count_documents({'ref': 'ads'})
print(ads_count)
wom_count = customer_collection.count_documents({'ref': 'wom'})
print(wom_count)
print((events_count + ads_count + wom_count))

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

plot_labels = ['Events', 'Advertisement', 'Word of Mouth']
plot_data = [events_count, ads_count, wom_count]
pyplot.pie(plot_data, labels = plot_labels, autopct = '%.1f%%', shadow = True)
pyplot.axis('equal')
pyplot.title('Percentage of each reference')
pyplot.show()