import csv
reader = csv.DictReader(open('allofus.csv', 'r'))
dict_list=[]
for line in reader:
    dict_list.append(line)
print(dict_list)
