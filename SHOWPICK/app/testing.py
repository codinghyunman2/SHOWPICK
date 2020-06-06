import csv

with open('./data/store.csv', newline='', encoding = "euc-kr") as csvfile:
       data = list(csv.reader(csvfile))

semi_big_category = []
for semi in range(1, len(data)):
    semi_big_category.append(data[semi][0])

set_semi_big_category = set(semi_big_category)


print(set_semi_big_category)




# for i in range(0,Setlength):
#     exec("Big_category_"+str(i)+"= Big_category()")
#     exec("Big_category_"+str(i)+".category=" SetLegnth(i))



