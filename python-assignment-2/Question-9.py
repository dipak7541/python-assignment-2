def binary_search(list, low, high, key):  
    if high >= low: 
        mid = (high + low) // 2 
        if list[mid] == key: 
            return mid
        elif list[mid] > key: 
            return binary_search(list, low, mid - 1, x) 
        else: 
            return binary_search(list, mid + 1, high, x) 
    else:  
        return -1
   
my_list = [2,3,4,10,40] 
x = 10 
res = binary_search(my_list, 0, len(my_list)-1, x)  
if res!= -1: 
    print("Element is present at index", str(res)) 
else: 
    print("Element is not present in array") 
