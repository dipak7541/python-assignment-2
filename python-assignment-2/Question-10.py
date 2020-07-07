def camel_to_snake(string):
    res=[string[0].lower()]
    for char in string[1:]:
        if char.isupper()==True:
            res.append('_') 
            res.append(char.lower())
        else:
            res.append(char)
    
    snakeresult=''.join(res)
    snakeresult=snakeresult.replace("camel","snake")
    kebabresult=snakeresult.replace('_','-')
    kebabresult=kebabresult.replace("snake","kebab")
    print(snakeresult)
    print(kebabresult)

if __name__=="__main__":
    camel_to_snake("ThisIsCamelCased")
