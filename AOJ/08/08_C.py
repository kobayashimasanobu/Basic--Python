abc = [0]*26
while True:
    try:
        ABC = input().lower()
    except:
        break
    for i in range(len(ABC)):
        n = ord(ABC[i]) - ord("a")
        if (n>=0 and n<26):
            abc[n]+=1
for i in range(26):
    print("%s : %d"%(chr(i+97),abc[i]))