import sys,re

counter=0
for _ in range(int(input())):
    if re.search(r"\d{5}$",input()):
        counter+=1
        
print(counter)
