G={}
def bfspath(G, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in G.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

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
p,q=map(int,input().split())
r,s=map(int,input().split())
v=[(p,q,1)]
h=[(r,s,0)]
s1=[(3,3,1)]
s2=[(0,0,0)]
c=0
while s1:
    m1,m2=s1.pop(0),s2.pop(0)
    t1,t2=fun(m1,m2)
    if m1 not in G.keys():
        G[m1]=[]
    for i,j in zip(t1,t2):
        if i not in G[m1]:
            G[m1].append(i)
    for i,j in zip(t1,t2):
        if i not in v:
            v.append(i)
            h.append(j)
            s1.append(i)
            s2.append(j)
print("The path in BFS is:")
for i in bfspath(G,(3,3,1),(0,0,0)):
    if i[2]==1:
        print("({},{},{}),({},{},0)".format(i[0],i[1],i[2],3-i[0],3-i[1]))
    else:
        print("({},{},{}),({},{},1)".format(i[0],i[1],i[2],3-i[0],3-i[1]))
