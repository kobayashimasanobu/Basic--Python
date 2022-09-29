Da = list(map(int,input().split()))
Db = list(map(int,input().split()))

def coll(A,B):
    if set(A)==set(B):
        C = list(set(A))
        for i in range(len(C)):
            if A.count(C[i])==B.count(C[i]):continue
            else:A = [-1]*6
        return(A,B)
    else:A = [-1]*6;return(A,B)

def rota(A,B):
    def roll(a,b,c,d,e,f,G):
        if G=="E":return[d,b,a,f,e,c]
        elif G=="N":return[b,f,c,d,a,e]
        elif G=="S":return[e,a,c,d,f,b]
        elif G=="W":return[c,b,f,a,e,d]

    def conf(A,B,C):
        C=[]
        if A[5]!=B[5]:C.append(0);return C
        elif A[1]==B[1] and A[2]==B[2] and A[3]==B[3]:C.append(1);return C
        elif A[1]==B[2] and A[2]==B[4] and A[3]==B[1]:C.append(1);return C
        elif A[1]==B[3] and A[2]==B[1] and A[3]==B[4]:C.append(1);return C
        elif A[1]==B[4] and A[2]==B[3] and A[3]==B[2]:C.append(1);return C
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
    if 1 in ans:
        return print("Yes")
    else:
        return print("No")

if -1 in coll(Da,Db):
    print("No")
else:
    rota(Da,Db)
