names=['Nikhil','Sumit','Santosh','Dipak','John']
found=False
for name in names:
    if name=='John':
        found=True
    else:
        found=False
if found==True:
    print('john in the list')
else:
    print('not found')
