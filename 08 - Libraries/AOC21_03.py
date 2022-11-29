from collections import Counter


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    print(lines)
    return lines


def firstProblem(lines: list[str]):
    gammaRate = ""
    epsilonRate = ""
    for i in range(len(lines[0])):
        digit = Counter([line[i] for line in lines]).most_common(1)[0][0]
        gammaRate += digit
        epsilonRate += str(1 - int(digit))
    print(int(gammaRate, 2) * int(epsilonRate, 2))
    return


# def secondProblem(lines: list[str]):

#     O2Rating=""
#     CO2Rating = ""

#     candidates = lines.copy()
#     for i in range(len(lines[0])):

#         digit = mostCommun(candidates, i)
#         candidates = [line for line in candidates if line[i] == digit]
#         print(i, digit, len(candidates), candidates)

#         if len(candidates) == 1:
#             O2Rating = candidates[0]
#             break

#     candidates = lines.copy()
#     for i in range(len(lines[0])):

#         digit = mostCommun(candidates, i)
#         candidates = [line for line in candidates if line[i] != digit]
#         print(i, digit, len(candidates), candidates)

#         if len(candidates) == 1:
#             CO2Rating = candidates[0]
#             break

#     print(O2Rating, CO2Rating)
#     print(int(O2Rating, 2) * int(CO2Rating, 2))

#     return


# def mostCommun(l: list[str], i: int) -> str:

#     num0 = 0
#     num1 = 0
#     for elem in l:
#         if elem[i] == "0":
#             num0 += 1
#         else:
#             num1 += 1

#     if num0 > num1:
#         return "0"
#     else:
#         return "1"


if __name__ == "__main__":
    lines = read("03input.txt")
    firstProblem(lines)
    # secondProblem(lines)
