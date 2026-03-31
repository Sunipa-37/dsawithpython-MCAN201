name=input("enter your name:").lower()
d={}
j=[]
vowel=['a','e','i','o','u']
for i in name:
    if i in vowel:
        if i in j:
            d[i]=d[i]+1
        else:
            d[i]=1
            j.append(i)
print(d)