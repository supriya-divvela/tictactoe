from itertools import product
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

def fun(e,x,y):
    s=[]
    r=[]
    if x[2]==1:
        for i in e:
            s.append((x[0]-i[0],x[1]-i[1],0))
            r.append((y[0]+i[0],y[1]+i[1],1))
    else:
        for i in e:
            s.append((x[0]+i[0],x[1]+i[1],1))
            r.append((y[0]-i[0],y[1]-i[1],0))
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
n=int(input())
for i in range(4,n):
    temp=i
    G={}
    e=list(filter(lambda x:sum(x)<i+1,list(product(list(range(i+1)),repeat=2))))
    e.remove((0,0))
    v=[(n,n,1)]
    h=[(0,0,0)]
    s1=[(n,n,1)]
    s2=[(0,0,0)]
    c=0
    while s1:
        m1,m2=s1.pop(0),s2.pop(0)
        t1,t2=fun(e,m1,m2)
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
    print(f"The path in BFS if boat capaticy is {temp}:")
    for i in bfspath(G,(n,n,1),(0,0,0)):
        if i[2]==1:
            print("({},{},{}),({},{},0)".format(i[0],i[1],i[2],n-i[0],n-i[1]))
        else:
            print("({},{},{}),({},{},1)".format(i[0],i[1],i[2],n-i[0],n-i[1]))
    print()

'''
input:11
output:
The path in BFS if boat capaticy is 4:
(11,11,1),(0,0,0)
(11,9,0),(0,2,1)
(11,10,1),(0,1,0)
(11,6,0),(0,5,1)
(11,7,1),(0,4,0)
(7,7,0),(4,4,1)
(8,8,1),(3,3,0)
(6,6,0),(5,5,1)
(7,7,1),(4,4,0)
(5,5,0),(6,6,1)
(6,6,1),(5,5,0)
(4,4,0),(7,7,1)
(5,5,1),(6,6,0)
(3,3,0),(8,8,1)
(4,4,1),(7,7,0)
(2,2,0),(9,9,1)
(3,3,1),(8,8,0)
(1,1,0),(10,10,1)
(2,2,1),(9,9,0)
(0,0,0),(11,11,1)

The path in BFS if boat capaticy is 5:
(11,11,1),(0,0,0)
(11,9,0),(0,2,1)
(11,10,1),(0,1,0)
(11,5,0),(0,6,1)
(11,6,1),(0,5,0)
(6,6,0),(5,5,1)
(7,7,1),(4,4,0)
(5,5,0),(6,6,1)
(6,6,1),(5,5,0)
(4,4,0),(7,7,1)
(5,5,1),(6,6,0)
(3,3,0),(8,8,1)
(4,4,1),(7,7,0)
(0,4,0),(11,7,1)
(0,5,1),(11,6,0)
(0,0,0),(11,11,1)

The path in BFS if boat capaticy is 6:
(11,11,1),(0,0,0)
(11,6,0),(0,5,1)
(11,7,1),(0,4,0)
(6,6,0),(5,5,1)
(7,7,1),(4,4,0)
(4,4,0),(7,7,1)
(5,5,1),(6,6,0)
(2,2,0),(9,9,1)
(3,3,1),(8,8,0)
(0,0,0),(11,11,1)

The path in BFS if boat capaticy is 7:
(11,11,1),(0,0,0)
(11,5,0),(0,6,1)
(11,6,1),(0,5,0)
(5,5,0),(6,6,1)
(6,6,1),(5,5,0)
(0,6,0),(11,5,1)
(0,7,1),(11,4,0)
(0,0,0),(11,11,1)

The path in BFS if boat capaticy is 8:
(11,11,1),(0,0,0)
(11,9,0),(0,2,1)
(11,10,1),(0,1,0)
(11,2,0),(0,9,1)
(11,3,1),(0,8,0)
(3,3,0),(8,8,1)
(4,4,1),(7,7,0)
(0,0,0),(11,11,1)

The path in BFS if boat capaticy is 9:
(11,11,1),(0,0,0)
(11,3,0),(0,8,1)
(11,4,1),(0,7,0)
(3,3,0),(8,8,1)
(4,4,1),(7,7,0)
(0,0,0),(11,11,1)

The path in BFS if boat capaticy is 10:
(11,11,1),(0,0,0)
(11,6,0),(0,5,1)
(11,7,1),(0,4,0)
(4,4,0),(7,7,1)
(5,5,1),(6,6,0)
(0,0,0),(11,11,1)
'''
