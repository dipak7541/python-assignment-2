import csv
mytuple=("Tanka",'Tilottama-6',22)
friend1=('Dipak','ChunniPakha-4',23)
friend2=('Jaunty',"Chapakot-1",21)
allofus=[]
allofus.append(mytuple)
allofus.append(friend1)
allofus.append(friend2)
file = open('allofus.csv', 'w+', newline ='')

with file:
    header = ['Name', 'Address', 'Age'] 
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()
    write = csv.writer(file) 
    write.writerows(allofus)
