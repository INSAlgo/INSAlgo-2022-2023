x=[]
n = int(input())
for i in input().split():
    x.append(int(i))
x.sort()
cout=0
while len(x)!=1:
    c=x[1]
    x[0]+=c
    cout+=x[0]
    x.pop(1)
    x.sort()

print(cout)