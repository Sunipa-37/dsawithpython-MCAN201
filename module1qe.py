def fun(sen1):
    r=sen1[0]
    
    for i in sen1[1:]:
        print(r[-1])
        if i==r[-1]:
            r+='*'
        else:
            r+=i
    return r
sen1=input("enter a sentence:")
print(fun(sen1))