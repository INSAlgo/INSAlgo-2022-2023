from collections import defaultdict,Counter


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    print(lines)
    return lines


def firstProblem(lines: list[str]):
    insertionDict = defaultdict(str)

    polymer = lines[0]

    for i in range(2,len(lines)):
        pattern,insert=lines[i].split(" -> ")
        insertionDict[pattern]+=insert

    for _ in range(10):
        newPolymer=""

        for letterPos in range(1,len(polymer)):

            insert= polymer[letterPos-1]+insertionDict[polymer[letterPos-1]+polymer[letterPos]]
            newPolymer+=insert
        newPolymer+=polymer[-1]
        polymer=newPolymer

    c=Counter(polymer)
    print(c.most_common()[0][1]-c.most_common()[-1][1])

    return

# # numOfLetter count the number of letter that will be inserted in the end when we are at step
# # it also count letter L1 but not letter L2
# def numOfLetter(step,L1,L2,insertDict):
#     global gDataMem
#     if step==numberOfSteps or L1=="":
#         return Counter(L1)
#     elif L2=="":
#         return Counter()
#     else:
#         if L1+L2 not in gDataMem[step]:
#             gDataMem[step][L1 + L2]=numOfLetter(step+1,L1,insertDict[L1+L2],insertDict)+numOfLetter(step+1,insertDict[L1+L2],L2,insertDict)
#         return gDataMem[step][L1+L2]


# def secondProblem(lines: list[str]):
#     insertionDict = defaultdict(str)
#     global numberOfSteps
#     numberOfSteps = 40
#     polymer = lines[0]

#     for i in range(2, len(lines)):
#         pattern, insert = lines[i].split(" -> ")
#         insertionDict[pattern] += insert

#     print(insertionDict)

#     global gDataMem
#     gDataMem = [dict() for _ in range(numberOfSteps)]

#     c=Counter()
#     for letterPos in range(1, len(polymer)):
#         if polymer[letterPos - 1] + polymer[letterPos] not in gDataMem[0]:
#             numOfLetter(0, polymer[letterPos - 1],polymer[letterPos], insertionDict)
#         c+=gDataMem[0][polymer[letterPos - 1] + polymer[letterPos]]
#     c[polymer[-1]]+=1

#     return c.most_common()[0][1]-c.most_common()[-1][1]


if __name__ == "__main__":
    lines = read("14input.txt")
    firstProblem(lines)
    # secondProblem(lines)
