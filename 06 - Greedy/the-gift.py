n = int(input())
c = int(input())
b=[]
for i in range(n):
    b.append(int(input()))
b.sort()

if(sum(b)<c):
    print("IMPOSSIBLE")

else :
    for i in range(len(b)):
        lastcontribution=min(b[i],c//(n-i))
        c-=lastcontribution
        print(lastcontribution)