#list, danh sach, array, mang

places = ["Dai su quan","Benh vien", "Bai bien"] #initialize
print(places) # Read
new_place = input("enter new place plzzzz: ")
places.append(new_place) #create
replace_index = places.index("Benh vien")
places[replace_index] = "Tau khong gian" #update
#places.pop(2) #pop khong co so thi se xoa thang cuoi cung #delete
places[0] = "Don canh sat"
#places.pop() # DELETE BY INDEX ko dien so thi delete cai cuoi
places.remove("Dai su quan") #DELETE BY VALUE
temp = places[0]
places[0] = places[1]
places[1] = temp

for i in range(len(places)):
    print(places[i])
print(places)

#ICRUD