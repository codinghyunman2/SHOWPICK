import csv


with open('/mnt/c/Users/User/Programming/NEXT_LION/Idea-Hackerton/Hacekrton-1430/SHOWPICK/app/data/store.csv', newline='', encoding = "euc-kr") as csvfile:
    csv_data = list(csv.reader(csvfile))

semi_big_category = []

for semi in range(1, len(csv_data)):
    semi_big_category.append(csv_data[semi][0])
set_semi_big_category = set(semi_big_category)

for i in set_semi_big_category:

    Temporary_Big_Category.objects.create(
        title = i
    )

def func_big_category():
    return Temporary_Big_Category

