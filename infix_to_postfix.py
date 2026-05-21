def prec(op):
    if op == '$' or op == '^':
        return 4
    elif op == '*' or op == '/':
        return 3
    elif op == '+' or op == '-':
        return 2
    else:
        return 0
l = [5, '+', '(', 10, '-', 2, ')', '*', 3]
op = ['+', '-', '*', '/', '%']
p = []
stk = ['(']

for i in l:
    if i in op:
        if prec(i) > prec(stk[-1]):
            stk.append(i)
        else:
            while stk[-1] != '(':
                a = stk.pop()
                p.append(a)
            stk.append(i)
    elif i == '(':
        stk.append(i)
    elif i == ')':
        while stk[-1] != '(':
            a = stk.pop()
            p.append(a)
        stk.pop()
    else:
        p.append(i)
while len(stk) > 1:
    p.append(stk.pop())

print(p)