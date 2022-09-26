a,b = map(int,input().split())
while a!=0 or b!=0:
    if a<=b:
        print("%d %d" %(a,b))
    else:
        print("%d %d" %(b,a))
    a,b = map(int,input().split())