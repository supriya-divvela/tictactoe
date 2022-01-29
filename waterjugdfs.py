import sys
def func(x,y):
    l=[(0,y),(x,0),(m,y),(x,n)]
    if (x+y)<=m and y>0:l.append((x+y,0))
    if (x+y)<=n and x>0:l.append((0,x+y))
    if (x+y)>=m and y>0:l.append((m,y-(m-x)))
    if (x+y)>=n and x>0:l.append((x-(n-y),n))
    return list(set(l))

cp,m,n,k,p=[],int(input()),int(input()),int(input()),int(input())
print("The path in DFS is:",end=" ")
def dfs(cl,x,y):
    cp.append((x,y))
    print((x,y),end=" ")
    if (x,y)==(k,p):sys.exit()
    for i in func(x,y):
        if i not in cp:
            dfs(cp,i[0],i[1])
dfs(cp,0,0)
