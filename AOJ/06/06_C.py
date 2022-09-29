n = int(input())
room=[[[0]*10 for x in range(3)]for y in range(4)]
for a in range(n):
    b,f,r,v = map(int,input().split())
    room[b-1][f-1][r-1]+=v

for a in range(4):
    for b in range(3):
        for c in range(10):
            print(" %d"%room[a][b][c],end="")
            if c==9:
                print()
        if b==2 and a!=3:
            print("#"*20)
            