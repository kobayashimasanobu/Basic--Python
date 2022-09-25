while True:
    a,op,b = input().split()
    if op=='?':
        break
    a,b=int(a),int(b)
    if op=="+":
        ans = a + b
    elif op=="-":
        ans = a - b
    elif op=="*":
        ans = a * b
    else:
        ans = a // b
    print(ans)