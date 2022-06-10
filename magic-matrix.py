#last commit was wrong, i promise this one's good

def is_magic(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)


    sumd1=0
    sumd2=0
    for i in range(n):
        sumd1+=matrix[i][i]
        sumd2+=matrix[i][n-i-1]
    if not(sumd1==sumd2):
        return False
    for i in range(n):
        sumr=0
        sumc=0
        for j in range(n):
            sumr+=matrix[i][j]
            sumc+=matrix[j][i]
        if not(sumr==sumc==sumd1):
            return False
        else:
            return True
    
    


n=int(input())
if(is_magic(n)==True):


