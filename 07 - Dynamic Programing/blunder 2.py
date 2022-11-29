class Salle:
    def __init__(self, val, v1, v2):
        self.val = val
        self.v1 = v1
        self.v2 = v2

def getSalle(memo, salles, n):
    val_salle = memo[n]
    if val_salle != -1:
        return val_salle
    else:
        salle = salles[n]
        v1_val = v2_val = 0
        if salle.v1 == -1:
            v1_val = salle.val
        else:
            v1_val = salle.val + getSalle(memo, salles, salle.v1)
        if salle.v2 == -1:
            v2_val = salle.val
        else:
            v2_val = salle.val + getSalle(memo, salles, salle.v2)
        val_salle = max(v1_val, v2_val)
        memo[n] = val_salle
    return val_salle

n = int(input())
memo = [-1] *n
salles = [Salle(-1, -1, -1)]*n
for _ in range(n):
    i, val, v1, v2 = [-1 if (j=='E') else int(j) for j in input().split(" ")]
    salles[i] = Salle(val, v1, v2)
print(getSalle(memo, salles, 0))

