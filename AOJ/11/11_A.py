n = list(map(int,input().split()))
dire = input()

def roll(a,b,c,d,e,f,G):
    if G=="E":
        return[d,b,a,f,e,c]
    elif G=="N":
        return[b,f,c,d,a,e]
    elif G=="S":
        return[e,a,c,d,f,b]
    elif G=="W":
        return[c,b,f,a,e,d]
for i in range(len(dire)):
    [n[0],n[1],n[2],n[3],n[4],n[5]]=roll(n[0],n[1],n[2],n[3],n[4],n[5],dire[i])
print(n[0])