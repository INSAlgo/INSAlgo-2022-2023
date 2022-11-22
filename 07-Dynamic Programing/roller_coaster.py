L, C, N = [int(i) for i in input().split()]
File = []
for i in range(N):
    Pi = int(input())
    File.append(Pi)

memo = [[]] * N
sortie = 0
index = 0
while C > 0:
    save_i = index
    if len(memo[index]) != 0:
        sortie+=memo[index][1]
        index = memo[index][0]
    else:
        revenu = 0
        while revenu+File[index]<=L:
            revenu+=File[index]
            if(index>=N-1):
                index = 0
            else:
                index+=1
            if index == save_i:
                break
        sortie+=revenu
        memo[save_i] = [index, revenu]
    C-=1
print(sortie)
