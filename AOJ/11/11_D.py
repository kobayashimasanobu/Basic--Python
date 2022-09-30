def rota(A,B,N):
    def roll(a,b,c,d,e,f,G):
        if G=="E":return[d,b,a,f,e,c]
        elif G=="N":return[b,f,c,d,a,e]
        elif G=="S":return[e,a,c,d,f,b]
        elif G=="W":return[c,b,f,a,e,d]

    def conf(A,B,C):
        C=[]
        if A[5]!=B[5]:C.append(0);return C
        elif A[1]==B[1] and A[2]==B[2] and A[3]==B[3] and A[4]==B[4]:
            C.append(1);return C
        elif A[1]==B[2] and A[2]==B[4] and A[3]==B[1] and A[4]==B[3]:
            C.append(1);return C
        elif A[1]==B[3] and A[2]==B[1] and A[3]==B[4] and A[4]==B[2]:
            C.append(1);return C
        elif A[1]==B[4] and A[2]==B[3] and A[3]==B[2] and A[4]==B[1]:
            C.append(1);return C
        else:C.append(0);return C
        
    ans=[]
    C=[]
    if A[0]==B[0]:ans+=conf(A,B,C)       
    if A[0]==B[1]:B=roll(B[0],B[1],B[2],B[3],B[4],B[5],"N");ans+=conf(A,B,C)
    if A[0]==B[2]:B=roll(B[0],B[1],B[2],B[3],B[4],B[5],"W");ans+=conf(A,B,C)
    if A[0]==B[3]:B=roll(B[0],B[1],B[2],B[3],B[4],B[5],"E");ans+=conf(A,B,C)
    if A[0]==B[4]:B=roll(B[0],B[1],B[2],B[3],B[4],B[5],"S");ans+=conf(A,B,C)
    if A[0]==B[5]:
        B=roll(B[0],B[1],B[2],B[3],B[4],B[5],"N")
        B=roll(B[0],B[1],B[2],B[3],B[4],B[5],"N")
        ans+=conf(A,B,C)
    N=[]
    if 1 in ans:
        N.append(1)
        return N
    else:
        N.append(0)
        return N

n = int(input())
a=[[0]*6 for i in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
f_ans=[]
for i in range(n-1):
    for k in range(i+1,n):
        f_ans+=rota(a[i],a[k],f_ans)
if 1 in f_ans:
    print("No")
else:
    print("Yes")
