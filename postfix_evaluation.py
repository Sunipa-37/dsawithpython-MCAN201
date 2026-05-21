def calc(b,i,a):
    if i == '+':
        c=b+a
    elif i =='-':c=b-a
    elif i == '/':c=b/a
    elif i == '*':c=b*a
    elif i == '^' or i=='$':c=b**a
    else:
        return"invali"

    return c
#l=[5, 10, 2, '-', 3, '*', '+']
l=[5,6,2,'+','*',12,4,'/','-']
op=['+','-','*','/','^','$']
stk=[]
for i in l:
    if i in op:
        a=stk.pop()
        b=stk.pop()
        c=calc(b,i,a)
        stk.append(c)
    else:
        pass
        stk.append(i)

print(stk)