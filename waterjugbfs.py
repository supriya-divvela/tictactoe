def find_all_paths(G,start,goal):
    o,c=[[start]],[[start]]
    while len(o):
        t=o.pop(0)
        for i in G[t[-1]]:
            if i not in list(t):
                q=list(t)
                q.append(i)
                c.append(q)
                o.append(q)
    c=list(filter(lambda x:x[-1]==goal,c))
    return c
def func(x,y):
    l=[(0,y),(x,0),(m,y),(x,n)]
    if (x+y)<=m and y>0:l.append((x+y,0))
    if (x+y)<=n and x>0:l.append((0,x+y))
    if (x+y)>=m and y>0:l.append((m,y-(m-x)))
    if (x+y)>=n and x>0:l.append((x-(n-y),n))
    return list(set(l))
cp,cl,k=[],[],[]
m,n=map(int,input("Enter 2 jug capacties:").split())
res1,res2=map(int,input("Enter resultant capacities of 2 jug:").split())
G={}
cp.append((0,0))
cl.append((0,0))
if 0<=res1<=m and 0<=res2<=n:
    while cp:
        q=cp.pop(0)
        s=func(q[0],q[1])
        G[q]=[]
        for i in s:
            if i not in cl:
                G[q].append(i)
        for i in s:
            if i not in cl:
                cl.append(i)
                cp.append(i)
                if i==(res1,res2):
                    break
    if find_all_paths(G,(0,0),(res1,res2))!=[]:
        print("The path in BFS is:",find_all_paths(G,(0,0),(res1,res2)))
    else:
        print("It is not possible...")
else:
    print("Please enter appropriate values...")
'''
input:
Enter 2 jug capacties:5 3
Enter resultant capacities of 2 jug:4 0
output:
The path in BFS is: [[(0, 0), (5, 0), (2, 3), (2, 0), (0, 2), (5, 2), (4, 3), (4, 0)]]
'''
