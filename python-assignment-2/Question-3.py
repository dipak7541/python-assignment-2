def check_arams(string):
    temp=""
    dct = {} 
    words=string.split(" ")
    words=sorted(words,key=len) 
    for element in words: 
        if len(element) not in dct: 
            dct[len(element)] = [element] 
        elif len(element) in dct: 
            dct[len(element)] += [element] 
    res = [] 
    for key in sorted(dct): 
        res.append(dct[key])
    all_freq = {}
    second={}
    for word in res:
        if len(word)!=1:
            for i in word:
                for j in range(0,len(i)):
                    if word[i]==0:
                        if i[j] in all_freq:
                            all_freq[i[j]] += 1
                        else:
                            all_freq[i[j]] = 1
                    else:
                        if i[j] in all_freq:
                            second[i[j]] += 1
                        else:
                            second[i[j]] = 1  
                print(all_freq)
                print(second)
    
    return res
    
print(check_arams("hello sirs hsssow ares you"))
