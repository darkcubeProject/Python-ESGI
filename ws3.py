import random

def gen_pos(n=5):
    
    max = n ** 2
    found = 0
    items = {i:0 for i in range (max)}
    while found < n:
        x= random.randint(0, max-1)
        if items[x]==0:
            items[x] = 1
            found += 1
    return items

def flatten (row,col,n=5):
    return row * n + col

def expand (x,n=5):
    return(x//n,x%n)

def check_pos(echiquier, row, col, n):
    for i in range(row):
        if echiquier[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if echiquier[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if echiquier[i][j] == 1:
            return False
    return True

position_dame = ['2','8','11','16','23']

