from itertools import combinations

x=int(input())
str=input()
k=int(input())

list=str.split(" ")
c=0
total=0
for i in combinations(list, k):
    if "a" in i:
        c += 1
    total += 1
    
result=c/total  
print(result)
