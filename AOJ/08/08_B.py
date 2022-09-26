while True:
    a = int(input())
    if a == 0:
        break
    ans = 0
    for f in range(len(str(a))):
        ans += a%10
        a//=10    
    print(ans)