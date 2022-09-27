l=input().split()
a=float(l[0])
b=float(l[1])
t=l[2]
if t=='Addition':
    print(a+b)
elif t=='Subtraction':
    print(a-b)
elif t=='Multiplication':
    print(a*b)
elif t=='Division':
    print(a/b)