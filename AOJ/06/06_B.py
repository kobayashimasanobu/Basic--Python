n = int(input())
l=[]
for fa in range(n):
    A,a = input().split()
    a=int(a)
    if A=="S":
        l.append(a)
    elif A=="H":
        l.append(a+13)
    elif A=="C":
        l.append(a+26)
    elif A=="D":
        l.append(a+39)
i=1
for fb in range(52):
    if i not in l:
        if 1<=i<=13:
            print("S %d"%i)
        elif 14<=i<=26:
            print("H %d"%(i-13))
        elif 27<=i<=39:
            print("C %d"%(i-26))
        elif 40<=i<=52:
            print("D %d"%(i-39))
    i+=1