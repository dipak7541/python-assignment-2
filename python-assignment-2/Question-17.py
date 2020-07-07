
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        a=x/y
        return a
    except ZeroDivisionError:
        print("You can't divide by zero!")
    

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    a=int(input("Enter first Number"))
    b=int(input("Enter second Number"))
    choice=int(input("Enter your choice"))
    if choice>0 and choice <5 :
        if choice==1:
            result=add(a,b)
            print("Addition:{0}+{1}={2}".format(a,b,result))
        elif choice==2:
            result=subtract(a,b)
            print("Subtraction:{0}-{1}={2}".format(a,b,result))    
        elif choice==3:
            result=multiply(a,b)
            print("Multiplication:{0}*{1}={2}".format(a,b,result))
        else:
            result=divide(a,b)
            print("Division:{0}/{1}={2}".format(a,b,result))
    else:
        print("There are only four operations. Please select accordingly")
