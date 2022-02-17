import sys
def fun(x,y):
    if x[2]==1:
        s=[(x[0]-2,x[1],0),(x[0]-1,x[1]-1,0),(x[0],x[1]-2,0),(x[0]-1,x[1],0),(x[0],x[1]-1,0)]
        r=[(y[0]+2,y[1],1),(y[0]+1,y[1]+1,1),(y[0],y[1]+2,1),(y[0]+1,y[1],1),(y[0],y[1]+1,1)]
    else:
        s=[(x[0]+2,x[1],1),(x[0]+1,x[1]+1,1),(x[0],x[1]+2,1),(x[0]+1,x[1],1),(x[0],x[1]+1,1)]
        r=[(y[0]-2,y[1],0),(y[0]-1,y[1]-1,0),(y[0],y[1]-2,0),(y[0]-1,y[1],0),(y[0],y[1]-1,0)]
    x1,x2=[],[]
    for i,j in zip(s,r):
        if f(i,j):
            x1.append(i)
            x2.append(j)
    return x1,x2
def f(p,q):
    if p not in v:
        if p[0]>=0 and p[1]>=0 and q[0]>=0 and q[1]>=0:
            if (p[0]==0 and q[1]==0) or (p[1]==0 and q[0]==0):
                return True
            elif p[0]==0 or p[1]==0:
                if q[0]>=q[1]:return True
                else:return False
            elif q[0]==0 or q[1]==0:
                if p[0]>=p[1]:return True
                else:return False
            elif p[0]>0 and p[1]>0 and p[0]>=p[1]:
                if q[0]>=q[1]:return True
                else:return False
            elif q[0]>0 and q[1]>0 and q[0]>=q[1]:
                if p[0]>=p[1]:return True
                else:return False
            else:return False
        else:return False
    else:return False
v,h=[],[]
def dfs(v,x,y):
    v.append(x)
    h.append(y)
    if x[2]==0:
        print("{},({},{},1)".format(x,3-x[0],3-x[1]))
    else:
        print("{},({},{},0)".format(x,3-x[0],3-x[1]))
    if x==(0,0,0):sys.exit()
    t1,t2=fun(x,y)
    for i,j in zip(t1,t2):
        if i not in v:
            dfs(v,i,j)
print("The path in dfs is:")
dfs(v,(3,3,1),(0,0,0))
