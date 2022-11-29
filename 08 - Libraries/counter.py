from collections import Counter
input()
daPrice = 0
daList = list(map(int, input().split()))
daCount = Counter(daList)
N = int(input())
for i in range(N):
    daClient = list(map(int,input().split()))
    if(daCount.get(daClient[0])!=None and daCount.get(daClient[0])>0):
        daCount.update({daClient[0]:-1}) # for the key "daClient[0]", remove 1 from value
        daPrice += daClient[1]
    
print(daPrice)
