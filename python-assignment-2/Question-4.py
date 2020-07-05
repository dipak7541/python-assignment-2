names=['ram','sita']
print(id(names))
names.append('harry')
names.append('Jaunty')
print(names)
print(id(names))

names.sort()
print(names)
print(names[0])
print(names[-1])


140321359374144
['ram', 'sita', 'harry', 'Jaunty']
140321359374144
['Jaunty', 'harry', 'ram', 'sita']
Jaunty
sita
